from google.cloud import storage 

def download_gcs_file(bucket_name, from_file, to_file):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(from_file)
    
    blob.download_to_filename(to_file)

    print("Downloaded Object {}".format(from_file))


download_gcs_file('cvr_testing','check_python_env.py','check_python_env.py')