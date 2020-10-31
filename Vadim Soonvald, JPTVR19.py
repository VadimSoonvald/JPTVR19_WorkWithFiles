import datetime
with open('input.txt', 'r') as f, open('output.txt', 'w') as w :
    tmp = str(datetime.date.today()) + '\n'
    lines = f.readlines()
    print('Товары, с закупочной ценой:', lines)
    for line in lines[0:] :
        tm = line.strip().split()
        for i in range(len(tm) - 1, -1, -1) :
            if tm[i].isdigit() :
                tm[i] = str(1.8 * float(tm[i]))
                break
        tmp += ' '.join(tm) + '\n'
    tmp = tmp.strip()
    w.write(tmp)
    print('Товары, с новыми ценами +80% к цене:', tmp)
    