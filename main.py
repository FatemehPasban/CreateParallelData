import pandas as pd
from hazm import*
import clean_sent
import json
import clean_underline
import submitt
import skipp

print('سرعتییییی کار کن :)')
root = 'C:/Users/Fatemeh/PycharmProjects/pythonProject1/my_files/'
raw_data_path = 'df_hamshahri.xlsx'
vam_vaj_path = 'all words_words.xlsx'
parallel_corpus_path = 'parallel_corpus.xlsx'
normalizer = Normalizer()

vam_vajes = pd.read_excel(root+vam_vaj_path)
raw_data = pd.read_excel(root+raw_data_path)
parallel_corpus = pd.read_excel(root+parallel_corpus_path)
parallel_corpus = parallel_corpus.loc[:,['sen'	,'tr_sen','kind']]
with open(root+'my_dict.json', 'r',encoding='utf-8') as f :
  my_dict = json.load(f)
  f.close()
#print(parallel_corpus[:10])
counter = my_dict['counter']
raw_data_counter = my_dict['raw_data_counter']
print('counter is => ',counter)

# ----------------------------- for mistakes ---------------------
# my_dict['raw_data_counter'] = raw_data_counter+1
# with open(root + 'my_dict.json', 'w', encoding='utf8') as f:
#   json.dump(my_dict, f)
#   f.close()
# print('ok')
# print(my_dict['raw_data_counter'],my_dict['counter'])
#ssssss
#--------------------------------------------------------

#normalized_sent = normalizer.normalize(raw_data.loc[counter,'sent'])
normalized_sent = raw_data.loc[raw_data_counter,'sent']
print(normalized_sent)
check = input('is this sentence ok?  yes:1  no:0')

if int(check) == 1:
  word_list = word_tokenize(normalized_sent)
  word_list1 = clean_underline.clean_underline(word_list)
  #N_list = [2,1]
  N_list = [3,2,1]
  #N_list = [4,3,2,1]
  #N_list = [5,4,3,2,1]
  word_list2 = clean_sent.clean_sent(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,vam_vajes,word_list1,N_list)
  submitt.submitt(parallel_corpus_path,parallel_corpus,root,word_list2,normalized_sent,my_dict,counter)
elif int(check) == 0:
  skipp.skipp(root,raw_data,counter,my_dict)
