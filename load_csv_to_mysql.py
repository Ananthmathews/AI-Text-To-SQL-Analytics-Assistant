import os
import pandas as pd
from sqlalchemy import create_engine

# Define the path to the folder containing the CSV files
csv_folder = r"c:\users\lucky\downloads\archive"

# Define the MySQL connection
engine = create_engine('mysql+pymysql://sqlagent:Agent123@localhost:3306/ecommerce_ai')

# Loop through each CSV file in the folder
for filename in os.listdir(csv_folder):
    if filename.endswith('.csv'):
        # Read the CSV file into a DataFrame
        file_path = os.path.join(csv_folder, filename)
        # Use the filename (without .csv) as the table name
        table_name = filename.replace('.csv', '')  

        print(f"importing{filename}")

        # read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # upload the DataFrame to MySQL
        df.to_sql(name=table_name,
                   con=engine,
                     if_exists='replace', index = False) 
        print(f"finished {table_name}")
print("All files have been imported successfully.")        

        


