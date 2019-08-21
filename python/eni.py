#eni.py
# command : python .\eni.py  -host test -sub subnet-66f7db3a  -sec sg-b0a56bef -i i-00a87a843a2a12f9f
import boto3 
import logging
import argparse
from botocore.exceptions import ClientError


def parse_args():
    parser = argparse.ArgumentParser(description='These arguments are needed for creating and attaching the ENI')
    parser.add_argument('-sec', '--security', help='Pass Security Group', required = True)
    parser.add_argument('-sub', '--subnet', help='Pass Subnet', required = True)
    parser.add_argument('-host', '--hostname', help='Pass hostname', required = True)
    parser.add_argument('-log', '--logfile', help='Pass log file location', default = "C:\\Users\\Yogesh\\Desktop\\SysEng\\python\\logs.txt")
    parser.add_argument('-reg', '--region', help='Pass Region', default = 'us-east-1')
    parser.add_argument('-inst', '--instance', help='Pass Insatnce ID', required = True)
    args = parser.parse_args()
    return args




def get_client(region):
    return boto3.client('ec2', region)


def create_eni(client,hostname,subnet,securitygroup):
    """
    This function creates the new ENI
    """
    try:
        global NetworkInterfaceId
        NetworkInterfaceId = client.create_network_interface(
            Description= hostname,
            Groups=[securitygroup],
            SubnetId=subnet
            )
        NetworkInterfaceId = NetworkInterfaceId['NetworkInterface']['NetworkInterfaceId']
        print (NetworkInterfaceId)
        logging.info('Created New ENI: ' +NetworkInterfaceId)
        return NetworkInterfaceId
    except ClientError as e:
        print(e)
        logging.error(e)


def attach_eni(client,instanceid,eni_id,hostname):
    """
    This function attaches the newly created  ENI or attaches the Existing ENI to the correct server by matching hostanme to the ENI description
    It also checks for 3 scenarios
        - if the ENI is already attached to the server 
        - if the ENI is wrongly attached to the server 
        - if the correct ENI is already attached to the corresponding server
    """
    try:
        response = client.attach_network_interface(
            NetworkInterfaceId= eni_id, 
            InstanceId=instanceid,
            DeviceIndex=1
            )
        attachmenid = response['AttachmentId']
        print(attachmenid)
        logging.info('Attached ENI {e} to Instance {i}. The ENI Attachment ID is {a}'. format(i=instanceid,e=eni_id,a=attachmenid))
        
    except ClientError as e:
        logging.error(e)

        if e.response['Error']['Code'] =='InvalidParameterValue':
            match_eni = client.describe_network_interfaces(Filters=[{
                'Name': 'attachment.instance-id','Values': [instanceid]},
                {'Name': 'attachment.device-index','Values': ['1']}])
            match_eni_id = match_eni['NetworkInterfaces'][0]['NetworkInterfaceId']
            match_eni_description = match_eni['NetworkInterfaces'][0]['Description']

            if eni_id == match_eni_id:
                logging.error(('ENI :{m} is already attached to the instance {i}').format(m = match_eni_id, i = instanceid))
            else:
                if hostname != match_eni_description:
                    logging.error(('ENI is wrongly attached. ENI of host-{h}, ENI id: {e} is attached to current insatnce{i}').format(h = match_eni_description, i = instanceid, e = match_eni_id))
                else:
                    logging.error(str(e))
        else:
            logging.error(str(e))

            



def main():
    hostname        = args.hostname
    subnet          = args.subnet
    securitygroup   = args.security
    instanceid      = args.instance
    log_file        = args.logfile
    region          = args.region
    client          = get_client(region)

    logging.basicConfig(
        filename = log_file,
        format = '%(asctime)s %(message)s',
        level = logging.INFO,
        datefmt = '%d-%b-%y %H:%M:%S'
    )

    all_network_interfaces = client.describe_network_interfaces(Filters=[{'Name': 'description','Values': [hostname]}])
    
    if len(all_network_interfaces['NetworkInterfaces']) == 0:
        eni_id = create_eni(client,hostname,subnet,securitygroup)
        attach_eni(client,instanceid,eni_id,hostname)

    elif len(all_network_interfaces['NetworkInterfaces']) == 1:
        eni_id = all_network_interfaces['NetworkInterfaces'][0]['NetworkInterfaceId']
        attach_eni(client,instanceid,eni_id,hostname)
        logging.info('ENI Exists: '+eni_id)
    else:
        multiple_eni = [all_network_interfaces['NetworkInterfaces']]
        for int in multiple_eni:
            logging.error('Multiple ENIs to the same instance({ins}): {i} '.format(ins = instanceid, i = int)) 


if __name__ == "__main__":
    args = parse_args()
    main()



    
