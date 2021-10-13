import new_sent
import insert_input_to_wordlist

def with_equality(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,vam_vajes, a, word_list, k, N):
    global s
    find_it = 0
    Syns = []
    a = a.strip()
    for v in range(len(vam_vajes)):
        b = vam_vajes.loc[v, 'word'].strip()

        if a == b:
            s = [s.strip() for s in list(vam_vajes.loc[v].values) if type(s) is str]
            Syns = Syns + s[1:]

    if len(Syns) > 0:
        new_sen = new_sent.new_sent(word_list)
        print(new_sen)
        Syns = [s[0]] + Syns
        l = 0
        print(f'{a} => {s[0]} (با تساوی)')
        for syn in Syns:
            print(f'{l}: {syn}')
            l += 1

        print('\n')
        print('اگر نیاز به تایپ داری ستاره را وارد کن')
        print('اگه میخوای کل جمله رو دوباره وارد کنی دوتا ستاره بزن')
        syn_index = input('خواهشمندم شماره هم ارز مناسب را بنویس')
        word_list, find_it = insert_input_to_wordlist.insert_input_to_wordlist(root,counter,parallel_corpus_path,parallel_corpus,normalized_sent,my_dict,word_list, syn_index, Syns, a, N)
        # find_it = 1
        # break # که اگر دقیقا پیدا کرد دیگه به بقیه لیست وام واژه ها کار نداشته باشه

    return word_list, find_it