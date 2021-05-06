import pandas as pd
import random
import sys

def sorting_numbers_algorithm(num_list):
  new_list = []
  for q in range(len(num_list)):
    for i in num_list:
      n = i 
      for x in num_list:
        if n > x:
           pass

        else:
          n = x

      new_list.append(n)
    
      num_list.remove(n)
    
    return new_list


dat_path = "C:\\Users\\Tadeas\\Downloads\\generatingpoetry\\Gutenberg-Poetry.csv"

everything = pd.read_csv(dat_path)

num_of_words = 20

n = 2

specialek = 1

text = ""


for i in range(600):
  text += everything["s"][i].lower()
  text += " "


bad_chars = [';', "'", ':', '"','(', ')', ",", ".", "!", "?"]

for i in text:
  if i in bad_chars:
    text = text.replace(i, " ")

words = text.split(" ")

sequences = []
y = []

for x in range(len(words)-n):
  sequences.append(words[x:x+n])
  y.append(words[x+n])


new_sequence = []

for t in sequences:
  if t not in new_sequence:
    new_sequence.append(t)

new_y = []


for a in y:
  if a not in new_y:
    new_y.append(a)

supa_y = []

for i in range(len(new_sequence)):
  supa_y.append([])
  

for h, i in enumerate(new_sequence):
  for j, q in enumerate(sequences):
    if i == q:
      supa_y[h].append(j)

suupe_y = []

for w in range(len(supa_y)):
  apednut = {}
  unique_words = []
  for t in supa_y[w]:
    t = y[t]
    if t not in unique_words:
      unique_words.append(t)
  
  freq = []
  for m in range(len(unique_words)):
    freq.append(0)

  for q, h in enumerate(unique_words):
    for u in supa_y[w]:
      u = y[u]
      if h == u:
        freq[q] += 1

      else:
        pass

  for b in range(len(unique_words)):
    apednut[unique_words[b]] = freq[b]

  suupe_y.append(apednut)

for h in range(len(suupe_y)):
  val = []
  for x, m in suupe_y[h].items():
    n = m/sum(suupe_y[h].values())
    val.append(n)

  for c, x in enumerate(suupe_y[h].keys()):
    suupe_y[h][x] = val[c]

promena = True

while promena:
  input_text = random.randint(0, len(new_sequence))
  input_texto = new_sequence[input_text]
  fintext = ""
  how_words = int(input("How many sequnces of words you want ot generate?: "))
  for i in range(how_words+1):
    sup_text = input_texto[0]
    fintext += sup_text
    fintext += " "
    ind = new_sequence.index(input_texto)
    skoro_predict = suupe_y[ind]
    
    pred_word = ""
    
    if specialek == 0:
      lolik_list = []
      for rata in list(skoro_predict.values()):
        lolik_list.append(rata)

      sorted_probs = sorting_numbers_algorithm(list(skoro_predict.values()))[0]

      supa_ind = lolik_list.index(sorted_probs)
      
      worde = list(skoro_predict.keys())[supa_ind]

      pred_word += worde
    
    elif specialek == 1:
      if len(skoro_predict) > 3:
        lolik_list = []
        for rata in list(skoro_predict.values()):
          lolik_list.append(rata)

        sorted_probs = sorting_numbers_algorithm(list(skoro_predict.values()))[0:3]

        jop = random.randint(0, 2)
        
        fin_prob = sorted_probs[jop]

        supa_ind = lolik_list.index(fin_prob)

        worde = list(skoro_predict.keys())[supa_ind]

        pred_word += worde

      else:
        jop = random.randint(0, len(skoro_predict)-1)

        worde = list(skoro_predict.keys())[jop]

        pred_word += worde

    elif specialek == 2:
      jop = random.randint(0, len(skoro_predict)-1)

      worde = list(skoro_predict.keys())[jop]

      pred_word += worde

    else:
      sys.exit("LoL")
      


    input_texto.append(pred_word)
    input_texto = input_texto[1:]



  print(fintext)

    

    



  




  
  



  
  



  




  

  
  


  

  
        
        

    

    
        



  
  





#def textgenerationwithmarkovchain(num_of_words = 20, n=3): 
  








