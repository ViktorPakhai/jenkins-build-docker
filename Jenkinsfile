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
                    sh "echo  $registry"
                }
            }
        }
        stage('Cleaning up') {
            steps {
                sh "echo "Cleaning up""
            }
        }
        stage('SDG finish') {
            steps {
                sh "echo "Finish""
            }
        }
    }
}
