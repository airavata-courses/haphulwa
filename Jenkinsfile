node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("harsha/microservice3")
    }
    stage('Deploy'){
        def c = docker.image('harsha/microservice3').run('--link some-rabbit3:rabbit -p 6000:6000 harsha16/rabbitmq_services:python_server')
    }


}