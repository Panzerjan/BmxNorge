import pandas as pd 
from common.keyvault import secrets
from common.server import sql
import json


# Connect to sql server
connect = sql.Database()
json_file_path = "C:/repo/BmxNorge/files/race.json"

query = "select ArrangementId from Arrangement WHERE [Dato] > '2024-01-01'"

with open(json_file_path, 'r') as file:
    json_data = json.load(file)

    # Define custom column names (if renaming is needed)
column_names = {
    "ArrangementId": "ArrangementId",
    "Dato": "Dato",
    "Klubbid": "Klubbid",
    "LopId": "LopId",
    "SK": "SK",
    "SK_ASS": "SK_ASS",
    "Jury": "Jury",
    "Jury_2": "Jury_2"
}

# Create DataFrame from JSON data
df = pd.DataFrame(json_data)
# Rename columns according to specified names (if needed)
df = df.rename(columns=column_names)
df['Dato'] = pd.to_datetime(df['Dato'])
print(df)

# Find Race id from sql serverd
df2 =connect.ExecuteQuery(query)
print(df2)
df3 = pd.DataFrame(df2, columns=['ArrangementId'])
# Convert 'Column_Name' from object to integer
df3['ArrangementId'] = pd.to_numeric(df['ArrangementId'])

# Merge DataFrames on 'ArrangementId' column
merged_df = df.merge(df3, on='ArrangementId', how='left', indicator=True)

# Identify rows in df but not in df3 based on 'ArrangementId'
final = merged_df[merged_df['_merge'] == 'left_only'].drop('_merge', axis=1)
print(final)
#Insert into table 
connect.InsertDf(final, "Arrangement")