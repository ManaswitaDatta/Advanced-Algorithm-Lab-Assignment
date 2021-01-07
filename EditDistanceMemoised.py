def editDistMemoised(str1, str2, n, m, dp):
    # Create a table to store results of subproblems
    if n == 0:
        return m
    if m == 0:
        return n
    if dp[n][m] != -1:
        return dp[n][m]
    #If characters are equal, recurse for remaining character
    if str1[n-1] == str2[m-1]:
        if dp[n-1][m-1] == -1:
            dp[n][m] = editDistMemoised(str1, str2, n-1, m-1, dp)
        else:
            dp[n][m] = dp[n-1][m-1]
        return dp[n][m]
    #if characters are not equal, use any of the 3 operations
    else:
        if dp[n - 1][m] != -1:
            m1 = dp[n-1][m]
        else:
            m1 = editDistMemoised(str1, str2, n-1, m, dp)
        if dp[n][m - 1] != -1:
            m2 = dp[n][m-1]
        else:
            m2 = editDistMemoised(str1, str2, n, m-1, dp)
        if dp[n - 1][m - 1] != -1:
            m3 = dp[n-1][m-1]
        else :
            m3 = editDistMemoised(str1, str2, n-1, m-1, dp)
        dp[n][m] = 1 + min(m1, min(m2, m3))
        return dp[n][m]


# Driver code
'''
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
'''
str1 = "voldemort"
str2 = "dumbledore"

dp = [[-1 for x in range(len(str2) + 1)] for x in range(len(str1) + 1)]
print(editDistMemoised(str1, str2, len(str1), len(str2), dp))