#profile.py
# python profile_backup.py -log test.log
import boto3 
import argparse
import logging
from botocore.exceptions import ClientError

def parse_args():
    parser = argparse.ArgumentParser(description='These arguments are needed for describing IAM instance profile')
    parser.add_argument('-reg', '--region', help='Pass Region', default = 'us-east-1')
    parser.add_argument('-log', '--logfile', help='Pass logfile name and path', required=True)
    args = parser.parse_args()
    return args

def get_client(region):
    return boto3.client('ec2', region)

def get_associtation_ids(client, instance_ids,region):
    """
    This modeule gets the associations ids
    """
    global association_ids
    try:
        association_ids=[]
        for instance_id in instance_ids:
            associations = client.describe_iam_instance_profile_associations(
                Filters=[{'Name': 'instance-id','Values': [instance_id]}])
            association_ids.append(associations['IamInstanceProfileAssociations'][0]['AssociationId'])
        logging.info('AssociationIds: {aa}'.format(aa=association_ids))
        logging.info(associations)
        return association_ids

    except ClientError as e:
        logging.error(str(e))

def detach_old_profile_ec2(client, association_ids,region):
    """
    This module detatches IAM profile from the ec2 instance using the association-ids
    """
    try:
        for a in association_ids:
            detach = client.disassociate_iam_instance_profile(AssociationId=a)
            logging.info(detach)
    except ClientError as e:
        logging.error(str(e))


def attach_new_profile_ec2(client,new_pro_arn,instance_ids,region):
    """
    This module attaches the newly created IAM profile with the ec2 instance using the association-ids
    """
    try:
        for i in instance_ids:
            response = client.associate_iam_instance_profile(
                IamInstanceProfile={'Arn': new_pro_arn},InstanceId=i)
            ins = response['IamInstanceProfileAssociation']['InstanceId']
            new_association_id = response['IamInstanceProfileAssociation']['AssociationId']
            logging.info(response)
            logging.info("The instance {i} is attached to IAM Profile, New Association-Id:{a}".format(i=ins,a=new_association_id))

    except ClientError as e:
        logging.error(str(e))


def main():
    region      = args.region
    log_file    = args.logfile
    old_pro_arn = raw_input("Enter Old IAM Instance Profile ARN here: ")
    client      = get_client(region)

    logging.basicConfig(
    filename = log_file,
    format = '%(asctime)s %(message)s',
    level = logging.INFO,
    datefmt = '%d-%b-%y %H:%M:%S'
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%m-%d-%y %H:%M:%S')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    global instance_ids
    try:
        instance_ids=[]
        response = client.describe_instances(
            Filters=[{'Name': 'iam-instance-profile.arn','Values': [old_pro_arn]}])
        
        for resp in response['Reservations']:
            for inst in resp['Instances']:
                instance_ids.append(inst['InstanceId'])

        if len(instance_ids) == 0:
            logging.info("No Instances attached to {o}".format(o = old_pro_arn))
        else:
            global answer
            get_associtation_ids(client,instance_ids,region)
            answer = raw_input('Are you sure you want to detach IAM Instance Profile "{p}" from instance "{r}" (yes/no): '.format(p=old_pro_arn,r=instance_ids))
            if answer == "yes":
                detach_old_profile_ec2(client,association_ids,region)
                attach_new_profile_ec2(client,raw_input("Enter the New Instance profile ARN here: "),instance_ids,region)
            else:
                logging.info("Skipping Detach & Attach!")               
        logging.info(response)
        logging.info('Instance Ids: {ii}'.format(ii=instance_ids))
        return instance_ids
        
    except ClientError as e:
        logging.error(e)
 
if __name__ == "__main__":
    args = parse_args()
    main()