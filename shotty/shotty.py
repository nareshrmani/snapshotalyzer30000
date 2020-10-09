import boto3
import click
#new library called click which is used to create user friendly CLI commands.
session = boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

@click.command()
#Create a new function called list_instances
def list_instances():
    "List EC2 instances"
    for i in ec2.instances.all():
        print(','.join ((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.private_dns_name)))

    return
#Main Block calls the function list_instances above.
if __name__ == '__main__':
    list_instances()
