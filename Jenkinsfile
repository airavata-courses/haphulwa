node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
sh 'docker stop microservice1 || true && docker rm microservice1 || true'
        app = docker.build("harsha/microservice1")
    }
    stage('Deploy'){
        def c = docker.image('harsha/microservice1').run('-w /java-service -p 8085:8080 --name microservice1')
    }


}
