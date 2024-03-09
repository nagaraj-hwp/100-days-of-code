import os
import pandas as pd


# Function to iterate through sub_folders and append sheet 1 of each Excel file to a new file
def append_sheets_from_sub_folders(main_folder):
    # Initialize an empty DataFrame to store the appended data
    appended_data = pd.DataFrame()

    # Iterate through sub_folders
    for folder_name in os.listdir(main_folder):
        folder_path = os.path.join(main_folder, folder_name)
        if os.path.isdir(folder_path):
            # Iterate through Excel files in the sub_folder
            for filename in os.listdir(folder_path):
                if filename.endswith('.xlsx'):
                    file_path = os.path.join(folder_path, filename)
                    # Read the Excel file and append sheet 1 to the DataFrame
                    df = pd.read_excel(file_path, sheet_name=0)
                    appended_data = appended_data.append(df, ignore_index=True)

    # Write the appended data to a new Excel file
    output_file = os.path.join(main_folder, 'appended_data.xlsx')
    appended_data.to_excel(output_file, index=False)
    print("Data appended and saved to", output_file)


# Specify the path to the main folder containing sub_folders with Excel files
main_folder_path = './main_folder'
append_sheets_from_sub_folders(main_folder_path)
