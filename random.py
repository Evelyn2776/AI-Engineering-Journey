import time

class CustomRandom:
    def __init__(self):
        self.seed = int(time.time() * 1000)

    def _next_int(self, max_val):
        """Generates a pseudo-random index."""
        self.seed = (1103515245 * self.seed + 12345) % (2**31)
        return self.seed % max_val

    def pick_one(self, input_list):
        """Shuffles the list, converts to a tuple, and returns 1 item."""
        # 1. Protect original data by copying the list
        working_list = list(input_list)
        n = len(working_list)
        
        # 2. Shuffle using Fisher-Yates
        for i in range(n - 1, 0, -1):
            j = self._next_int(i + 1)
            working_list[i], working_list[j] = working_list[j], working_list[i]
            
        # 3. Convert to a tuple
        randomized_tuple = tuple(working_list)
        
        # 4. Return only the very first value from the randomized tuple
        return randomized_tuple[0]

# --- How to use it ---
my_rand = CustomRandom()
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Pick and print just one single value
single_choice = my_rand.pick_one(fruits)
print(single_choice)  # Output: e.g., "cherry"

