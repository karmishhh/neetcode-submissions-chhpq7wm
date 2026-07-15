class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left < right:
            summ = people[left] + people[right]
            if summ > limit:
                right -= 1
                boats += 1
            elif summ <= limit:
                left += 1
                right -= 1
                boats += 1
        if left == right:
            right = len(people)-1
            if people[left] <= limit: # or right both works since left == right lolll 
                boats += 1
            
        return boats
                

        