import pandas as pd
import glob
import os

# Specify the directory containing your CSV files
csv_dir = 'path/to/dir'  # Use a raw string
# List all CSV files in the directory
csv_files = glob.glob(os.path.join(csv_dir, '*.csv'))

# Define the column names explicitly
column_names = ['Col1', 'Col2', 'Col3', 'Col4']

# Initialize an empty DataFrame with the column names
merged_df = pd.DataFrame(columns=column_names)

# Loop through the list of files
for file in csv_files:
    # Read the CSV file without the header as we have already set the column names
    temp_df = pd.read_csv(file, header=0)  # header=0 reads the first line as header, then aligns and drops it
    
    # Append the DataFrame to the merged DataFrame
    merged_df = pd.concat([merged_df, temp_df], ignore_index=True)

# Save the merged DataFrame to a new CSV file, including the header
output_file = os.path.join(csv_dir, 'merged_file.csv')
merged_df.to_csv(output_file, index=False)
