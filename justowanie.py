
# coding: utf-8

# In[213]:

# tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae vestibulum nunc. Mauris aliquam tempor sapien, ut dictum quam condimentum nec. Ut eu leo a enim fringilla tempor at eu enim. Praesent at nisi et neque dictum rhoncus. Maecenas aliquam ante orci, et mollis massa efficitur sit amet. Nam ut nisi pellentesque risus sagittis molestie. Ut ut nisi ac est placerat scelerisque sit amet in libero. Aenean nibh turpis, egestas eget orci non, mattis dignissim libero."
# DEKOMPOZYCJA
class tekst:
    """Justowanie"""
    
    
    def __init__(self, tekst, w):
        """Konstruktor"""
        self._T = tekst
        self._tT = tekst.split()
        self._w = w
        self._dtT = map(len, self._tT)
        self._lwyr = len(self._tT)
        #for i in self._dtT:
            #assert i <= w, ("Wyraz jest za dlugi")
        assert False in map(lambda a: a>w, self._dtT), ("Wyraz jest za dlugi")
        
    def _zachlanny(self):
        """Justowanie - algorytm zachlanny"""
        parent = []
        buf, idx = 0, 0
        while idx < self._lwyr:
            buf += self._dtT[idx]
            if buf > self._w:
                parent.append(idx)
                buf = self._dtT[idx]
            else:
                buf += 1 #spacja
            idx += 1
        return parent
    
    def _justowanie(self):
        """Justowanie"""
        return self._zachlanny()
    
    def justuj(self):
        """Justowanie - dla uzytkownika"""
        temp = ""
        start = 0
        for i in self._justowanie():
            temp += " ".join(self._tT[start:i]) + "\n"
            start = i
        return temp + " ".join(self._tT[start:])
            


# In[ ]:




# In[214]:

t1 = tekst("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae vestibulum nunc. Mauris aliquam tempor sapien, ut dictum", 8)


# In[215]:

t1._zachlanny()


# In[216]:

print t1.justuj()


# In[ ]:




# In[ ]:



