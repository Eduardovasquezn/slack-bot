import functions_framework
from google.cloud import storage

def list_files(bucket_name):
    """Lists all files in a GCP bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    
    file_names = [blob.name for blob in blobs]
    return file_names

@functions_framework.http
def list_bucket_files(request):
    """Cloud Function to list all files in 'teams-meetings' bucket."""
    bucket_name = "team-meetings"
    
    try:
        files = list_files(bucket_name)
        return {"files": files}, 200
    except Exception as e:
        return {"error": str(e)}, 500