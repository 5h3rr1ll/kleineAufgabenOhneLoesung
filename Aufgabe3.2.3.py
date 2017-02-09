Worte = "Anna und otto haben ein Pferd als Reittier".split()

def Palindrome(lst):
    for wort in Worte:
        wort = wort.lower()
        wortRe = wort[::-1]
        if wort == wortRe:
            return True

print(Palindrome(Worte))
