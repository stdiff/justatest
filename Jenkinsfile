pipeline {
    agent any

    stages {
        stage('Environment') {
            steps {
                echo 'Building..'
                sh 'virtualenv venv'
                sh """
                  source venv/bin/activate
                  pip install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh """
                  source venv/bin/activate
                  python -m unittest test/test_your_function.py
                """
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}