/* Requires the Docker Pipeline plugin */
pipeline {
    none
    options{
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python --version'
            }
        }
    }
}