package add;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

import add.AdditionService;

public class AdditionServer {
	 public static void StartsimpleServer(AdditionService.Processor<AdditionServiceHandler> processor) {
	        try {
	            TServerTransport serverTransport = new TServerSocket(9090);
	            TServer server = new TSimpleServer(
	                    new TServer.Args(serverTransport).processor(processor));
	            System.out.println("Starting the simple server...");
	            server.serve();
	        } catch (Exception e) {
	            e.printStackTrace();
	        }
	    }

	    public static void main(String[] args) {
	        StartsimpleServer(new AdditionService.Processor<>(new AdditionServiceHandler()));
	    }
}
