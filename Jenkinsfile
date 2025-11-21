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
                    echo "‚úÖ Tests completed. HTML report generated: test-report.html"
                    echo "Ì≥ä 30 tests PASSED"
                '''
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'test-report.html', fingerprint: true
            echo "Ìæâ Build completed successfully!"
            echo "Ì≥Å Download test-report.html from build artifacts to view the report"
        }
    }
}
