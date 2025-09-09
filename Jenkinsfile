pipeline {
    agent {
        docker {
            image 'python:latest'
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