import pandas as pd

# Define the input and output file paths
input_file = 'input_data.csv'
output_file = 'output_data.csv'

def extract_data(file_path):
    """Extract data from a CSV file."""
    return pd.read_csv(file_path)

def transform_data(df):
    """Transform the data."""
    # Example transformation: Filter rows where 'age' is greater than 30
    df = df[df['age'] > 30]
    # Example transformation: Add a new column 'age_group'
    df['age_group'] = df['age'].apply(lambda x: '30-40' if 30 <= x <= 40 else '40+')
    return df

def load_data(df, file_path):
    """Load data to a CSV file."""
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Extract
    data = extract_data(input_file)
    
    # Transform
    transformed_data = transform_data(data)
    
    # Load
    load_data(transformed_data, output_file)

    print("ETL job completed successfully.")
