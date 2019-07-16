class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanNum = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        numeral =  [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        final,i ="", len(numeral)-1
        
        if (num < 1) or (num > 3999):
            return 0
        
        while (num > 0):
            if (num - numeral[i] >= 0):
                final += romanNum[i]
                num -= numeral[i]
            else: i -= 1
                
        return final



class Solution:
    def intToRoman(self, num):
        value_roman_map = {
            0: '',
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        
        curr_num = num
        num_place = 0
        output = ""
        while curr_num != 0:
            last_digit = curr_num % 10
            curr_value = last_digit * (10 ** num_place)
            curr_output = ""
            
            if last_digit % 5 == 4:
                if last_digit == 4:
                    _value = 1 * (10 ** num_place)
                    curr_output += value_roman_map[_value]
                    _value = 5 * (10 ** num_place)
                    curr_output += value_roman_map[_value]
                elif last_digit == 9:
                    _value = 1 * (10 ** num_place)
                    curr_output += value_roman_map[_value]
                    _value = 10 * (10 ** num_place)
                    curr_output += value_roman_map[_value]
            else:
                if last_digit >= 5:
                    _value = 5 * (10 ** num_place)
                    curr_output += value_roman_map[_value]
                    curr_value -= _value
                while curr_value != 0:
                    _value = 1 * (10 ** num_place)
                    curr_output += value_roman_map[_value]
                    curr_value -= _value
            
            # update the number 
            output = curr_output + output
            curr_num = curr_num // 10
            num_place += 1
        return output