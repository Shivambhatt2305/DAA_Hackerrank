# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# #
# # Complete the 'sockMerchant' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts following parameters:
# #  1. INTEGER n
# #  2. INTEGER_ARRAY ar
# #

# def sockMerchant(n, ar):
#     # Write your code here
#     count=0
#     final_count=0
#     for i in range(len(ar)):
#         for j in range(i+1,len(ar)):
#             if ar[i]==ar[j]:
#                 count+=1 
#                 if(count==2 and count%2==0):
#                     final_count+=1
#         count=0
#     return final_count

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count = 0
    final_count = 0
    used = [False] * n 
    for i in range(len(ar)):
        if not used[i]:
            for j in range(i+1,len(ar)):
                if not used[j] and ar[i]==ar[j]:
                    count+=1
                    used[i]=used[j]=True 
                    final_count+=1
                    break  
            count=0
    return final_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

