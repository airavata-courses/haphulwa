from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import AdditionService

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = AdditionService.Client(protocol)
    transport.open()
    product = client.add(4, 5)
    print('Add result by Python client :', product)
    transport.close()
except:
    print('Connection Error')
