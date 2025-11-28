pipeline {
    agent {
        docker {
            image 'public.ecr.aws/sam/build-python3.13:1.148.0-20251122050712'
            args '-u root'
        }
    }

    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID_JENKINS')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY_JENKINS')
        AWS_DEFAULT_REGION    = 'us-east-1'
    }

    stages {

        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_calc.py'
            }
        }

        stage('Assume, Build and Deploy') {
            steps {
                script {
                    sh """
                        set -e

                        read AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN <<< \\
                        \$(aws sts assume-role \\
                            --role-arn arn:aws:iam::029756584744:role/3rdparty-jenkins-manage-cfn \\
                            --role-session-name jenkins-session-\$BUILD_NUMBER \\
                            --query 'Credentials.[AccessKeyId,SecretAccessKey,SessionToken]' \\
                            --output text)

                        export AWS_ACCESS_KEY_ID
                        export AWS_SECRET_ACCESS_KEY
                        export AWS_SESSION_TOKEN

                        aws sts get-caller-identity

                        sam build
                        sam deploy --no-confirm-changeset --no-fail-on-empty-changeset
                    """
                }
            }
        }

    }
}
