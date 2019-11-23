pipeline {
    agent {
        docker {
            image 'stdiff/justatest-base'
        }
    }
    stages {
        stage("Environment check") {
            steps {
                sh "cat /tmp/nameplate"
                sh "docker images --filter=reference=stdiff/justatest-base --format \"{{.ID}}\""
                sh "cat /etc/os-releases"
                sh "python --version"
                sh "pip list"
            }
        }
        stage('Unit Test') {
            steps {
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