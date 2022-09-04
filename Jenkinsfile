pipeline {
    agent any

    parameters {
        string defaultValue: '192.168.0.3', name: 'EXECUTOR'
        string defaultValue: 'http://192.168.0.3:8081', name: 'OPENCART_URL'
        string defaultValue: 'chrome', name: 'BROWSER'
        string defaultValue: '102.0', name: 'BROWSER_VERSION'
        string defaultValue: '1', name: 'THREADS'
    }

    stages {
        stage('tests') {
            steps {
                sh """
                    PATH=$PATH:$PWD/build
                    python3 -m venv venv
                    . venv/bin/activate
                    pip3 install -r requirements.txt
                    pytest -v tests --executor ${EXECUTOR} --url ${OPENCART_URL} --browser ${BROWSER} --browser_version ${BROWSER_VERSION} --vnc -n ${THREADS}
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
