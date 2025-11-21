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
                    echo "Using Python 3.14 from C:\\Python314\\"
                    C:\\Python314\\python.exe --version
                    C:\\Python314\\Scripts\\pip.exe --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Python314\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'C:\\Python314\\python.exe -m pytest -v'
            }
        }
    }
}
