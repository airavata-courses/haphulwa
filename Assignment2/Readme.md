1) Run the API gateway: 
Run python server.py
Go to http://localhost:7000/

2) Start Node.js server:
Run docker pull harsha16/rabbitmq_services:node_server
docker run -p 8000:8000 harsha16/rabbitmq_services:node_server npm start

3) Start Java server:
Run docker pull harsha16/rabbitmq_services:java_server
docker run -d -w /java-service -p 8080:8080 harsha16/rabbitmq_services:java_server java Application

4) Start Python client:
Run docker pull harsha16/rabbitmq_services:python_client
docker run -p 5000:5000 -d harsha16/rabbitmq_services:python_client python app.py