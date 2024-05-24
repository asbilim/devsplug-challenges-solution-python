
#code by paul_lilian
#https://www.devsplug.com

class Conversion:

    """
        this is a class that can be used to convert a number from 
        one numbering system to another.

        :parameters: number (str)

    """

    def __init__(self,number):

        self.number = number
        self.hexadecimal_dict ={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

    def is_binary_number(self):

        """
            simple funciton to check if a number is in binary
        """

        for i in self.number:

            if int(i) >1:
                return False
        
        return True
    
    def translate(self,from_base=10,to_base=2,precision=6):

        """
            the function convert a number from one base to another
            :from_base : int
                The base of the number to translate.
            :to_base : int
                The base to translate the number to.
            :precision : int
                The number of digits to include in the translation.

        """

        fractional = "." in self.number

        if fractional:

            return self.translate_fractional(from_base,to_base,precision)

        if from_base != 10: 
            self.number=self.to_decimal(from_base) 


        result = ""

        self.number = int(self.number)

        while self.number > 0:

            hexadecimal_dict_values = list(self.hexadecimal_dict.values())
            hexadecimal_dict_keys = list(self.hexadecimal_dict.keys())
            the_rest = self.number % to_base

            if the_rest in hexadecimal_dict_values:
                index = hexadecimal_dict_values.index(the_rest)
                the_rest = hexadecimal_dict_keys[index]

            result = str(the_rest) + result
            self.number //=to_base
     

        self.number = result
        return result
    

    def translate_fractional(self,from_base=10,to_base=2,precision=6):

        """
    This function converts a fractional number from one base to another.

    :param from_base: int
        The base of the number to translate.
    :param to_base: int
        The base to translate the number to.
    :param precision: int
        The number of digits to include in the translation.
    :return: str
    The translated fractional number.
    The function first converts the whole part of the number to the target base using the `translate` method. 
    Then, it converts the fractional part of the number to the target base by multiplying it by the target 
    base repeatedly until the whole part of the number becomes zero. The result is then formatted as a 
    string with the whole and fractional parts separated by a decimal point.

    """
        if from_base != 10: 
            self.to_decimal_fractional(from_base)


        number_to_array = str(self.number).split(".")   
        whole_part = number_to_array[0]
        fractional_part = number_to_array[1]
        self.number = whole_part
        whole_part = self.translate(from_base=from_base,to_base=to_base)
        self.number = str(self.number)
        result = ""
        self.number = int(self.number) if not "." in self.number else float(self.number)
        number_to_float = float("."+fractional_part)



        while precision > 0:
            
            number_to_float = number_to_float * to_base
           
            if str(number_to_float).split(".")[0] == "0" and to_base != 2:
                break

            result += str(number_to_float).split(".")[0]
            number_to_float = float('.'+str(number_to_float).split(".")[1])
            precision-=1


        self.number = f"{whole_part}.{result}"
        return self.number
    
    def to_decimal(self,from_base=2,inverse=False):

        """
        This function converts a number from a given base to decimal.

        :param from_base: int
            The base of the number to translate. Default is 2 (binary).
        :param inverse: bool
            If True, the function will convert the number to its equivalent in the given base.
            If False, the function will convert the number from the given base to decimal.

        :return: int
            The decimal equivalent of the number.

        Raises:
            ValueError: If the input number is not a binary number when `from_base` is 2.

        
        """

        if '.' in self.number:

            return self.to_decimal_fractional(from_base)

        

        if from_base==2 and not self.is_binary_number():
            raise ValueError("please provide a base 2 number for this conversion")
        

        if from_base==16:
    
            number_2_list = list(self.number.upper())
            for index,number in enumerate(number_2_list):
                
                number_2_list[index] = self.hexadecimal_dict.get(number) if self.hexadecimal_dict.get(number) else number

            
        
        string_len = len(number_2_list) if from_base==16 else len(self.number)
        counter = 0
        result=0

        while counter < string_len:

            array_to_use = number_2_list if from_base==16 else self.number
            if inverse:
                result += int(array_to_use[counter]) * from_base**(-(counter+1))
            else:
                result += int(array_to_use[counter]) * from_base**(string_len-counter-1)
            counter+=1

        self.number = result
        return result
    
    def to_decimal_fractional(self,from_base=2):

        """
        This function converts a fractional number from a given base to decimal.

        :param from_base: int
            The base of the number to translate. Default is 2 (binary).

        :return: str
            The decimal equivalent of the fractional number.

        Raises:
            ValueError: If the input number is not a valid fractional number.

        """

        number_to_array = self.number.split('.')

        if len(number_to_array) != 2:
            raise ValueError("this is not a valid fractional number")
        
        fractional_part = number_to_array[1]
        self.number =  number_to_array[0]
        whole_part_to_decimal = self.to_decimal(from_base=from_base)
        self.number = fractional_part
        decimal_part_to_decimal = self.to_decimal(from_base=from_base,inverse=True)

        self.number = whole_part_to_decimal + decimal_part_to_decimal

        return str(self.number) 
        


        

case_1 = Conversion("0.72265625").translate(from_base=10,to_base=2)

print(case_1)