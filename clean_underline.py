def clean_underline(s):
  ss = []
  for i in range(len(s)) :
    if '_' in s[i]:
      l = s[i].split('_')
      ss.extend(l)
    else:
      ss.append(s[i])
  return ss