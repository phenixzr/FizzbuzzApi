from FizzbuzzApi import app

class FizzBuzzLC():
    def isValidData(self, fzQuery):
        errStr = None
        res = False

        if fzQuery.int1 != None and fzQuery.int1 > 0 \
            and fzQuery.int2 != None and fzQuery.int2 > 0 and fzQuery.int2 != fzQuery.int1 \
            and fzQuery.mlimit != None and fzQuery.mlimit > 0 and fzQuery.mlimit > fzQuery.int1 and fzQuery.mlimit > fzQuery.int2 \
            and fzQuery.str1 != None and len(fzQuery.str1) > 0 \
            and fzQuery.str2 != None and len(fzQuery.str2) > 0:
            res = True
        elif fzQuery.int1 == None:
            errStr = "int1 must be set"
        elif fzQuery.int2 == None:
            errStr = "int2 must be set"
        elif fzQuery.mlimit == None:
            errStr = "mlimit must be set"
        elif fzQuery.int1 < 0: 
            errStr = "int1 must be greather than zero"
        elif fzQuery.int2 < 0 : 
            errStr = "int2 must be greather than zero"
        elif fzQuery.int2 == fzQuery.int1:
            errStr = "int1 and int2 must not be equal"
        elif fzQuery.mlimit < 0: 
            errStr = "limit must be greather than zero"
        elif fzQuery.mlimit < fzQuery.int1 or fzQuery.mlimit < fzQuery.int2:
            errStr = "limit must be greather than int1 and int2"
        elif fzQuery.str1 == None or len(fzQuery.str1) == 0:
            errStr = "str1 must be a valid string"
        elif fzQuery.str2 == None or len(fzQuery.str2) == 0:
            errStr = "str2 must be a valid string"
        else :
            errStr = "bad request, can't validate your query"    
        return res, errStr

    def processFizzbuzz(self, fzQuery):
        res = []
        step = 1
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

    def compute(self, fzQuery):
        isValid, errStr = self.isValidData(fzQuery)
        if isValid:
            return True, self.processFizzbuzz(fzQuery), errStr
        else :
            return False, None, errStr

