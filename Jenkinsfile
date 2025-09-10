pipeline {
    agent {
        docker {
            image 'python:3.13-slim'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh "python -m unittest test_calc.py"
            }
        }
    }
}
