from aws_cdk import (
    aws_dynamodb as _dynamodb,
    aws_kinesis as _kinesis,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    aws_apigateway as _apigateway,
    core
)


class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_table = _dynamodb.Table(self, id='dynamoTable',table_name='testcdktable',
                                    partition_key=_dynamodb.Attribute(name='lastname',type=_dynamodb.AttributeType.STRING))

        my_stream =_kinesis.Stream(self,id='kinesisstream',stream_name='cdkkinesisstream')

        my_bucket = _s3.Bucket(self,id='s3bucket',bucket_name='cdks3bucket')

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambdacode'), # create this folder outside stack file folder i.e root level
            handler='hello.handler',
        )

        my_api = _apigateway.LambdaRestApi(self,id='lambdaapi',rest_api_name='cdkapi',handler=my_lambda)
        #Add methods
        music = my_api.root.add_resource('music')
        music.add_method('GET') 
        music.add_method("DELETE", _apigateway.HttpIntegration("http://aws.amazon.com"))




