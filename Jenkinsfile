pipeline {
  agent {
    docker {
      image 'stdiff/justatest-base'
      arg '-u worker'
    }
  }
  stages {
    stage('Environment check') {
      steps {
        sh 'cat /tmp/nameplate'
        sh 'cat /etc/os-release'
        sh 'git log -1'
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