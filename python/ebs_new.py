#ebs_new.py
import boto3
import argparse
import logging
from botocore.exceptions import ClientError

def parser_args():
    parser = argparse.ArgumentParser(description="This is a test script")
    parser.add_argument ("-res","--resource", help="resource", required = True )
    parser.add_argument ("-reg","--regions", help="regions", required=True)
    args = parser.parse_args()
    return args
​
def get_client(resource, region):
    return boto3.resource(resource, region)
​
def get_volumes(resource, region):
    try:
        client = get_client(resource, region)
        response = client.volumes.filter(
            Filters = [{'Name':'status', 'Values':['available']}]
            )
        vol = [vol.id for vol in response]
        return vol
        print(vol)
        logging.info('This is thevolume present {v}'.format(v=vol))
    except ValueError as e:
        logging.error(str(e))
    except NameError as e:
        logging.error(str(e))
    except ClientError as e:
        logging.error(str(e))

log_file = '/Users/ykannan/Desktop/untitled folder/test_error.txt'
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)
​
if __name__=='__main__':
    args = parser_args()
    get_volumes(args.resource, args.regions)