from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        #Create empty array to represent number of people
        np = [0] * num_people
        count = 0
        candieGift = 1

        while candies > 0:

            np[count % num_people] += candieGift

            # Subtract the gifted candies from the count, and increment the next gift amount
            candies -= candieGift
            count += 1
            
            if candies > candieGift:
                candieGift += 1
            else: 
                candieGift = candies

        return np

def main(): 
    sol = Solution()
    candies1 = 7
    candies2 = 10
    candies3 = 9
    people1 = 4
    people2 = 3
    people3 = 4

    print(sol.distributeCandies(candies3, people3))
    #print(sol.distributeCandies(candies2, people2))

if __name__ == "__main__":
    main()