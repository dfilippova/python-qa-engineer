pipeline {
    agent any

    stages {
        stage('tests') {
            steps {
                sh """
                    PATH=$PATH:$PWD/build
                    python3 -m venv venv
                    . venv/bin/activate
                    pip3 install -r requirements.txt
                    pytest -v tests --vnc
                """
            }
        }
        stage('report-allure') {
            steps {
                script {
                    allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
    }
}
