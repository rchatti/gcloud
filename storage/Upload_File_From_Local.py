from google.cloud import storage, bigquery 

def upload_file(bucket_name, from_file, to_file):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    ## blob = bucket.blob("home/rchatti/" + to_file)
    blob = bucket.blob(to_file)

    blob.upload_from_filename(from_file)
    print("File, {}, uploaded to bucket {}".format(from_file, bucket_name))

upload_file('cvr_testing','test_file.txt','test_file.txt')
