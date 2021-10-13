def new_sent(cleaned_word_list):
  new_text = ''
  for charr in cleaned_word_list:
    charr = charr.strip()
    new_text = new_text + ' ' + charr
  #print(new_text)
  return new_text