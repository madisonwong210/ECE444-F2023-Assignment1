class Utils:
    @staticmethod
    def reversed(num):
        if type(num) is not int:
            return "Input must be an int"
        output = ""
        temp = num
        sign = 1
        if temp < 0:
            sign = -1
            temp = abs(num)
        while temp > 0:
            output += str(temp % 10)
            temp = temp // 10
        new = sign * int(output)
        return new
    
    @staticmethod
    def formatter(num):
        if type(num) is not int:
            return "Input must be an int"
        binary = ""
        octal = ""
        for i in [2, 8]:
            temp = num
            sign = 1
            if temp < 0:
                sign = -1
                temp = abs(num)    
            while temp > 0:
                if i == 2:
                    binary += str(temp % i)
                else:
                    octal += str(temp % i)
                temp = temp // i

        return ("Binary: {} Octal: {}".format(sign * int(binary[::-1]), sign * int(octal[::-1])))
