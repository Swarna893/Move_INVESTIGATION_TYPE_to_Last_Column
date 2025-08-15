# Moving the Investigation_Type column to the extreme right


import pandas as pd
import numpy as np

def move_column_to_end(df, column_name):
  """
  Moves a specified column to the extreme right of the DataFrame.

  Args:
    df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to move.

  Returns:
    pd.DataFrame: The DataFrame with the specified column moved to the end.
  """
  # Check if the column exists in the DataFrame
  if column_name not in df.columns:
    print(f"Error: Column '{column_name}' not found in DataFrame.")
    return df
  
  # Pop the column from its original position
  column_to_move = df.pop(column_name)
  
  # Assign the column to the end of the DataFrame
  df[column_name] = column_to_move
  
  return df

def delete_empty_rows_and_move_column(input_csv_path, output_csv_path, column_name):
  """
  Deletes rows with empty values in a specified column, then moves that
  column to the extreme right and saves the result to a new CSV file.

  Args:
    input_csv_path (str): The path to the original CSV file.
    output_csv_path (str): The path to save the new, cleaned CSV file.
    column_name (str): The name of the column to check for empty values and move.
  """
  try:
    # Read the CSV file
    df = pd.read_csv(input_csv_path)

    # Convert all values in the column to strings and strip whitespace
    df[column_name] = df[column_name].astype(str).str.strip()
    
    # Replace empty strings with NaN
    df[column_name] = df[column_name].replace('', np.nan)

    print(f"Original number of rows: {len(df)}")
    
    # Drop rows with NaN in the specified column
    df_cleaned = df.dropna(subset=[column_name])
    
    print(f"Number of rows after cleaning: {len(df_cleaned)}")
    
    # Move the specified column to the extreme right
    df_final = move_column_to_end(df_cleaned.copy(), column_name)
    
    # Display the new column order to confirm the change
    print("\nNew column order:")
    print(df_final.columns)
    
    # Save the final DataFrame to a new CSV file
    df_final.to_csv(output_csv_path, index=False)
    print(f"\nCleaned and reordered data saved to '{output_csv_path}'")

  except FileNotFoundError:
    print(f"Error: The file '{input_csv_path}' was not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

# Example Usage:
input_file = 'D:/Final_Year_Project/Data_preparation/cleaned_sales_data.csv'
output_file = 'D:/Final_Year_Project/Data_preparation/cleaned_and_reordered_airline_accidents.csv'
column_to_check_and_move = 'Investigation_Type'

delete_empty_rows_and_move_column(input_file, output_file, column_to_check_and_move)
