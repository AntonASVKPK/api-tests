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
                bat 'C:\\Python314\\python.exe --version'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Python314\\Scripts\\pip.exe install -r requirements.txt'
            }
        }
        
        stage('Run Tests with HTML Report') {
            steps {
                bat '''
                    C:\\Python314\\python.exe -m pytest -v --html=report.html --self-contained-html
                '''
            }
        }
    }
    
    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '',
                reportFiles: 'report.html',
                reportName: 'HTML Test Report'
            ])
            echo "=== Build with HTML report completed ==="
        }
    }
}
