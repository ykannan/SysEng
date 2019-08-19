import boto3
import logging
import argparse

session = boto3.Session(profile_name='default')
client = session.client('ec2')

def get_volumes():
    """
    This functions gets a list of all available volumes.That can be marked for deletion
    """
    ec2 = boto3.resource('ec2',region_name='us-east-1')
    vol= ec2.volumes.filter(
        Filter = [
            {'Name': 'status',
            'Values': ['available']}
        ]
    )
    x = [volume for volume in vol]
    print(x)

