var amqp = require('amqplib/callback_api');

amqp.connect('amqp://129.114.17.184:15672', function(err, conn) {
 conn.createChannel(function(err, ch) {
  var q = 'rpc_queue';

  ch.assertQueue(q, {
   durable: false
  });
  ch.prefetch(1);
  console.log(' [x] Awaiting RPC requests');
  ch.consume(q, function reply(msg) {
   var n = parseInt(msg.content.toString());

   console.log(" [.] fib(%d)", n);

   var r = fibonacci(n);
   console.log("Result", r);

   ch.sendToQueue(msg.properties.replyTo,
    new Buffer(r.toString()), {
     correlationId: msg.properties.correlationId
    });

   ch.ack(msg);
  });
 });
});

function fibonacci(n) {
    var a = 0, b = 1, c;
    if (n < 3) {
        if (n < 0) return fib(-n);
        if (n === 0) return 0;
        return 1;
    }
    while (--n)
        c = a + b, a = b, b = c;
    return c;
}
