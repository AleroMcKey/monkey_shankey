import pandas as pd
import os

def load_dynamic_excels(folder_path):
    all_data = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            df = pd.read_excel(os.path.join(folder_path, filename))
            all_data.append(df)
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        return pd.DataFrame()