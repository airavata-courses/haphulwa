node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("harsha/gateway")
    }
    stage('Deploy'){
        def c = docker.image('harsha/gateway').run('--link some-rabbit3:rabbit -p 5000:5000')
    }


}