def printChanges(s1, s2, dp):
    i = len(s1)
    j = len(s2)
    list = []
    # Check till the end
    while (i > 0 and j > 0):

        # If characters are same
        if s1[i - 1] == s2[j - 1]:
            list.append(s1[i - 1] + " " + s2[j - 1] + " " + str(0))
            i -= 1
            j -= 1

        # Replace
        elif dp[i][j] == dp[i - 1][j - 1] + 1:
            list.append(s1[i - 1] +" " +s2[j - 1] +" " + str(1))
            j -= 1
            i -= 1

        # Delete
        elif dp[i][j] == dp[i - 1][j] + 1:
            list.append(s1[i - 1]+" _ "+ str(1))
            i -= 1

        # Add
        elif dp[i][j] == dp[i][j - 1] + 1:
            list.append("_"+" " + s2[j - 1]+" " + str(1))
            j -= 1

    while(i > 0):
        list.append(s1[i - 1]+" _ "+str(1))
        i -= 1

    while(j > 0):
        list.append("_ "+s2[j - 1]+" " + str(1))
        j -= 1
    for i in range(len(list) - 1, -1, -1):
        print(list[i])

# Function to compute the DP matrix
def editDistOptimalAlign(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0 for i in range(len2 + 1)]
          for j in range(len1 + 1)]

    # Initilize by the maximum edits possible
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

        # Compute the DP Matrix
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):

            # If the characters are same
            # no changes required
            if s2[j - 1] == s1[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

                # Minimum of three operations possible
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],
                                   dp[i - 1][j - 1],
                                   dp[i - 1][j])

                # Print the steps
    printChanges(s1, s2, dp)


# Driver Code
s1 = "style"
s2 = "types"

# Compute the DP Matrix
editDistOptimalAlign(s1, s2)
