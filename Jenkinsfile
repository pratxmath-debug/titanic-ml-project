pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
               git branch: 'main', url: 'https://github.com/pratxmath-debug/titanic-ml-project.git'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python --version || python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || pip3 install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train_model.py || python3 train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t titanic-app -f docker/Dockerfile .'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}

