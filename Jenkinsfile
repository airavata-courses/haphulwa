node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("harsha/microservice1")
    }
    stage('Deploy'){
        def c = docker.image('harsha/microservice1').run('-w /java-service -p 8085:8080')
    }


}
