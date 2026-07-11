class Solution:
    def climbStairs(self, n: int) -> int:
        # climbStairs(1) = 1, climbStairs(2) = 2 
        # climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
        def dp(n, cache):
            # Base Cases: 
            if n <= 2:
                return n    
            if n in cache:
                return cache[n]
            # Recursive cases
            cache[n] = dp(n-1,cache) + dp(n-2, cache)
            # Final return 
            return cache[n]
        return dp(n, {})
