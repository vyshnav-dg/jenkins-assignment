pipeline {
    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID_JENKINS')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY_JENKINS')
        AWS_DEFAULT_REGION    = 'us-east-1'
    }

    agent {
        docker {
            image 'public.ecr.aws/sam/build-python3.13:1.148.0-20251122050712'
            args '-u root'
        }
    }

    stages {

        stage('Assume Deployment Role') {
            steps {
                script {
                    def roleJson = sh(
                        script: """
                            aws sts assume-role \
                              --role-arn arn:aws:iam::029756584744:role/3rdparty-jenkins-manage-cfn \
                              --role-session-name jenkins-session \
                              --query 'Credentials' \
                              --output json
                        """,
                        returnStdout: true
                    ).trim()

                    def creds = readJSON text: roleJson

                    env.AWS_ACCESS_KEY_ID     = creds.AccessKeyId
                    env.AWS_SECRET_ACCESS_KEY = creds.SecretAccessKey
                    env.AWS_SESSION_TOKEN     = creds.SessionToken
                }
            }
        }

        stage('Verify Identity After AssumeRole') {
            steps {
                sh 'aws sts get-caller-identity'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_calc.py'
            }
        }

        stage('Build the project') {
            steps {
                sh 'sam build'
            }
        }

        stage('Deploy to AWS') {
            steps {
                sh 'sam deploy --no-confirm-changeset --no-fail-on-empty-changeset'
            }
        }

    }
}
