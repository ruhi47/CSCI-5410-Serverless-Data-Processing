from google.cloud import storage
from Levenshtein import distance
import csv
import re


def generateVector(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    print(file)
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(event['bucket'])
    blob = bucket.blob(event['name'])
    contents = blob.download_as_text()
    print(contents)

    results = []
    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
                 "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
                 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs',
                 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is',
                 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
                 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
                 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
                 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
                 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
                 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
                 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
                 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn',
                 "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
                 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn',
                 "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    for word in contents.split():
        if word.lower() not in stopwords and word[0].isupper():
            w = re.sub("[)\".,']", "", word)
            results.append(w)
    print(blob)
    if int(event['name'].split(".")[0]) < 300:
        name = 'trainVector.csv'
        bucket_name = 'traindatab00872269'
    else:
        name = 'testVector.csv'
        bucket_name = 'testdatab00872269'

    bucket = storage_client.bucket(bucket_name)
    stats = storage.Blob(bucket=bucket, name=name).exists(storage_client)
    print(stats)
    if not stats:
        with open('/tmp/' + name, 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Current_Word', 'Next_Word', 'Levenshtein_distance'])

            for i in range(len(results) - 1):
                spamwriter.writerow([results[i], results[i + 1], distance(results[i], results[i + 1])])
    else:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(name)
        print(blob)
        dest_file = '/tmp/' + name
        blob.download_to_filename(dest_file)

        with open(dest_file, 'a') as f_object:
            writer_object = csv.writer(f_object, delimiter=',',
                                       quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(results) - 1):
                writer_object.writerow([results[i], results[i + 1], distance(results[i], results[i + 1])])

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(name)
    blob.upload_from_filename('/tmp/' + name)

