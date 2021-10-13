from hazm import*
import clean_underline
import pandas as pd
import json

def insert_input_to_wordlist(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,word_list,syn_index,m_syns,a,N):
    find_it =1
    if syn_index == '*':
      inp = input(' واژه مناسب را تایپ کن')
      lis = word_tokenize(inp)
      lis = clean_underline.clean_underline(lis)
      a_list = word_tokenize(a)
      a_list = clean_underline.clean_underline(a_list)
      F_ind = word_list.index(a_list[0])
      #E_ind = word_list.index(a_list[-1])
      E_ind= F_ind + len(a_list)-1
      word_list = word_list[:F_ind] + lis + word_list[E_ind+1:]

    elif syn_index == '**':
      new_sen = input(' جمله مناسب را تایپ کن')
      #my_dict[counter] = [normalized_sent ,new_sen, 'typed']
      parallel_corpus.at[counter] = [normalized_sent ,new_sen, 'typed']

      writer = pd.ExcelWriter(root+parallel_corpus_path)
      parallel_corpus.to_excel(writer)
      writer.save()

      my_dict['counter'] = counter+1
      raw_data_counter = my_dict['raw_data_counter']
      my_dict['raw_data_counter'] = raw_data_counter+1
      with open(root+'my_dict.json', 'w',encoding='utf8') as f :
        json.dump(my_dict, f)
        f.close()
      raise SystemExit("Stop right there!")
    else :
      if syn_index == '0':
        find_it=0
      lis_splite = m_syns[int(syn_index)].split()
      lis = word_tokenize(m_syns[int(syn_index)])
      if len(lis)!= len(lis_splite):
        lis= lis_splite
      lis = clean_underline.clean_underline(lis)
      a_list = word_tokenize(a)
      a_list_split = a.split()
      if len(a_list)!= len(a_list_split):
        a_list = a_list_split
      a_list = clean_underline.clean_underline(a_list)
      F_ind = word_list.index(a_list[0])
      if N==1:
        E_ind=F_ind+ len(a_list) -1
        word_list = word_list[:F_ind] + lis + word_list[E_ind+1:]
      else:
        while True:
          if word_list[F_ind+1] == a_list[1]:
            E_ind=F_ind+ len(a_list) -1
            word_list = word_list[:F_ind] + lis + word_list[E_ind+1:]
            print('--------------')
            return word_list,find_it
          else :
            F_ind = word_list.index(a_list[0],F_ind+1)

    print('--------------')
    return word_list,find_it