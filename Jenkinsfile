pipeline {
  agent {
    docker {
      image 'stdiff/justatest-base'
      args '-u root:sudo'
    }
  }
  options {
      timeout(time: 1)
  }
  stages {
    stage('Environment check') {
      steps {
        sh 'cat /tmp/nameplate'
        sh 'cat /etc/os-release'
        sh 'whoami'
        sh 'python --version'
        sh 'pip list'
      }
    }
    stage('Unit Test') {
      steps {
        sh 'python -m unittest test/test_my_function.py'
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
      }
    }
  }
}