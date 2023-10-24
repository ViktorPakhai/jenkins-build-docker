pipeline {
    environment {
        registry = "sdgadmin/docker-test"
    	registryCredential = "DockHub_sdgadmin"
    	dockerImage = ''
    }
    agent any
    stages {
        stage('Cloning our Git') {
            steps {

                git branch: 'main',
                credentialsId: 'GitHub',
                url: 'https://github.com/ViktorPakhai/jenkins-build-docker.git'
                sh "ls -lat"
            }
        }
        stage('Building our image') {
            steps {
                script {
                    echo "Building our image stage"
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps {
                sh "docker rmi $registry"
            }
        }
        stage('SDG finish') {
            steps {
                echo "Finish"
            }
        }
    }
}
