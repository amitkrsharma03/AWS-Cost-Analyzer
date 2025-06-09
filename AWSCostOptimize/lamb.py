import boto3
import datetime
import json

# AWS clients
ce = boto3.client('ce')  # Cost Explorer
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

# Constants
COST_THRESHOLD = 5.00  # daily USD threshold
S3_BUCKET_NAME = 'your-cost-reports-bucket'
S3_KEY_PREFIX = 'cost-reports/'

def lambda_handler(event, context):
    # Get yesterday's date range
    end = datetime.date.today()
    start = end - datetime.timedelta(days=1)

    # Get cost usage from AWS Cost Explorer
    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    cost = float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])
    
    print(f"Cost for {start}: ${cost}")

    if cost > COST_THRESHOLD:
        # Describe running EC2 instances
        ec2_report = ec2.describe_instances(
            Filters=[
                {'Name': 'instance-state-name', 'Values': ['running']}
            ]
        )

        report_data = {
            'Date': start.strftime('%Y-%m-%d'),
            'Cost': cost,
            'RunningInstances': []
        }

        for reservation in ec2_report['Reservations']:
            for instance in reservation['Instances']:
                report_data['RunningInstances'].append({
                    'InstanceId': instance['InstanceId'],
                    'InstanceType': instance['InstanceType'],
                    'State': instance['State']['Name'],
                    'LaunchTime': instance['LaunchTime'].isoformat()
                })

        # Save report to S3
        report_key = f"{S3_KEY_PREFIX}cost_report_{start}.json"
        s3.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=report_key,
            Body=json.dumps(report_data),
            ContentType='application/json'
        )

        print(f"Report saved to s3://{S3_BUCKET_NAME}/{report_key}")

        # Optionally, send SNS or log event (not included for now)

    return {
        'statusCode': 200,
        'body': f'Checked cost for {start}, result: ${cost}'
    }
