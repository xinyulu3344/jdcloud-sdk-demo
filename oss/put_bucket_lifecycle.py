import boto3

ACCESS_KEY = ''
SECRET_KEY = ''
s3 = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    # 下面给出一个endpoint_url的例子
    endpoint_url='https://s3.cn-north-1.jdcloud-oss.com'
)


if __name__ == "__main__":
    response = s3.put_bucket_lifecycle_configuration(
        Bucket='BUCKET',
        LifecycleConfiguration={
            'Rules': [
                {
                    'ID': 'glacier',
                    'Status': 'Enabled',
                    'Filter': {
                        'Prefix': ''
                    },
                    'Transitions': [{
                        'Days': 1,
                        'StorageClass': 'GLACIER'
                    }],
                },
            ]
        },
    )
    print(response)
