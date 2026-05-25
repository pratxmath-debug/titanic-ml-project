pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
which python3
python3 --version
python3 -m ensurepip --upgrade || true
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
'''
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 src/train.py'
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
