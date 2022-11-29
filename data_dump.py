import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
# we have to give data base name and collection name
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


if __name__== "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"number of rows and columns {df.shape}")
    # convert data frame csv to json because mongodb we save the data in json
    df.reset_index(drop = True, inplace = True) # inplace mean over return on same location
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #dumping in mango DB
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    

