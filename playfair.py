import math
from string import ascii_lowercase as ascii_letters


class PlayFairCipher:

    """
        here i am implementing the playfair cipher ,
        i have two choices for the matrix , whether to omit "w"
        or to add two letters in the same row, i will omit "w"
    """

    def __init__(self,keyword):

        self.keyword=""
        for letter in keyword:
            if letter != "w" and letter.isalpha():
                self.keyword+=letter 

        self.matrix = self.create_playfair_matrix()
   
    def generate_matrix(self):

        return [[i for i in range(5)] for j in range(5)]
    
    def encrypt(self,plaintext):
        letters = ""
        for letter in plaintext:
            if letter.isalpha():
                letters += letter

        pairs = self.generate_pairs(letters)
        result = []
        for pair in pairs:
            if self.check_same_line(pair) and self.check_same_line(pair)[0]:
                result.append(self.check_same_line(pair)[1])
            elif self.check_same_column(pair) and self.check_same_column(pair)[0]:
                result.append(self.check_same_column(pair)[1])
            else:
                result.append(self.position_square(pair))

        return ' '.join(''.join(i).upper() for i in result)


    def list_intersection(self,string):

        return "".join([i for i in ascii_letters if not i in string])
    
    def generate_pairs(self,input_string):
        
        """
            here we generate pairs of twos,
            and if they are identical we replace the last with x
        """
        if len(input_string) %2 !=0:
            input_string+="x"
  
        pairs = []
      
        for i in range(0, len(input_string) - 1, 2):
            generated = input_string[i:i+2]
            if generated.count(generated[0]) > 1:
                generated = list(generated)
                generated[1]="x"
                generated = "".join(generated)
            pairs.append(generated)
        
        return pairs
    
    def check_same_line(self,pair):
        
        for i in range(5):
            if pair[0] in self.matrix[i] and pair[1] in self.matrix[i]:
                
                index_1 = self.matrix[i].index(pair[0])
                index_2 = self.matrix[i].index(pair[1])
                
                #here it means , both letters are in the same line , we return next letter
                return True,[self.matrix[i][(index_1+1)%5],self.matrix[i][(index_2+1)%5]]
        
        return False
    
    def check_same_column(self,pair="xx"):

        position_1 = ""
        position_2 = ""

        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == pair[0]:
                    position_1 = [i,j]
                if self.matrix[i][j] == pair[1]:
                    position_2 = [i,j]
     
        try:

            if position_1[1] == position_2[1]:
                #means they are in the same column
                return True,[self.matrix[(position_1[0]+1)%5][position_1[1]],self.matrix[(position_2[0]+1)%5][position_2[1]]]
        except Exception as e:

            return False,[]
        
        
        
    
    def position_square(self,pair):

        position_1 = []
        position_2 = []

        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == pair[0]:
                    position_1 = [i,j]
                if self.matrix[i][j] == pair[1]:
                    position_2 = [i,j]
        
        try:
      
            distance = int(math.fabs(position_2[1] - (position_1[1]+1))) #get the distance between the two positions
        
        except Exception as e:
            print(f"Error: {e},  positions:{position_1} , position:{position_2}")
            return []

      
        letter_1 = self.matrix[position_1[0]][(position_1[1]+distance)%5]
        letter_2 = self.matrix[position_2[0]][(position_2[1]+distance)%5]

        return [letter_1,letter_2]


    def create_playfair_matrix(self):

        matrix = self.generate_matrix()
        counter = 0
        level  = 0
        next = 0
        unique_sting = ""

        while counter < len(self.keyword):
            if self.check_letter(matrix,self.keyword[counter]):
                matrix[level][next] = self.keyword[counter]
                unique_sting+=self.keyword[counter]
                next+=1
                if next == 5:
                    next = 0
                    level+=1
            counter+=1      
        
        remaining_letters = self.list_intersection(unique_sting)

        try:
            remaining_letters = list(remaining_letters)
            remaining_letters.remove("w")
            remaining_letters = "".join(remaining_letters)
            #we try to remove w 
        except Exception as e:
            print(f"an error: {e}")

        counter = 0

        for i in range(5):
            for j in range(5):
                if not str(matrix[i][j]).isalpha() :
                    matrix[i][j] = remaining_letters[counter]
                    counter+=1

        self.display_matrix(matrix)
        return matrix
                
        

    def check_letter(self,matrix,letter):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == letter:
                    return False
        return True

    def display_matrix(self,matrix):

        rows_number = len(matrix)
        cols_number = len(matrix[0])

        for i in range(rows_number):
            for j in range(cols_number):
                print(matrix[i][j],end=" ")
            print()

    
if __name__ == "__main__":

    menu = """
        ****************************************************************
        --steps for encryption
        1-choose 1 to encrypt a message
        2-provide a key (alphanumeric)
        3-enter the message to encrypt
        4-enter anything different from 1 to stop
        ****************************************************************

    """
    print(menu)

    while True:
        choice = int(input("enter your choice: "))
        if choice != 1:
            break

        secret = input("enter your secret key: ")
        instance = PlayFairCipher(secret)
        plaintext = input("enter your plaintext: ")
        cipher_text = instance.encrypt(plaintext)
        print(f"the encrypted message is: {cipher_text}")
