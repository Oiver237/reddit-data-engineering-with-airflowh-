from utils.constants import *
import s3fs
def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key= AWS_ACCESS_KEY_ID,
                               secret = AWS_SECRET_ACCESS_KEY)
        return s3
    except Exception as e:
        print(e)
        
def create_bucket_if_not_exist(s3, bucket):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print('Bucket created successfully.')
        else:
            print('Bucket already exists.')
    except Exception as e:
        print(e)

def upload_to_s3(s3, file_path, bucket, s3_file_name):
    try:
        s3.put(file_path, bucket+'/raw/'+s3_file_name)
        print('File uploaded to s3.')
    except FileNotFoundError:
        print('The file was not found.')