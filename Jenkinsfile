node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
 sh 'docker stop microservice3 || true && docker rm microservice3 || true'
        app = docker.build("harsha/microservice3")
    }
    stage('Deploy'){
        def c = docker.image('harsha/microservice3').run('-p 6000:6000 --name microservice3')
    }


}
