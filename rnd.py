"""if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        arg = s[1:]
        if cmd !="print":
            eval("l.{} {}".format(cmd, tuple(map(int, arg))))
        else:
            print(l)
"""
"""
if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    a = hash(tuple(integer_list))
    print(a)
"""


"""def swap_case(s):
    l = []
    for i in s:
        if i.islower() == True:
            l.append(i.upper())
        else:
            l.append(i.lower())
    return "".join(l)

if __name__ == '__main__':
    s = list(map(str, "HackerRank.com presents 'Pythonist 2'."))
    result = swap_case(s)
    print(result)"""


"""# Enter your code here. Read input from STDIN. Print output to STDOUT
t = ["Hacker", "Rank"]
n = int(len(t))

for i in range(int(len(t))):
    print(t[i][::2], t[i][1::2])"""


"""#Replace all ______ with rjust, ljust or center.

thickness = 5 #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))"""


# TODO: Practice / Python / Strings / Text Wrap

# import textwrap

# HackerRank STDIN parameters test case 0
# string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# max_width = 4

"""
def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))
"""
"""
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
"""
# END OF Practice / Python / Strings / Text Wrap


"""string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

print(string[::2], string[1::2])
"""
s = "0123456789ABCDEF"
for i in s[:8]:
    for j in s:
        hex_char = bytearray.fromhex(f"{i}{j}").decode()
        print(f"{hex_char} = {i}{j}")
