pipeline {
    agent {
        docker {
            image 'ubuntu:v1_m'
        }
    }
    stages {
        stage ('Build') {
            steps {
                sh '''
                echo "Hello world"
                hostname
                '''
            }
        }
    }
}