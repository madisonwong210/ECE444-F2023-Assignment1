class Utils:
    def reversed(self, num):
        if type(num) is not int:
            return "Input must be an int"
        output = ""
        temp = num
        while temp > 0:
            output += str(temp % 10)
            temp = temp // 10
        return int(output)

    def formatter(self, num):
        if type(num) is not int:
            return "Input must be an int"
        # convert to binary
        temp_bin = num
        binary = ""
        while temp_bin > 0:
            binary += str(temp_bin % 2)
            temp_bin = temp_bin // 2

        # convert to octal
        temp_oct = num
        octal = ""
        while temp_oct > 0:
            octal += str(temp_oct % 8)
            temp_oct = temp_oct // 8
        
        return ("Binary: {} Octal: {}".format(int(binary[::-1]), int(octal[::-1])))
        