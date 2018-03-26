class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 

        out = []

        count = 0 
        cur_char = chars[0]

        for i,v in enumerate(chars):
            if v == cur_char:
                count+=1 
            else:
                out+= [str(cur_char),]
                if count>1:
                    out+=list(str(count))
                cur_char = v  
                count = 1
        out += [str(cur_char),]
        if count>1:
            out+=list(str(count))
        res = len(out)
        chars[:res] = out
        return res
