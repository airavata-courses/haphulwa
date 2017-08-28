<?php
require_once __DIR__.'/Thrift/ClassLoader/ThriftClassLoader.php';
use Thrift\ClassLoader\ThriftClassLoader;
$GEN_DIR = dirname(__FILE__).'/gen-php';
$loader = new ThriftClassLoader();
$loader->registerNamespace('Thrift', __DIR__);
$loader->registerDefinition('add', $GEN_DIR);
$loader->register();
use Thrift\Protocol\TBinaryProtocol;
use Thrift\Transport\TSocket;
use Thrift\Transport\THttpClient;
use Thrift\Transport\TBufferedTransport;
use Thrift\Exception\TException;
try
{
    $socket = new Thrift\Transport\TSocket('127.0.0.1', 9090);
    $transport = new Thrift\Transport\TBufferedTransport($socket, 1024, 1024);
    $protocol = new Thrift\Protocol\TBinaryProtocol($transport);
    $client = new \add\AdditionServiceClient($protocol);
    $transport->open();
    echo 'Add result by PHP client is : ' . $client->add(2,7);
}
catch (Exception $e)
{
    echo "Exception: %e\r\n";
}