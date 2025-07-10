from src.excel.downloader import load_static_excel
from src.sql.updater import load_sql_data
from src.dynamic.mover import load_dynamic_excels
from src.utils.helpers import log_message
import pandas as pd
import os

def main():
    log_message("Starting the data update process.")

    # 1. Load static Excel
    static_path = "./data/static.xlsx"
   #  static_path = "C:/Users/omakieieva/Documents/static.xlsx"  # <-- update this path
    if not os.path.exists(static_path):
        log_message(f"Static Excel file not found: {static_path}")
        return
    static_df = load_static_excel(static_path)
    log_message("Loaded static Excel.")

    # 2. Query SQL Server
    connection_string = os.environ.get('multidrive_connection_string')
    log_message(f"Loaded connection string: {connection_string}")
  
    sql_query = "SELECT * FROM your_table"  # <-- update this query
    sql_df = load_sql_data(connection_string, sql_query)
    log_message("Loaded SQL data.")

    # 3. Load dynamic Excel files
    dynamic_folder = "C:/Users/omakieieva/Documents/excels"  # <-- update this path
    if not os.path.exists(dynamic_folder):
        log_message(f"Dynamic Excel folder not found: {dynamic_folder}")
        return
    dynamic_df = load_dynamic_excels(dynamic_folder)
    log_message("Loaded dynamic Excel files.")

    # 4. Load Storm EDMI data
    Storm_EDMI_url = load_storm_edmi()  # Ensure this function is defined in the correct module

    # 4. Combine data (customize as needed)
    combined_df = pd.concat([static_df, sql_df, dynamic_df], ignore_index=True)
    log_message("Combined all data.")

    # 5. Save the report
    output_path = "C:/Users/omakieieva/Documents/combined_report.xlsx"
    combined_df.to_excel(output_path, index=False)
    log_message(f"Report saved as {output_path}")

if __name__ == "__main__":
    main()