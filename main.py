from collections import Counter
while True:
    text_ = input('Введіть текст ')
    type_ = input('Введіть тип виведення(a,b,c) ')
    if type_ == 'a':
        textlist = text_.split()
        i = 1
        length = len(textlist);
        for i in range(0, length):
            for j in range(0, length + i):
                try:
                    if len(textlist[j]) > len(textlist[j+1]):
                        one = textlist[j]
                        textlist[j] = textlist[j + 1]
                        textlist[j + 1] = one
                    elif textlist[j] == textlist[j+1]:
                        textlist.remove(textlist[j+1])
                except:
                    continue
        textlist.reverse()
        for i in range(0,5):
            print(textlist[i])

    elif type_ == 'b':
        textlist = text_.split()
        i = 1
        length = len(textlist);
        for i in range(0, length):
            for j in range(0, length + i):
                try:
                    if textlist[j] == textlist[j+1]:
                        textlist.remove(textlist[j+1])
                    if len(textlist[j]) < 3:
                        textlist.remove(textlist[j])
                except:
                    continue
        textlist_sorted = sorted(textlist)
        for i in range(0,len(textlist_sorted)):
            print(textlist_sorted[i])
    elif type_ == 'c':
        textlist = text_.split()
        i = 1
        length = len(textlist);
        for i in range(0, length):
            for j in range(0, length + i):
                try:
                    if len(textlist[j]) > len(textlist[j+1]):
                        one = textlist[j]
                        textlist[j] = textlist[j + 1]
                        textlist[j + 1] = one
                    if len(textlist[j]) < 3:
                        textlist.remove(textlist[j])
                except:
                    continue
        textlist_sorted_by_count = Counter (textlist)

        for i in range(0, len(textlist)):
            for j in range(0, length + i):
                if textlist[j] == textlist[j + 1]:
                    print(textlist[i], " appears  ",textlist_sorted_by_count[textlist[i]], " times")
                else:
                    continue