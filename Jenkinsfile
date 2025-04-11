pipeline {
    agent any 
    stages {
        stage ('CHECKOUT GIT') {
            steps {
                git credentialsId: 'MY_PAT', url:"https://github.com/gayathri7022/Practice.git", branch: "main"
            }
        }

        stage ('INSTALL DEPENDENCIES') {
            steps {
                bat '''
                    "C:\\Users\\mjmnj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                    call .\\venv\\Scripts\\activate && 
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage ('Test') {
            steps {
                bat '''
                call .\\venv\\Scripts\\activate
                pytest test.py
                '''
            }
                
        }

        stage ('Deploy') {
            steps {
                echo "Deploying Feature"
                bat '''
                call .\\venv\\Scripts\\activate
                pyhton calci.py
                '''
            }
        }

    }
}