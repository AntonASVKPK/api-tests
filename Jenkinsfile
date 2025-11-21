pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Verify Environment') {
            steps {
                bat '''
                    echo "Checking Python installation..."
                    python --version
                    pip --version
                    echo "Environment ready!"
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }
    }
    
    post {
        always {
            echo "=== Build completed ==="
        }
    }
}
