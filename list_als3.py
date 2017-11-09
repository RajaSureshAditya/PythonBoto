#!/usr/bin/env python

import boto3

s3 = boto3.resource('s3')

for sss in s3.buckets.all():
    print sss.name
    print "========="
    for bbb in sss.objects.all():
        print "\t%s" % bbb.key
