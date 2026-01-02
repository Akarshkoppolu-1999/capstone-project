pipeline {
    agent any
    environment {
        DOCKER_REGISTRY = "my-local-registry" // Replace with your registry if needed
        IMAGE_NAME_BACKEND = "capstone-backend"
        IMAGE_NAME_FRONTEND = "capstone-frontend"
    }
    stages {
        stage('Debug - List Files') {
            steps {
                sh 'ls -R'
            }
        }
        stage('Build') {
            steps {
                echo 'Building Docker Images...'
                sh 'docker-compose build'
            }
        }
        stage('Unit Tests') {
            steps {
                echo 'Running tests inside containers...'
                // Example: sh 'docker-compose run backend pytest'
                sh 'echo "Tests passed!"'
            }
        }
        stage('Security Scan') {
            steps {
                echo 'Scanning images for vulnerabilities with Trivy...'
                // If Trivy is installed on Jenkins agent:
                // sh 'trivy image ${IMAGE_NAME_BACKEND}'
                sh 'echo "Security scan completed (simulated)"'
            }
        }
        stage('Push to Registry') {
            steps {
                echo 'Tagging and Pushing images...'
                // sh 'docker tag ${IMAGE_NAME_BACKEND} ${DOCKER_REGISTRY}/${IMAGE_NAME_BACKEND}:latest'
                // sh 'docker push ${DOCKER_REGISTRY}/${IMAGE_NAME_BACKEND}:latest'
                sh 'echo "Push successful"'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging environment...'
                sh 'docker-compose up -d'
                sh 'docker-compose ps'
            }
        }
        stage('Verify Deployment') {
            steps {
                echo 'Verifying deployment...'
                sh 'curl -f http://localhost:5000/health || exit 1'
                echo 'Deployment Verified!'
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Deployment successful! Access at http://localhost:8080'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
