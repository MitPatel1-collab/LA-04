pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-nginx-app"
        IMAGE_TAG  = "v${BUILD_NUMBER}"
        MINIKUBE_IP = "192.168.49.2"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image ${IMAGE_NAME}:${IMAGE_TAG}"
                sh """
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    docker save ${IMAGE_NAME}:${IMAGE_TAG} -o /tmp/${IMAGE_NAME}-${IMAGE_TAG}.tar
                """
            }
        }

        stage('Load Image to Minikube') {
    steps {
        echo 'Loading image into Minikube...'
        sh "docker save ${IMAGE_NAME}:${IMAGE_TAG} -o /tmp/image.tar"
        sh "minikube image load /tmp/image.tar || true"
    }
}

       stage('Deploy to Kubernetes') {
    steps {
        echo 'Deploying to Kubernetes...'
        sh "kubectl set image deployment/nginx-deployment nginx=${IMAGE_NAME}:${IMAGE_TAG}"
        sh "kubectl get pods"
    }
}

        stage('Verify Deployment') {
            steps {
                echo 'Verifying...'
                sh "kubectl get pods"
                sh "kubectl get deployments"
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded! Image: ${IMAGE_NAME}:${IMAGE_TAG}"
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}