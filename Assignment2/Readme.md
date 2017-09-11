0) Starting docker
Run docker run -d --hostname my-rabbit --name some-rabbit3 -p 8080:15672 -p 5672:5672 -p 5671:5671 rabbitmq:3-management

1) Run the API gateway: 
Run python server.py

2) Start Node.js server:
Run docker pull harsha16/rabbitmq_services:node_server
docker run --link some-rabbit3:rabbit -p 8000:8000 harsha16/rabbitmq_services:node_server npm start

3) Start Java server:
Run docker pull harsha16/rabbitmq_services:java_server
docker run --link some-rabbit3:rabbit -w /java-service -p 8085:8080 harsha16/rabbitmq_services:java_server java Application
Go to http://localhost:8085/ (Important step!!)

4) Start Python client:
Run docker pull harsha16/rabbitmq_services:python_client
docker run --link some-rabbit3:rabbit -p 5000:5000 harsha16/rabbitmq_services:python_client python app.py

5) Test throigh UI
Go to http://localhost:7000/