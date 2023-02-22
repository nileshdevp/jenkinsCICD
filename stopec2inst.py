import boto3
import sys

region = 'ap-northeast-1'
accesskey = 'AKIASPARKNSUQU5OEYII'
secretkey = '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'

response = client.stop_instances(
    InstanceIds=[
        'i-06c09421fb364174c',
    ],
)

print(response)
