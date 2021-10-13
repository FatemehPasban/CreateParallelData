import json
import pandas as pd
def submitt(parallel_corpus_path,parallel_corpus,root,word_list,normalized_sent,my_dict,counter):
  new_text = ''
  for charr in word_list:
    new_text = new_text + ' ' + charr
  print(normalized_sent,'\n' ,new_text)
  submit = input('رد:0    تایید:1    نیاز به برسی بیشتر:2    ویرایش جمله:3 ')

  if int(submit) == 1:
    #my_dict[counter] = [normalized_sent , new_text,'ok']
    #parallel_corpus.at[counter] = my_dict[str(counter)][:2]
    parallel_corpus.at[counter] = [normalized_sent, new_text,'ok']
    writer = pd.ExcelWriter(root+parallel_corpus_path)
    parallel_corpus.to_excel(writer)
    writer.save()

    my_dict['counter'] = counter+1
    raw_data_counter = my_dict['raw_data_counter']
    my_dict['raw_data_counter'] = raw_data_counter + 1
    with open(root + 'my_dict.json', 'w', encoding='utf8') as f:
      json.dump(my_dict, f)
      f.close()

  elif int(submit) == 0 :
    pass

  elif int(submit) == 2 :
    #my_dict[counter] = [normalized_sent ,new_text, 'later']
    parallel_corpus.at[counter] = [normalized_sent, new_text,'later']
    writer = pd.ExcelWriter(root+parallel_corpus_path)
    parallel_corpus.to_excel(writer)
    writer.save()
    my_dict['counter'] = counter+1
    raw_data_counter = my_dict['raw_data_counter']
    my_dict['raw_data_counter'] = raw_data_counter + 1
    with open(root + 'my_dict.json', 'w', encoding='utf8') as f:
      json.dump(my_dict, f)
      f.close()

  elif int(submit) == 3 :
    new_sen = input(' جمله مناسب را تایپ کن')
    #my_dict[counter] = [normalized_sent ,new_sen, 'typed']
    parallel_corpus.at[counter] = [normalized_sent, new_text, 'typed']
    writer = pd.ExcelWriter(root+parallel_corpus_path)
    parallel_corpus.to_excel(writer)
    writer.save()
    my_dict['counter'] = counter+1
    raw_data_counter = my_dict['raw_data_counter']
    my_dict['raw_data_counter'] = raw_data_counter + 1
    with open(root+'my_dict.json', 'w',encoding='utf8') as f :
      json.dump(my_dict, f)
      f.close()
    #raise SystemExit("Stop right there!")

  #print(my_dict)
  with open(root+'my_dict.json', 'w',encoding='utf8') as f :
    json.dump(my_dict, f)
    f.close()