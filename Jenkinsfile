// Jenkinsfile

pipeline {
    agent any // This means Jenkins can run this on any available machine

    stages {

        // STAGE 1: Build the Docker Image
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'

                // This is a CRUCIAL trick for Minikube.
                // It tells your terminal to use Minikube's *internal* Docker.
                // This builds the image *inside* the Minikube virtual machine.
                sh 'eval $(minikube -p minikube docker-env)'

                // Now, 'docker build' builds the image where Minikube can find it.
                // This is why 'imagePullPolicy: IfNotPresent' (from Task 3) works.
                sh 'docker build -t flask-app:latest .'

                echo 'Docker image built successfully.'
            }
        }

        // STAGE 2: Deploy to Kubernetes
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'

                // This command tells kubectl to apply our new configurations.
                // It will automatically start a 'RollingUpdate' because of your Task 3 work.
                sh 'kubectl apply -f kubernetes/'
            }
        }

        // STAGE 3: Verify Deployment
        stage('Verify Deployment') {
            steps {
                echo 'Verifying deployment rollout...'

                // This command waits for the rolling update to be 100% complete
                sh 'kubectl rollout status deployment/flask-app-deployment'

                // This prints the final status of our app
                echo 'Deployment successful! Showing running pods and services:'
                sh 'kubectl get pods,services'
            }
        }
    }

    post {
        // This 'always' block runs at the end, whether the pipeline passed or failed
        always {
            echo 'Pipeline finished. Cleaning up shell environment...'
            // This 'unsets' the Minikube Docker environment variables.
            // It's just good practice to clean up.
            sh 'eval $(minikube -p minikube docker-env -u)'
        }
    }
}
