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
        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_calc.py'
            }
        }

stage('Assume, Verify, Build and Deploy') {
    steps {
        script {
            sh """
                export \$(printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" \\
                    \$(aws sts assume-role \\
                        --role-arn arn:aws:iam::029756584744:role/3rdparty-jenkins-manage-cfn \\
                        --role-session-name jenkins-session \\
                        --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" \\
                        --output text))

                echo "Verify identity"
                aws sts get-caller-identity

                echo "Build project"
                sam build

                echo "Deploy to AWS"
                sam deploy --no-confirm-changeset --no-fail-on-empty-changeset
            """
        }
    }
}

    }
}
