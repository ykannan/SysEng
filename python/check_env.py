

import argparse
import dns.resolver
import socket
import requests
import csv
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# import logging
# import azure
# from azure.common.credentials import ServicePrincipalCredentials
# from azure.mgmt.authorization import AuthorizationManagementClient
# from azure.common.client_factory import get_client_from_cli_profile
# from azure.common.credentials import get_cli_profile
# from azure.mgmt.resource import SubscriptionClient
# from knack.util import CLIError
# from azure.mgmt.authorization import AuthorizationManagementClient

def parse_args():
    parser = argparse.ArgumentParser(description='These arguments are needed for generating report for active environments')
    parser.add_argument('-lis', '--list', help='Pass list file path', required=True)
    parser.add_argument('-rep', '--report', help='Pass report file name to be created', default='report.csv')
    args = parser.parse_args()
    return args


def report(csvf,lisf):
    fieldnames=['Url','Status','Cloud', 'Message']
    with open(csvf,'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        with open(lisf,'r') as f:
            for site in f:
                try:
                    site = site.rstrip('\n')
                    url1 ="https://{s}.c3-e.com/static/console/".format(s=site)
                    url2 ="{s}.c3-e.com".format(s=site)
                    response = requests.get(url1)
                    status = response.status_code
                    addr1 = socket.gethostbyname_ex(url2)
                    if "aws" in addr1[0]:
                        writer.writerow({"Url":url2, "Status":status, "Cloud":"AWS", "Message":"OK"})
                        print("Url:{u}, Status:{st},Cloud: {c}".format(st=status,u=url2,c="AWS"))
                    else:
                        writer.writerow({"Url":url2, "Status":status, "Cloud":"AZURE", "Message":"OK"})
                        print("Url:{u}, Status:{st},Cloud: {c}".format(st=status,u=url2,c="Azure"))
                
                except Exception as e:
                    message = 'DNSLookupError'
                    print("Url:{u}, {m}".format(u=url2, m=message))
                    writer.writerow({"Url":url2, "Status":"None", "Cloud":"None", "Message": "Does not exist " +message})


def main():
    csvf = args.report
    lisf = args.list

    report(csvf,lisf)

if __name__ == "__main__":
    args = parse_args()
    main()

# def list_subscriptions():    
#     global list1
#     try:
#         list1=[]
#         sub_client = get_client_from_cli_profile(SubscriptionClient)
#         subscription  = sub_client.subscriptions.list()
#         for sub in subscription:
#             list1.append(sub.display_name)
#         return list1

#     except CLIError:
#         logger.info("Not logged in, running az login")
#         _run_az_cli_login()
#         sub_client = get_client_from_cli_profile(SubscriptionClient)


# list_subscriptions()
# test()