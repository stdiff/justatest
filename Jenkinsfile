pipeline {
    agent {
        docker {
            image 'stdiff/justatest-base'
        }

    }
    stages {
        stage('Unit Test') {
            steps {
                echo 'Testing..'
                sh "python -m unittest test/test_my_function.py"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}