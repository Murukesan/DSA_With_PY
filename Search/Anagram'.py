def Anagram_check(s1,s2):
    anagram = True
    if len(s1) != len(s2):
        anagram=False
        return anagram
    else:
        lst1 = sorted(list(s1))
        lst2 = sorted(list(s2))
        for i in range(0, len(lst1), 1):
            if lst1[i] != lst2[i]:
                anagram=False
                return anagram
        return anagram


if __name__=="__main__":
    s1 = "anagram"
    s2 = "nagaram"
    Result=Anagram_check(s1,s2)
    if Result==True:
        print("Two Strings are anagram")
    else:
        print("Not a Anagram")





