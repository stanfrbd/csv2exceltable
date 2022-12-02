import pandas as pd
import xlsxwriter
import argparse
import os

def action_csv(txt):
    try:
        #read the csv into a pandas dataframe
        data = pd.read_csv(txt)
        basename = os.path.basename(txt)
        output_name = basename.split('.')[0] + '.xlsx'    
        #setup the writer
        writer = pd.ExcelWriter(output_name, engine='xlsxwriter')
        #write the dataframe to an xlsx file
        data.to_excel(writer, sheet_name='sheet1', index=False)

        workbook = writer.book
        worksheet = writer.sheets['sheet1']

        (max_row, max_col) = data.shape

        # Create a list of column headers, to use in add_table().
        column_settings = []
        for header in data.columns:
            column_settings.append({'header': header})

        # Add the table.
        worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings, 'style': 'Table Style Light 1'})

        # Make the columns wider for clarity.
        worksheet.set_column(0, max_col - 1, 12)

        # automatically saves the file
        writer.close()
        print("Generated " + output_name)
    except:
        print("Fatal error: corrupted file.")

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('-i','--input-file', help='Choose the path to input file containing URLs e.g. "test.csv" -- it will export to xlsx in the current directory')
    
    global args
    args = parser.parse_args()

    if args.input_file:
        action_csv(args.input_file)

if __name__ == "__main__":
    try: 
        main() 
    except Exception as err: 
        print("General error: ", err) 
        exit(1)