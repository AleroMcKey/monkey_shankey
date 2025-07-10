

from io import BytesIO
import pandas as pd
import requests

def load_storm_edmi():
# Request Storm Failed/Late Meters report
    r = requests.get('https://api.storm.edmicloud.com/reporting/datadelivery/failuresnapshot', headers=header)
# Create BytesIO Object
    byte_io = BytesIO(r.content)
# Read BytesIO object like csv into dataframe
    return pd.read_csv(byte_io)

