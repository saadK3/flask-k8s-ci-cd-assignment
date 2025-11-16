// Jenkinsfile (Windows Version)

pipeline {
    agent any

    stages {

        // STAGE 1: Build the Docker Image
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'

                powershell '''
            minikube -p minikube docker-env | Invoke-Expression
            docker build -t flask-app:latest .
        '''

            echo 'Docker image built successfully.'
            }
        }

        // STAGE 2: Deploy to Kubernetes
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                bat 'kubectl apply -f kubernetes/'
            }
        }

        // STAGE 3: Verify Deployment
        stage('Verify Deployment') {
            steps {
                echo 'Verifying deployment rollout...'
                bat 'kubectl rollout status deployment/flask-app'

                echo 'Deployment successful! Showing running pods and services:'
                bat 'kubectl get pods,services'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up shell environment...'
            // This is the Windows/PowerShell way to unset the env vars
            powershell 'minikube -p minikube docker-env -u | Invoke-Expression'
        }
    }
}
