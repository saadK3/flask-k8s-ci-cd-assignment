pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker Image...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Kubernetes...'
            }
        }
    }
}