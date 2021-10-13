import pandas as pd
import json

def skipp(root,raw_data,counter,my_dict):
  #raw_data = raw_data.drop([counter], axis=0)
  raw_data_counter = my_dict['raw_data_counter']
  my_dict['raw_data_counter'] = raw_data_counter+1
  with open(root+'my_dict.json', 'w',encoding='utf8') as f :
    json.dump(my_dict, f)
    f.close()
  #writer = pd.ExcelWriter(root+raw_data_path)
  #raw_data.to_excel(writer)
  #writer.save()
