def is_isogram(string):
    smalls = list("abcdefghijklmnopqrsetvwxyz")
    ans = True
    for small in smalls:
        if string.lower().count(small) > 1:
            ans = False
    return ans
