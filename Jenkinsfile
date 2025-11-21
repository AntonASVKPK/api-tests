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
                bat 'C:\\Users\\Антон\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe --version'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\Антон\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\Антон\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe -m pytest -v'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
