def get_num_words(texts)->int:
  words=texts.split()
  word_count=0
  for _ in words:
    word_count+=1
  print(f'Found {word_count} total words')


def get_letter_num(texts)->int:
  words=texts.lower().split()
  letter_counts={}
  for word in words:
    for letter in word:
      if letter in letter_counts:
        letter_counts[letter]+=1
      else:
        letter_counts[letter]=1
  return letter_counts


def sort_on(items):
  return items['num']
  