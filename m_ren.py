import os
from datetime import date

# putanja, umjesto klasičnih windows "\" ide backslash "/"
src_dir = "D:/testing"
tdate = date.today().strftime('%d-%m-%Y')
lst = os.listdir(src_dir)


def rename(src_dir):
    n = 0
    for filename in lst:
        dst = src_dir + "/novo-ime-" + str(tdate) +"-0"+ str(n) + ".txt"
        src = src_dir + "/" + filename
        os.rename(src, dst)
        n += 1
        print(src)


if __name__ == '__main__':
    rename(src_dir)

