class Solution(object):
    def __init__(self, letters):
        self.letters = letters

    def hash(self, string):
        h = 7
        for ch in string:
            h = h*37 + self.letters.index(ch)
        return h

    def generateStringAndHashUsingPrefix(self, length, index, prefix):
        probable_string = prefix + "".join([self.letters[index]] + [self.letters[0]]*(length-1))
        new_hash = self.hash(probable_string)
        return probable_string, new_hash

    def findString(self, num, length, i, j, prefix):
        """
        :type nums: List[int]
        :rtype: int
        """

        probable_string = None
        mid = (i +j)/2
        probable_string, new_hash = self.generateStringAndHashUsingPrefix(length, mid, prefix)
        if new_hash == num:
            return probable_string

        if i == j:
            if length > 1:
                if i + 1 < len(self.letters):
                    probable_string1, new_hash1 = self.generateStringAndHashUsingPrefix(length, i+1, prefix)
                    if new_hash1 > num and num > new_hash:
                        probable_string = self.findString(num, length-1, 0, len(self.letters)-1, prefix+probable_string[len(prefix)])
                elif i - 1 >= 0:
                    probable_string2, new_hash2 = self.generateStringAndHashUsingPrefix(length, i-1, prefix)
                    if new_hash2 < num and num > new_hash2:
                        probable_string = self.findString(num, length-1, 0, len(self.letters)-1, prefix+probable_string[len(prefix)])
        elif (j-i) == 1:
            if num > new_hash:
                probable_string1, new_hash = self.generateStringAndHashUsingPrefix(length, mid+1, prefix)
                if num < new_hash:
                    probable_string = self.findString(num, length-1, 0, len(self.letters)-1, prefix+probable_string[len(prefix)])
                else:
                    probable_string = self.findString(num, length, mid+1, j, prefix)
            else:
                if mid - 1 >= 0:
                    probable_string, new_hash = self.generateStringAndHashUsingPrefix(length, mid-1, prefix)
                    if num > new_hash:
                        probable_string = self.findString(num, length-1, 0, len(self.letters)-1, prefix+probable_string[len(prefix)])
                    else:
                        probable_string = self.findString(num, length, i, mid-1, prefix)
                else:
                    probable_string = self.findString(num, length, i, mid, prefix)
        else:
            if num > new_hash:
                probable_string = self.findString(num, length, mid, j, prefix)
            else:
                probable_string = self.findString(num, length, i, mid, prefix)


        return probable_string

def main():
    letters = "acdegilmnoprstuw"
    number = raw_input("Enter the hash: ")
    length = raw_input("Enter the length of string: ")

    string = Solution(letters).findString(int(number), int(length), 0 , len(letters)-1, "")
    
    if Solution(letters).hash(string) == int(number):
        print "rehashed string: ", string
    else:
        print "Not Found" 
    # print Solution(letters).hash("degiloooppppppppppppww") 
    # print Solution(letters).hash("lgggggg") > 680131659347


if __name__ == '__main__':
    main()