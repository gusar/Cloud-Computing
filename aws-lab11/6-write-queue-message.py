import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import urllib2
import sys

access_key = ""
secret_access_key = ""
keys = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read()
access_key, secret_access_key = keypart1.split(':')

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key=access_key, aws_secret_access_key=secret_access_key)

message = Message()
queue = sys.argv[1]
msg.set_body(sys.argv[2])

q = conn.get_queue(queue)
q.write(message)

print("Message \"" + sys.argv[2] + "\" written to queue " + sys.argv[1])
