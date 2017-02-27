import boto3
import requests

class API():
    def __init__():
		# Get the service client.
		self.s3 = boto3.client('s3')

	def getItemFromBucket(bucket, key):
		# Generate the URL to get 'key-name' from 'bucket-name'
		url = self.s3.generate_presigned_url(
		    ClientMethod='get_object',
		    Params={
		        'Bucket': 'bucket-name',
		        'Key': 'key-name'
		    }
		)

		# Use the URL to perform the GET operation. You can use any method you like
		# to send the GET, but we will use requests here to keep things simple.
		return requests.get(url)

	def postItemToBucket(bucket, item)
		# Generate the POST attributes
		post = s3.generate_presigned_post(
		    Bucket='bucket-name',
		    Key='key-name'
		)

		# Use the returned values to POST an object. Note that you need to use ALL
		# of the returned fields in your post. You can use any method you like to
		# send the POST, but we will use requests here to keep things simple.
		files = {"file": "file_content"}
		response = requests.post(post["url"], data=post["fields"], files=files)
		