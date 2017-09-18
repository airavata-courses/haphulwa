import pika
import uuid
import os
from flask import Flask
from flask import request,render_template,send_from_directory
from flask_cors import CORS,cross_origin
import socket
app = Flask(__name__, static_url_path='')
CORS(app)

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='my-rabbit'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,queue=self.callback_queue)
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

class FactorialRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='my-rabbit'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_fact_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)
		
class PrimeRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='my-rabbit'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,queue=self.callback_queue)
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_prime_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

@app.route("/fibonacci", methods=['GET', 'POST'])
def say_hello():
	message = str(request.args.get('number'))
	print('msg');
	fibonacci_rpc = FibonacciRpcClient()
	response = fibonacci_rpc.call(int(message))
	return str(response);
	
@app.route("/factorial", methods=['GET', 'POST'])
def say_hello2():
	message = str(request.args.get('number2'))
	factorial_rpc = FactorialRpcClient()
	response = factorial_rpc.call(int(message))
	return str(response);
	
@app.route("/prime", methods=['GET', 'POST'])
def say_hello3():
	message = str(request.args.get('number3'))
	prime_rpc = PrimeRpcClient()
	response = prime_rpc.call(int(message))
	if response==1:
		return "Not prime"
	else:
		return "Prime"
	
@app.route('/')
def runit():
	return """
	<!DOCTYPE html>
<html>
   <head>
      <title> RPC Microservices </title>
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
      <script>
         $(document).ready(function() {
         $("#calculate").click(function(){
         $.ajax({url: "http://129.114.17.184:5000/fibonacci", 
         data:{number: $("#number").val()}, 
         type:"GET", 
         success: function(result){
         document.getElementById('hello_msg').innerHTML = result;
         }});
         });
         $("#calculate2").click(function(){
         $.ajax({url: "http://129.114.17.184:5000/factorial", 
         data:{number2: $("#number2").val()}, 
         type:"GET", 
         success: function(result){
         document.getElementById('hello_msg2').innerHTML = result;
         }});
         });
		  $("#calculate3").click(function(){
         $.ajax({url: "http://129.114.17.184:5000/prime", 
         data:{number3: $("#number3").val()}, 
         type:"GET", 
         success: function(result){
         document.getElementById('hello_msg3').innerHTML = result;
         }});
         });
         });
      </script>
   </head>
   <body>
      <h4><i> Flow: Api Gateway(Python) -> Server(Node.js Microservice) [RPC RabbitMQ model] </i></h4>
      Fibonacci: Enter no: <input type="text" id="number"/>
      <button id="calculate">Calculate</button>
      <br/>
      <div id="hello_msg"></div>
      <br/>
      <h4><i> Flow: Api Gateway(Python) -> Server(Java Microservice) [RPC RabbitMQ model] </i></h4>
      Factorial: Enter no: <input type="text" id="number2"/>
      <button id="calculate2">Calculate</button>
      <br/>
      <div id="hello_msg2"></div>
      <br/>
	  <h4><i> Flow: Api Gateway(Python) -> Server(Python Microservice) [RPC RabbitMQ model] </i></h4>
      Prime: Enter no: <input type="text" id="number3"/>
      <button id="calculate3">Calculate</button>
      <br/>
      <div id="hello_msg3"></div>
   </body>
</html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)