pipeline {
    agent any

    stages {
        stage('cloning the repo') {
            steps {
                shell("git clone -b trigger https://github.com/Shashwatsingh22/Dynamically-Firwall-Update")
            }
        }

        stage('start script') 
        {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                 script{
                         shell("bash /var/lib/jenkins/workspace/updateFirewall/script.sh")
                 }
                }
            }
        }

        stage ('confirmation')
        {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE'){
                 
                script{
                    shell('cat /home/ubunutu/pythonScriptForAutomation/jenkins.log')
                }

            }
        }
        }
    }       
}    