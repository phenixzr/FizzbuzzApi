step = 1
class FizzBuzzLC():
    def compute(fzQuery):
        res = []
        for i in range(1, fzQuery.mlimit + step, step):
            multipleofi1, multipleofi2 = i % fzQuery.int1 == 0, i % fzQuery.int2 == 0
            if multipleofi1 and multipleofi2 :
                res.append(fzQuery.str1 + fzQuery.str2)
            elif multipleofi1 :
                res.append(fzQuery.str1)
            elif multipleofi2 :
                res.append(fzQuery.str2) 
            else:
                 res.append(i)
        return res
