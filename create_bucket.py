#!/usr/bin/env python
import boto3
import sys

s3=boto3.resource('s3')

for bucketname in sys.argv[1:]:
    response=s3.create_bucket(Bucket=bucketname,CreateBucketConfiguration= {'LocationConstraint':'us-west-2'})
    print response

