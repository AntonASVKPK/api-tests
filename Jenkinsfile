pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                bat '''
                    echo "Setting up Python..."
                    where python
                    where py
                    C:\\Python312\\python.exe --version
                    C:\\Python312\\Scripts\\pip.exe --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Python312\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'C:\\Python312\\python.exe -m pytest -v'
            }
        }
    }
}
