#!/usr/bin/env python
import argparse
import sys
import logging
import boto3
from botocore.exceptions import ClientError


def get_client(resource, region):
    return boto3.client(resource, region_name=region)


def parse_args():
    parser = argparse.ArgumentParser(description="EC2 ENI attachment")
    parser.add_argument("-n", "--nodename", help="nodename", required=True)
    parser.add_argument("-g", "--secgroup", help="security group id", required=True)
    parser.add_argument("-s", "--subnet", help="subnet id", required=True)
    parser.add_argument("-i", "--instance", help="instance id", required=True)
    parser.add_argument("-r", "--region", help="region", default="ap-northeast-1")
    parser.add_argument("-l", "--logfile", help="location of log file", default="/opt/strongswan-support/eni.log")
    args = parser.parse_args()
    return args


def create_new_eni(client, hostname, subnet_id, securityGroup):
    """
    Create new ENI in AWS
    :param client: boto3 ec2 client
    :param hostname: descriptive name of host for which ENI is intended
    :param subnet_id: ID of subnet in which ENI is placed
    :param securityGroup: ID of security group attached to ENI
    :return: ID of new ENI (string)
    """
    try:

        network_interface = client.create_network_interface(SubnetId=subnet_id, Groups=[securityGroup])
        network_interface_id = network_interface['NetworkInterface']['NetworkInterfaceId']
        client.modify_network_interface_attribute(
            NetworkInterfaceId=network_interface_id,
            Description={'Value': hostname},
        )
        logging.info("ENI created with ID {}".format(network_interface_id))

    except Exception as e:

        logging.error(str(e))
        sys.exit(1)

    return network_interface_id


def attach_eni(client, instance_id, eni_id, hostname):
    """
    Attach ENI to EC2 instance in AWS
    :param client: boto3 ec2 client
    :param instance_id: instance ID to attach ENI
    :param eni_id: ENI ID of network interface
    :param hostname: Hostname of the Instance
    """
    try:

        client.attach_network_interface(
            DeviceIndex=1,
            InstanceId=instance_id,
            NetworkInterfaceId=eni_id
        )
        logging.info("Attached the ENI: {0} to instance: {1}".format(eni_id, hostname))

    except ClientError as e:

        if e.response['Error']['Code'] == "InvalidParameterValue":
            network_interface = client.describe_network_interfaces(
                Filters=[{
                    'Name': 'attachment.instance-id',
                    'Values': [instance_id]
                    },
                    {
                    'Name': 'attachment.device-index',
                    'Values': ['1']
                    }
                ]
            )
            if eni_id == network_interface['NetworkInterfaces'][0]['NetworkInterfaceId']:
                logging.info("ENI already attached to the instance - No action taken")
                sys.exit(0)

            else:
                if hostname != network_interface['NetworkInterfaces'][0]['Description']:
                    logging.error("ERROR: Unexpected ENI attached to Instance: found id {0} description {1}, expected "
                                  "{2}".format(str(network_interface['NetworkInterfaces'][0]['NetworkInterfaceId']),
                                               str(network_interface['NetworkInterfaces'][0]['Description']),
                                               hostname))
                    sys.exit(1)
                else:
                    logging.error(str(e))
                    sys.exit(1)

        else:
            logging.error(str(e))
            sys.exit(1)


def main():
    hostname = args.nodename
    log_file = args.logfile
    region = args.region

    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%m-%d-%y %H:%M:%S')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    client = get_client('ec2', region)
    all_network_interfaces = client.describe_network_interfaces(
        Filters=[{
            'Name': 'description',
            'Values': [hostname]
        }
        ]
    )
    if len(all_network_interfaces['NetworkInterfaces']) == 0:
        logging.info("Creating new ENI")
        new_eni = create_new_eni(client, args.nodename, args.subnet, args.secgroup)
        logging.info("Attaching new ENI")
        attach_eni(client, args.instance, new_eni, hostname)

    elif len(all_network_interfaces['NetworkInterfaces']) == 1:
        logging.info("ENI already Created, attaching existing ENI")
        attach_eni(client, args.instance, all_network_interfaces['NetworkInterfaces'][0]['NetworkInterfaceId'],
                   hostname)

    else:
        logging.error("ERROR: Multiple ENIs Found")
        for eni in all_network_interfaces['NetworkInterfaces']:
            logging.error("ENI ID: {0} ENI found with description {1}".format(eni['NetworkInterfaceId'],
                                                                             eni['Description']))
        sys.exit(1)


if __name__ == "__main__":
    args = parse_args()
    main()