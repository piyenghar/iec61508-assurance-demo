pipeline {
    agent {
        label 'ubuntu-gcc-sphinx'
    } 
    stages {
        stage('sphinx') {
            steps {
                sh 'pip install --break-system-packages uv'
                sh 'uv sync'
                sh 'uv run sphinx-build -a -E -j auto -b html docs/source docs/build/html 2> sphinx.log'
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: true, reportDir: 'docs/build/html', reportFiles: 'index.html', reportName: 'Sphinx Documentation', reportTitles: ''])
                recordIssues sourceCodeRetention: 'LAST_BUILD', tools: [sphinxBuild(pattern: 'sphinx.log')]
            }
        }

        stage('Deploy') {
            steps {
                sshPublisher(
                    continueOnError: false, 
                    failOnError: true,
                    alwaysPublishFromMaster: true,
                    publishers: [
                        sshPublisherDesc(
                        configName: "static_files-iecdemo",
                        transfers: [sshTransfer(sourceFiles: 'docs/build/html/**/*', removePrefix: 'docs/build/html')],
                        verbose: true
                        )
                    ]
                )
            }
        }

    }
}