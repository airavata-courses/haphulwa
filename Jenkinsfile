node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */
      sh '''sudo docker ps -q --filter "name=gateway" | grep -q . && sudo docker stop msp && sudo docker rm -fv gateway'''
        app = docker.build("harsha/gateway")
    }
    stage('Deploy'){
        def c = docker.image('harsha/gateway').run('-p 5000:5000 --name gateway')
    }
}
