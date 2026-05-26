pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/pratxmath-debug/titanic-ml-project.git'
            }
        }

        stage('Check Docker') {
            steps {
                sh 'which docker'
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t titanic-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5002:5000 titanic-app'
            }
        }
    }
}

