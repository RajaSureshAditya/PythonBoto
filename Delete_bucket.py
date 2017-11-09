#!/usr/bin/env python

import boto3

import sys

s3 = boto3.resource('s3')

bucket_name = sys.argv[1]

for bucket in sys.argv[1:]:
    resbucket = s3.Bucket(bucket)
    try:
        resbucket.object_versions.delete()
        response = resbucket.delete()
        print response
    except Exception as error:
        print error
