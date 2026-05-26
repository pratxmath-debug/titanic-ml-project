pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/pratxmath-debug/titanic-ml-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t titanic-app ./docker'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}

