import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
import string
from string import ascii_lowercase as abclower
from string import ascii_uppercase as abchigher

class Algorithms:

    def __init__(self):
        self.alist = ["binary_search_iterative", "binary_search_recursive", "linear_search", "quicksort", 
        "bubblesort", "compareArrInt", "findWord", "factorial", "perfectnumber", "primenumbers", "patternsearch",
        "getpatterns", "euclid", "getIndex", "compareArr", "Fibonacci_recursive", "staircase", "myAlg",
        "BinaryToInt", "getDigits", "flipped", "hexToDecimal", "AgCryptoEncript", "AgCryptoDecript"]

    def __str__(self):
        return str(self.alist)


    def binary_search_iterative(self, arr, target):
        low = 0
        high = len(arr) - 1
        time_complexity = 0

        while low <= high:
            # get the average between low and high
            mid = (low + high) // 2 # we use double slash hear to get the rounded version of the middle
            if target == arr[mid]:
                print("Time complexity: " + str(time_complexity))
                return True

            elif target < arr[mid]:
                high = mid - 1

            elif target > arr[mid]:
                low = mid + 1

            time_complexity += 1



        return False

    def binary_search_recursive(self, arr, target, low, high):
        if low > high:
            return False

        else:
            mid = (low + high) // 2
            if target == arr[mid]:
                return mid

            elif target < arr[mid]:
                return self.binary_search_recursive(arr, target, low, mid - 1)
            elif target > arr[mid]:
                return self.binary_search_recursive(arr, target, mid + 1, high)


    def linear_search(self, target, arr):
        time_complexity = 0
        for i in range(len(arr)):
            if arr[i] == target:
                print(time_complexity)
                return i;

            time_complexity += 1
    # This function takes last element as pivot, places 
    # the pivot element at its correct position in sorted 
    # array, and places all smaller (smaller than pivot) 
    # to left of pivot and all greater elements to right 
    # of pivot 
    def partition(self, arr,low,high): 
        i = ( low-1 )         # index of smaller element 
        pivot = arr[high]     # pivot 
    
        for j in range(low , high): 
    
            # If current element is smaller than or 
            # equal to pivot 
            if   arr[j] <= pivot: 
            
                # increment index of smaller element 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
    
    # The main function that implements QuickSort 
    # arr[] --> Array to be sorted, 
    # low  --> Starting index, 
    # high  --> Ending index 
    
    # Function to do Quick sort 
    def quicksort(self, arr,low,high): 
        if low < high: 
    
            # pi is partitioning index, arr[p] is now 
            # at right place 
            pi = self.partition(arr,low,high) 
    
            # Separately sort elements before 
            # partition and after partition 
            self.quicksort(arr, low, pi-1) 
            self.quicksort(arr, pi+1, high)


    def bubblesort(self, arr): 
        tc = 0  
        for i in range(len(arr)):
            for i in range(len(arr)):
                if i != len(arr) - 1:
                    for j in range(i, i+2):
                        if arr[j] < arr[i]:
                            arr[i], arr[j] = arr[j], arr[i]

                        tc+=1

        print("Time complexity: ", str(tc))
        return arr

    def findWord(self, string, word, returnCount=False):
        cs = []
        count = 0
        d = 0
        i = 0

        # O(n)
        for c in string:
            w = ''
            i+=1
            cs.append(c)
            sep = ''
            isThere = False
            if c == ' ':
                w = sep.join(cs[d:i - 1])
                if w == word:
                    isThere = True
                    count += 1

                d = i

            if i == len(string):
                w = sep.join(cs[d:i])
                if w == word:
                    isThere = True
                    count += 1

                d = i

        return isThere, count

    def compareArrInt(self, a, b, num):
        # Used mostly for longer datasets
        self.quicksort(a, 0, len(a) - 1)
        self.quicksort(b, 0, len(b) - 1)
        if self.binary_search_iterative(a, num):
            if self.binary_search_iterative(b, num):
                return True

        return False
    
    def factorial(self, num):
        if num >= 1:
            return num * self.factorial(num - 1)

        else:
            return 1

    
    def primenumbers(self, prime=None, R=None):
        i = 13
        p = False
        if type(prime) == type(None):
            prime = [2,3,5,7,11]

        for j in prime:
            print(j)

        if type(R) == type(None):
            print("Infinite loop Starting")
            while True:
                for j in prime:
                    if i % j == 0:
                        p=False
                        break
                    else:
                        p=True

                if p:
                    print(i)

                i+=1

        else:
            primeNumbers = []
            c = 0
            while c <= R:
                for j in prime:
                    if i % j == 0:
                        p=False
                        break
                    else:
                        p=True

                if p:
                    primeNumbers.append(i)

                i+=1
                c+=1



    def perfectnumber(self, num=None):
        if type(num) != type(None):
            i = 1
            p = 0
            while i < num:
                if num % i == 0:
                    p += i

                i+=1
            
            if p == num:
                return True

    def patternsearch(self, txt, pat):
        l = len(pat)
        i = len(pat)
        patterns = []
        #O(n)
        while i < len(txt):
            if txt[i - l: i] == pat:
                patterns.append(i - l)

            i += 1

        return patterns

    def getpatterns(self, txt, length):
        l = length
        i = length
        patterns = []
        while i < len(txt):
            patterns.append(txt[i - l: i])
            i += 1

        return patterns

    def euclid(self, a, b):
        distance = (b[0] - a[0]) + (b[1] - a[1])
        return sqrt(distance)

    def getIndex(self, arr, num):
        i = 0
        while i < len(arr):
            if arr[i] == num:
                return i
            i+=1

    def absolute(self, x):
        pass
    def getsqaround(self, a):
        arr = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if [i, j] != [0,0]:
                    arr.append([a[0] + i, a[1] + j])
        
        return arr



    def Fibonacci_recursive(self, n, memo):
        if memo[n - 1]!=None:
            return memo[n]

        if n > 2:
            result = self.Fibonacci_recursive(n - 1, memo) + self.Fibonacci_recursive(n - 2, memo)

            try:
                memo[n] = result
            except:
                memo.append(result)
            return result
        elif n <= 2:
            return 1

    def Fibonacci_iterative(self, n, returnArr=False):
        if n <= 2:
            return 1

        else:
            arr = []
            for i in range(0, n + 1):
                if i <= 2:
                    arr.append(1)
                else:
                    arr.append((arr[i - 1]) + (arr[i - 2]))

                    

            if returnArr:
                return arr

            else:
                return arr[n]

    def createArr(self, num, length):
        arr = []
        if num == None:
            for i in range(0, length):
                arr.append(None)

        else:
            for i in range(length + 1):
                arr.append(num)

        return arr


    def myAlg(self, x):
        y = 0
        for i in range(1, x-1):
            y += (x * i) / (x - i)

        y += (x**2) - x

        return y

    def BinaryToInt(self, binary):
        
        try: 
            b = self.getDigits(binary)
        except:
            b = binary

        decimal = 0
        for i in range(len(b)):
            decimal += b[i] * (2 ** (len(b) - i - 1))
        return decimal

    def flipped(self, arr):
        na = []
        for i in range(len(arr)):
            na.append(arr[len(arr) - i - 1])

        return na
    
    def getDigits(self, n):
        digits = []
        while n // 1 > 0:
            d = n % 10
            digits.append(d)
            n //= 10

        return self.flipped(digits)

    def hexToDecimal(self, h):
        '''
        n = {'0':0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9':9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        x = None
        if h[:2] == '0x':
            x = h[2:].upper()
        
        isNegative = False
        if h[0] == '-':
            x = h[1:].upper()
            isNegative = True

        else:
            x = h.upper()

        decimal = 0
        for i in range(len(x)):
            decimal += n.get(x[i]) * (16 ** (len(x) - i - 1))

        if not isNegative:
            return decimal

        else:
            return -decimal'''

        d = int(h, 16) 
        return d

    def AgCryptoEncript(self, txt):
        en = []

        key = {}
        abc = abclower + abchigher + " "
        for i in range(len(abc)):
            key[abc[i]] = (self.Fibonacci_iterative(i + 2) ** 3) * -2
        

        for i in range(len(txt)):
            en.append(hex(key.get(txt[i]) - i))

        return en
    def AgCryptoDecript(self, en):
        key = {}
        abc = abclower + abchigher + " "
        for i in range(len(abc)):
            key[(self.Fibonacci_iterative(i + 2) ** 3) * -2] = abc[i]

        txt = []

        for i in range(len(en)):
            txt.append(key.get(self.hexToDecimal(en[i]) + i))

        sep = ''
        return sep.join(txt)

    def goldenRatio(self):
        ''' this number can be
        n - 1 = 1/n
         n = (a - b) / a

        '''


        r = (1 + np.sqrt(1 + 4)) / 2
        return r

if __name__ == "__main__":
    
    algorithms = Algorithms()

    txt = abclower + abchigher
    '''
    en = algorithms.AgCryptoEncript(txt)
    print(algorithms.AgCryptoDecript(en))'''

    print(algorithms.goldenRatio() - 1, (1/ algorithms.goldenRatio()))