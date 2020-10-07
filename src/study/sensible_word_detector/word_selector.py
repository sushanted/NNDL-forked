import re

with open("data/count_1w.txt","r") as inn, open("data/word_var_len.txt","w") as out:
    selected_words = 0
    for i in range(70000):
        word = inn.readline()
        word = re.findall(r'\w+',word)[0]
        if( 4 < len(word) < 12):
            selected_words+= 1
            out.writelines(word+"\n")
            print(word)

print(selected_words)
