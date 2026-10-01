def isIsomorphic(s, t):
        seen = {}
        seen2 = {}

        for a, b in zip(s, t):
            if a in seen and seen[a] != b:
                return False

            if b in seen2 and seen2[b] != a:
                return False

            seen[a] = b
            seen2[b] = a

        return True
