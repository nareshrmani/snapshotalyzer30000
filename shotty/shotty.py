import boto3
import click
#new library called click which is used to create user friendly CLI commands.
session = boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')

#Create an option to take tag and project of EC2.

@click.option('--project', default=None,
    help="Only instances of project (tag Project:<Name>)")

#Create a new function called list_instances
def list_instances(project):
    "List EC2 instances"
    instances=[]

#Create an if loop to create a filter condition on the tag and project of EC2.
    if project:
        filters= [{'Name':'tag:Project','Values':[project]}]
        instances=ec2.instances.filter(Filters=filters)
    else:
        instances=ec2.instances.all()

    for i in instances:
        tags= {t['Key']:t['Value'] for t in i.tags or []}
        print(','.join ((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.private_dns_name,
            tags.get('Project', '<no project>')
            )))
    return

@instances.command('stop')
@click.option('--project',default=None,
    help='only instances for project')

#Create a new function called stop_instances
def stop_instances(project):
    "Stop EC2 instances"
    instances=[]
#Create an if loop to create a filter condition on the tag and project of EC2.
    if project:
        filters= [{'Name':'tag:Project','Values':[project]}]
        instances=ec2.instances.filter(Filters=filters)
    else:
        instances=ec2.instances.all()

#Create a for loop for stopping instances
    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    return

@instances.command('start')
@click.option('--project',default=None,
    help='only instances for project')

#Create a new function called start_instances
def start_instances(project):
    "Start EC2 instances"
    instances=[]
#Create an if loop to create a filter condition on the tag and project of EC2.
    if project:
        filters= [{'Name':'tag:Project','Values':[project]}]
        instances=ec2.instances.filter(Filters=filters)
    else:
        instances=ec2.instances.all()

#Create a for loop for starting instances
    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()
    return
    
#Main Block calls the function list_instances above.
if __name__ == '__main__':
    instances()
