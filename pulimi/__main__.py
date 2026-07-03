import pulumi
import pulumi_aws as aws

amzn_linux_2023_ami = aws.ec2.get_ami(most_recent=True,
    owners=["amazon"],
    filters=[{
        "name": "name",
        "values": ["al2023-ami-2023.*-x86_64"],
    }])
flask_instance = aws.ec2.Instance("flask-web-server",
    ami=amzn_linux_2023_ami.id,
    instance_type=aws.ec2.InstanceType.T3_MICRO,
    #subnet_id=example_subnet.id,
    tags={
        "Name": "flask-web-server",
    })

