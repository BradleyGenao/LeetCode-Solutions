class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        basket = collections.defaultdict(int)
        start = 0
        max_fruits = 0
        for end, fruit in enumerate(fruits):
            basket[fruit] +=1
            
            while len(basket) > 2:
                left_fruit = fruits[start]
                basket[left_fruit] -=1
                if  basket[left_fruit] == 0:
                    del  basket[left_fruit]
                start +=1
            max_fruits = max(max_fruits, end - start + 1)
        return max_fruits
        