pipeline {
    agent {
        label 'ubuntu-gcc-sphinx'
    } 
    stages {
        stage('sphinx') {
            steps {
                sh 'cd docs && make html 2> sphinx.log'
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'docs/build/html', reportFiles: 'index.html', reportName: 'Sphinx Documentation', reportTitles: '', useWrapperFileDirectly: true])
                recordIssues sourceCodeRetention: 'LAST_BUILD', tools: [sphinxBuild(pattern: 'docs/sphinx.log')]
            }
        }

    }
}