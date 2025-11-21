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
                    C:\\Python314\\python.exe -m pytest -v --html=test-report.html --self-contained-html
                    echo "Tests completed. HTML report generated."
                '''
            }
        }
        
        stage('Publish HTML Report') {
            steps {
                script {
                    // Альтернативный способ публикации HTML отчета
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '',
                        reportFiles: 'test-report.html',
                        reportName: 'HTML Test Report'
                    ])
                }
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'test-report.html', fingerprint: true
            echo "=== Build completed ==="
        }
    }
}
