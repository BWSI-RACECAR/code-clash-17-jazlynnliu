"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #17 - Pascal's Triangle (pascal.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Blaise Pascal is a famous French Mathematician and Philosopher who 
created Pascal's Triangle. Pascal's Triangle is a triangular array composed of 
binomial coefficients that arises in probability theory, combinatorics, and algebra. (Wikipedia)

Prompt: Given the number of rows, return a 2D list of Pascal's Triangle

Test Cases:
Input: rows = 1 ; Output = [[1]]
Input: rows = 2 ; Output = [[1], [1, 1]]
Input: rows = 3 ; Output = [[1], [1, 1], [1, 2, 1]]

"""

class Solution:
    def pascalTri(self,rows):
        # type row: int
        # return type: list[list[int]]

        # TODO: Write code below to return a nested list with the solution to the prompt
        nest_list = []
        for count in range(rows):
            temp = []
            if count == 0:
                temp.append(1)
            else:
                temp.insert(0, 1)
                temp.append(1)
                if count > 1:
                    temp.insert(count + 1, (nest_list[-1][count] + nest_list[-1][count - 1]))
            nest_list.append(temp)
        return nest_list

def main():
    num = int(input())

    tc1 = Solution()
    ans = tc1.pascalTri(num)
    print(ans)

if __name__ == "__main__":
    main()