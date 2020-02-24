from google.cloud import storage, bigquery 

def list_blobs(bucket_name, prefix):
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix)

    for blob in blobs: 
        print("BLOB Name is {}".format(blob))
    

list_blobs('cvr_testing','spark')