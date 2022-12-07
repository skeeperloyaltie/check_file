def recursiveSolution(n): 
    # Base case when n is 0 or 1 
    if n == 0 or n == 1: 
        return 1
    else: 
        # Ways to jump when last step is 1  
        x = recursiveSolution(n-1)  
        # Ways to jump when last step is 2  
        y = recursiveSolution(n-2)  
        # Ways to jump when last step is 3  
        z = recursiveSolution(n-3)  
        return x + y + z 

b. A faster algorithm to help the frog can be found using dynamic programming, as given below:

def dynamicSolution(n): 
    # Create an array to store the results 
    dp = [0] * (n+1) 
  
    # Base case when n is 0 or 1 
    dp[0] = 1
    dp[1] = 1
  
    # Fill the array in bottom up manner 
    for i in range(2, n+1): 
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] 
  
    return dp[n] 
