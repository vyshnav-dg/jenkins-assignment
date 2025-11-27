pipeline {
    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION    = 'us-east-1'
    }

    agent {
        docker {
            image 'public.ecr.aws/sam/build-python3.13:1.148.0-20251122050712'
        }
    }

    stages {
        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_calc.py'
            }
        }
        stage('Display AWS creds') {
            steps {
                sh "aws sts get-caller-identity"
            }
        }
        stage('Build the project') {
            steps {
                sh 'sam build'
            }
        }
        stage('Deploy to AWS') {
            steps {
                sh "sam deploy --no-confirm-changeset --no-fail-on-empty-changeset"
            }
        }
    }
}
