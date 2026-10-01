def isIsomorphic(s, t):
        seen = {}
        res = []

        for char in s:
            if char not in seen:
                seen[char] = (len(seen) + 1) % 1000
            
            res.append(seen[char])

        seen2 = {}
        res2 = []
        
        for char in t:
            if char not in seen2:
                seen2[char] = (len(seen2) + 1) % 1000
            
            res2.append(seen2[char])
        
        return res == res2
