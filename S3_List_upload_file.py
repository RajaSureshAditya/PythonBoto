from ast import Try
from distutils.log import debug, info
import boto3
import os
import pprint
import logging
from botocore.exceptions import ClientError

os.environ['AWS_PROFILE'] = "default"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"
# boto3.set_stream_logger('botocore', level='DEBUG')


def create_temp_tenant_session(access_role_arn, session_name, tenant_id, duration_sec):
    """
    Create a temporary session
    :param access_role_arn: The ARN of the role that the caller is assuming
    :param session_name: An identifier for the assumed session
    :param tenant_id: The tenant identifier the session is created for
    :param duration_sec: The duration, in seconds, of the temporary session
    :return: The session object that allows you to create service clients and resources
    """
    sts = boto3.client('sts')
    assume_role_response = sts.assume_role(
        RoleArn=access_role_arn,
        DurationSeconds=duration_sec,
        RoleSessionName=session_name,
        Tags=[
            {
                'Key': 'TenantID',
                'Value': tenant_id
            }
        ]
    )
    session = boto3.Session(aws_access_key_id=assume_role_response['Credentials']['AccessKeyId'],
                    aws_secret_access_key=assume_role_response['Credentials']['SecretAccessKey'],
                    aws_session_token=assume_role_response['Credentials']['SessionToken'])
    return session

def get_tenant_objects(session):
    s3_client_v2 = session.client('s3')
    response = s3_client_v2.list_objects_v2(Bucket='vcommonbucket')
    for content in response['Contents']:
        try:
            obj_dict = s3_client_v2.get_object(Bucket='vcommonbucket', Key=content['Key'])
            print(content['Key'], obj_dict['LastModified'])
        except:
            print("user doesn't have access to "+content['Key']+" of s3 folder ")

def update_file_in_s3_coke(session,filename):
    s3_client_v2 = session.client('s3')
    try:
        response = s3_client_v2.upload_file("/Users/adi/go/src/docker-go-healthcheck/README.md", "vcommonbucket", '%s/%s' % (filename,"Readme.md"))
    except ClientError as e:
        logging.error(e)
        print(e)
        return False
    print(response)


def main():
  session = create_temp_tenant_session("arn:aws:iam::699601524344:role/TrackingAccessRole","TenantID97","coke",900)
  update_file_in_s3_coke(session,"coke")
  
if __name__ == "__main__":
    main()
