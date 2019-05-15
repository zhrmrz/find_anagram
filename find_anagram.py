from collections import Counter
class Sol:
    def find_anagram(self,s,t):
        list=[]
        c=Counter(t)
        for i in range(len(s)-len(t)+1):
            if Counter(s[i:i+len(t)])==c:
                list.append(i)
        return list


if __name__ == '__main__':
    p1=Sol()
    print(p1.find_anagram('abccccbca','abc'))
