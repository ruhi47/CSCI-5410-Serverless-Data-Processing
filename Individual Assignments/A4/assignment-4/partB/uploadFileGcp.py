from os import walk

from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client.from_service_account_json(
        'csci-5410-assignment-4-355804-a08ac1d96908.json')
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


if __name__ == '__main__':
    filenames = next(walk('Dataset/Train'), (None, None, []))[2]
    for files in filenames:
        upload_blob('sourcedatab00872269',
                    '/Users/ruhityagi/Documents/Assignments_5410_SDP/Coding/assignment-4/Dataset/Train/'+files,
                    files)

    filenames = next(walk('Dataset/Test'), (None, None, []))[2]
    for files in filenames:
        upload_blob('sourcedatab00872269',
                    '/Users/ruhityagi/Documents/Assignments_5410_SDP/Coding/assignment-4/Dataset/Test/'+files,
                    files)
