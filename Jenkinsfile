pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = 'ghcr.io/khris-xp'
        IMAGE_NAME = 'spdx-jenkins-assignment'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh 'npm run test'
            }
        }

        stage('Build') {
            steps {
                sh 'npm run build'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://ghcr.io', 'khris-xp') {
                        docker.image("${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}").push()
                        docker.image("${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}").push('latest')
                    }
                }
            }
        }

        stage("robot") {
            agent { label 'test' }
            steps {
                echo 'Check for ./robot/'
                sh 'mkdir -p robot'
                echo 'Cloning Robot'
                dir('./robot/') {
                    git branch: 'main', url: "${ROBOT_GIT}"
                }
                echo 'Run Robot'
                sh 'cd robot && python3 -m  robot --outputdir ${ROBOT_RESULTS} \
                        --xunit output.xml \
                        --test '*' \
                        tests/api_tests.robot'
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    docker stop nestjs-api || true
                    docker rm nestjs-api || true
                    docker run -d --name nestjs-api -p 3000:3000 ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }
    
    post {
        always {
            junit 'junit.xml'
            robot 'robot-tests/reports'
        }
    }
}