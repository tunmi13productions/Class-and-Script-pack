#13Downloader, version 1.0
#Based off of 13Updater 2.0
#Copyright 2023 tunmi13 productions
#This code is open sourced, and may be modified or redistributed in any format.
"""
This uses a progress bar using a module called tqdm.
pip install tqdm
It then takes the percentage of the file size given by requests, loops through with data, then gets the percentage using the data out of the file size.
The progress is monitored by two variables.
current_progress: This acts as a sort of delay between readouts. If we were to display progress continuously, the user would be spammed. This is useful for big files as to separate readouts.
progress: This is the actual progress so far. If it is greater than the current progress variable by 5, it will adjust the variable current_progress, then speak it with accessible_output2. It will continue doing this until it reaches 100 percent.
"""
#Required modjules.
from accessible_output2 import outputs
output = outputs.auto.Auto()
import requests
from tqdm import tqdm
def dl(url_path,filename):
 response = requests.get(url_path, stream=True)
 file_size = int(response.headers.get('Content-Length', 0))
 block_size = 1024
 progress_bar = tqdm(total=file_size, unit='iB', unit_scale=True)
 current_progress = 0
 with open(filename, 'wb') as f:
  for data in response.iter_content(block_size):
   progress_bar.update(len(data))
   progress = round((float(progress_bar.n)/file_size)*100,0)
   if progress >= current_progress + 5:
    current_progress = progress
    output.output(f"{int(current_progress)} percent.")
   f.write(data)
 progress_bar.close()