# Assignment 2

### Starting RabbitMQ on docker:
* Run docker run -d --hostname my-rabbit --name some-rabbit3 -p 8080:15672 -p 5672:5672 -p 5671:5671 rabbitmq:3-management

### Start Node.js server: (In a new terminal) 
* Run docker pull harsha16/rabbitmq_services:node_server
* Run docker run --link some-rabbit3:rabbit -p 8000:8000 harsha16/rabbitmq_services:node_server npm start

### Start Java server:  (In a new terminal) 
* Run docker pull harsha16/rabbitmq_services:java_server
* Run docker run --link some-rabbit3:rabbit -w /java-service -p 8085:8080 harsha16/rabbitmq_services:java_server java Application
* Go to http://localhost:8085/ (Important step!!)

### Start Python Server:  (In a new terminal) 
* Run docker pull harsha16/rabbitmq_services:python_server
* Run docker run --link some-rabbit3:rabbit -p 6000:6000 harsha16/rabbitmq_services:python_server python app.py

### API gateway
* Run docker pull harsha16/rabbitmq_services:python_client
* Run docker run --link some-rabbit3:rabbit -p 5000:5000 harsha16/rabbitmq_services:python_client python client.py
* Go to http://localhost:5000 

