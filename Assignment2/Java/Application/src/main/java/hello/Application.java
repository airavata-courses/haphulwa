package hello;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RestController;
import com.rabbitmq.client.*;
import java.io.IOException;
import java.util.concurrent.TimeoutException;

@SpringBootApplication
@RestController
public class Application {
 private static final String RPC_QUEUE_NAME = "rpc_fact_queue";
 String response = "";
 @CrossOrigin(origins = "*")
 @RequestMapping("/")
 public String home() throws IOException, TimeoutException {
  ConnectionFactory factory = new ConnectionFactory();
  factory.setHost("my-rabbit");

  Connection connection = null;

  try {
   connection = factory.newConnection();
   final Channel channel = connection.createChannel();
	System.out.println(connection);
	System.out.println(channel);
   channel.queueDeclare(RPC_QUEUE_NAME, false, false, false, null);

   channel.basicQos(1);

   System.out.println(" [x] Awaiting RPC requests");

   Consumer consumer = new DefaultConsumer(channel) {
    @Override
    public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
     AMQP.BasicProperties replyProps = new AMQP.BasicProperties
      .Builder()
      .correlationId(properties.getCorrelationId())
      .build();



     try {
      String message = new String(body, "UTF-8");
      int n = Integer.parseInt(message);

      System.out.println(" [.] factorial(" + message + ")");
      response = String.valueOf(factorial(n));
	  System.out.println(" factorial" + response);
     } catch (RuntimeException e) {
      System.out.println(" [.] " + e.toString());
     } finally {
      channel.basicPublish("", properties.getReplyTo(), replyProps, response.getBytes("UTF-8"));

      channel.basicAck(envelope.getDeliveryTag(), false);
     }
    }
   };

   channel.basicConsume(RPC_QUEUE_NAME, false, consumer);

   //...
  } finally {}
  return response;
 }
 public static void main(String[] args) {
  SpringApplication.run(Application.class, args);
 }
 private static int factorial(int n) {
  if (n == 0)
   return 1;
  else
   return (n * factorial(n - 1));
 }
}