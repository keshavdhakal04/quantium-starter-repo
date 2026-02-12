import pandas as pd
import glob

# 1. Collect all transaction source files from data folder
# Using a specific variable name instead of just 'files'
source_files = glob.glob('data/*.csv') 

if not source_files:
    print("No CSV files found! Check your file path.")
else:
    processed_data_list = []
    
    for file_path in source_files:
        # Load the raw data from the current file
        transaction_data = pd.read_csv(file_path)
        
        # 2. Filter for Pink Morsels only
        # Target only the specific product requested by Soul Foods
        pink_morsel_data = transaction_data[transaction_data['product'].str.lower() == 'pink morsel'].copy()
        
        # 3. Calculate Sales
        # Clean the price string (remove '$') and convert to decimal (float)
        if pink_morsel_data['price'].dtype == 'object':
            pink_morsel_data['price'] = pink_morsel_data['price'].str.replace('$', '', regex=False).astype(float)
        
        # Create a new 'sales' field by multiplying volume by unit price
        pink_morsel_data['sales'] = pink_morsel_data['quantity'] * pink_morsel_data['price']
        
        # 4. Extract only the required fields: Sales, Date, and Region
        formatted_data = pink_morsel_data[['sales', 'date', 'region']]
        
        processed_data_list.append(formatted_data)

    # 5. Consolidate all processed data into a single table
    combined_pink_morsel_data = pd.concat(processed_data_list, ignore_index=True)
    
    # Save the final result to the output file
    output_file_path = 'data/formatted_output.csv'
    combined_pink_morsel_data.to_csv(output_file_path, index=False)

    print(f"Data processing complete. Created '{output_file_path}'.")