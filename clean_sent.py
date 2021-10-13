import new_sent
import with_equality
import string
import with_difflib

def clean_sent(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,vam_vajes,word_list, N_list):
    for N in N_list:
        word_list_N = []
        for j in range(len(word_list) - (N - 1)):
            ng = new_sent.new_sent(word_list[j:j + N])
            if len(['yes' for i in ng if i in string.punctuation + '،' + '؛']) == 0:
                word_list_N.append(ng)
        k = 0
        print('searching for : ',N,'_Gram')
        while k < len(word_list_N):

            # for k in range(len(word_list_N)):
            a = word_list_N[k]
            # print('2')
            word_list, find_it = with_equality.with_equality(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,vam_vajes, a, word_list, k, N)
            # word_list,find_it = with_difflib(vam_vajes,a ,word_list,k,N,normalized_sent)
            # print('with_equality')
            if find_it != 1:
                word_list, find_it = with_difflib.with_difflib(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,vam_vajes, a, word_list, k, N)
            if find_it == 1:
                k += N - 1
            k += 1
    return word_list