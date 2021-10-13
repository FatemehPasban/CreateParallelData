import new_sent
import insert_input_to_wordlist
import difflib

def with_difflib(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,vam_vajes, a, word_list, k, N):
    find_it = 0
    w_list = {}
    for v in range(len(vam_vajes)):
        b = vam_vajes.loc[v, 'word'].strip()
        if difflib.SequenceMatcher(None, a, b).ratio() * 100 >= 76:
            w_list[v] = b

    l = 1
    m_syns = []
    m_syns.append(a)
    if len(w_list) != 0 & 1:
        new_sen = new_sent.new_sent(word_list)
        print(new_sen)
        print(f'{0} : {a}')
        find_it = 1

    for ke, val in w_list.items():
        syns = [s.strip() for s in list(vam_vajes.loc[ke].values) if type(s) is str]
        m_syns.extend(syns[1:])
        print(f'{a} => {syns[0]} (با شباهت)')

        for i in range(l, l + len(syns[1:])):
            print(f'{i} : {m_syns[i]}')
            l += 1

    if len(w_list) != 0 & 1:
        print('\n')
        # print('اگر نیاز به ترجمه ندارد شماره خود واژه را وارد کن')
        print('اگر نیاز به تایپ داری ستاره را وارد کن')
        print('اگه میخوای کل جمله رو دوباره وارد کنی دوتا ستاره بزن')
        syn_index = input('خواهشمندم شماره هم ارز مناسب را بنویس')
        word_list, find_it = insert_input_to_wordlist.insert_input_to_wordlist(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,word_list, syn_index, m_syns, a, N)

    return word_list, find_it
