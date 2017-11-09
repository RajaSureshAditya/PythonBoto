#!/usr/bin/env python

import boto3

import sys

s3 = boto3.resource('s3')

bucket_name = sys.argv[1]

for bucket in sys.argv[1:]:
    resbucket = s3.Bucket(bucket)
    for key in resbucket.objects.all():
        try:
            response = key.delete()
            print response
        except Exception as error:
            print error
