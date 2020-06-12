pipeline {
  agent {
    kubernetes {
      label 'nodejs'
      yamlFile 'nodejs-pod.yml'
    }
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
    skipDefaultCheckout true
  }
  stages {
    stage('Setup') {
      steps {
        container('nodejs') {
         checkout scm
         sh 'yarn install'
        }
      }
    }
    stage('Tests') {
      parallel {
        stage('Lint') {
          steps {
            container('nodejs') {
              sh 'pwd;ls'
              sh 'yarn lint'
            }
          }
        }
        stage('Unit tests') {
          steps {
            container('nodejs') {
              sh 'ls'
              sh 'yarn test'
            }
          }
        }
      }
    }
    stage('Build and Push Image') {
      when {
        beforeAgent true
        branch 'master'
      }
      steps {
        container('kaniko') {
          sh """#!/busybox/sh
            /kaniko/executor --context `pwd` --destination gcr.io/ldonley/vue-hn-clone:${env.COMMIT_ID} --cache=true
          """
        }
      }
    }
  }
}
