#ebs.py
import boto3
import logging
import argparse
from botocore.exceptions import EndpointConnectionError

log_file = "error.txt"
logging.basicConfig(
    filename = log_file,
    level = logging.INFO,
    format = '%(asctime)s -%(levelname)s-%(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
    )

def parser_args():
    parser = argparse.ArgumentParser(description = 'These arguments are used for parsing the regions and resources')
    parser.add_argument('-reg', '--region', help = 'enter region', required = True)
    parser.add_argument('-res', '--resource', help ='enter resource', default = 'ec2')
    args = parser.parse_args()
    return args

def get_client(resource, region):
    return boto3.resource(resource, region)

def get_volumes(resource, region):
    """
    This functions gets a list of all available volumes.That can be marked for deletion
    """
    global client
    client = get_client(resource, region)
    try:
        global vol
        vol= client.volumes.filter(Filters = [{'Name': 'status','Values': ['available']}])
        try:
            global i
            for i in vol:
                logging.info('Volumes Available: ' + str(i.id))
                print('Volumes Available: ' + str(i.id))
        except:
            print ('Error in for loop')
    except EndpointConnectionError as e:
        logging.error(e)
        
    delete_volumes()


def delete_volumes():
    try:
        for i in vol:
            v = client.Volume(i.id)
            v.delete()
            logging.info('Volumes Delete: ' +str(v.id))
            print('Volumes Delete: ' +str(v.id))
    
    except EndpointConnectionError as e:
        logging.error(e)



args = parser_args()
get_volumes(args.resource, args.region)




