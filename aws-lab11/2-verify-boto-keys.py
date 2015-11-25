import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import urllib2
import sys

# Get the keys and use them to connect to AWS
access_key = ""
secret_access_key = ""
keys = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read()
access_key, secret_access_key = keys.split(':')
print("Boto version: " + boto.Version)
print("Access key: " + access_key)
print("Secret key: " + secret_access_key)

