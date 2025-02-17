pipeline {
    agent {
        label 'test-agent'
    }

    environment {
        IMAGE_NAME = 'ghcr.io/sdpx-2024/sdpx-jenkins-assignment'
        // REGISTRY_CREDENTIALS = credentials('ghcr-credentials')
        REGISTRY_CREDENTIALS = credentials('ghcr-pat')
        DOCKER_CREDENTIALS = credentials('docker-credentials')
        APP_NAME = 'plus-api'
        ROBOT_REPO = 'https://github.com/hello-ce/sdpx-robots-testing'
        ROBOT_BRANCH = 'main'
    }

    stages {
        stage("Install & Run Unit Tests") {
            steps {
                sh "pip install -r requirements.txt"
                sh "python3 unit_test.py"
            }
        }

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_ID} ."
            }
        }

        stage('Run Container & Run Robot Testing') {
            steps {
                sh "docker run -dp 5000:5001 --name ${APP_NAME} ${IMAGE_NAME}:${BUILD_ID}"
                git branch: "${ROBOT_BRANCH}", url: "${ROBOT_REPO}"
                sh "robot plus.robot"
            }

            post {
                always {
                    sh returnStatus: true, script: "docker stop ${APP_NAME}"
                    sh returnStatus: true, script: "docker rm ${APP_NAME}"
                }
            }
        }

        stage('Push Image to Registry') {
            steps {
                sh 'echo $DOCKER_CREDENTIALS_PSW  | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin'
                sh "docker push ${DOCKER_CREDENTIALS_USR}/spdx-jenkins-assignment:${BUILD_ID}"
            }
        }

        stage('Deploy') {
            agent {
                label 'uat-agent'
            }
            steps {
                sh returnStatus: true, script: "docker stop ${APP_NAME}"
                sh returnStatus: true, script: "docker rm ${APP_NAME}"
                sh 'echo $DOCKER_CREDENTIALS_PSW  | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin'
                sh "docker pull ${DOCKER_CREDENTIALS_USR}/spdx-jenkins-assignment:${BUILD_ID}"
                sh "docker run -dp 5000:5001 --name ${APP_NAME} ${DOCKER_CREDENTIALS_USR}/spdx-jenkins-assignment:${BUILD_ID}"
            }
        }
    }
}