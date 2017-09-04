# Assignment 1

*Design:* Have implemented 3 microservices in Spring MVC , Python & Flask , Node.js & Express.
All the 3 microservices just display a Hello World message.

### General instructions:
* Install Docker [Link](https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows)
*  Enable Hyper-V [Link](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v)

### Java Microservice:
* Run docker pull harsha16/helloworld_microservices:hello_java
* Run docker run -d -w /java-service -p 8080:8080 harsha16/helloworld_microservices:hello_java java Application
* Java Microservice -> http://localhost:8080

### Python Microservice
* Run docker pull harsha16/helloworld_microservices:hello_python
* Run docker run -p 5000:5000 -d harsha16/helloworld_microservices:hello_python python app.py
* Python Microservice -> http://localhost:5000

### Node.js Microservice
* Run docker pull harsha16/helloworld_microservices:hello_node
* Run docker run -p 8000:8000 -d harsha16/helloworld_microservices:hello_node npm start
* Python Microservice -> http://localhost:8000

### References:
* https://spring.io/guides/gs/spring-boot-docker/#scratch
* https://runnable.com/docker/java/dockerize-your-java-application
* https://docs.docker.com/compose/gettingstarted/#step-1-setup
* https://nodejs.org/en/docs/guides/nodejs-docker-webapp/