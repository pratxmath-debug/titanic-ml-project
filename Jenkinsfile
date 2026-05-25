pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python src/train.py'
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
