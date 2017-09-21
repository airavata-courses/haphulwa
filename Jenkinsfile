node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
sh 'docker stop microservice2 || true && docker rm microservice2 || true'
        app = docker.build("harsha/microservice2")
    }
    stage('Deploy'){
        def c = docker.image('harsha/microservice2').run('-p 8000:8000 --name microservice2')
    }


}
