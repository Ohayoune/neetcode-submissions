class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #has something to do with set
        #create a dictionary of char sets to lists of string, adding to the list each time an anagram is found.
        #at the end, combine all of the strings

        md = dict() #md = 'mydict'

        for s in strs:
            a = "".join(sorted(s))
            if a in md:
                md[a].append(s)
            else:
                md[a] = [s]

        return list(md.values())