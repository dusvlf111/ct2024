#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10810                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: dusvlf5950 <boj.kr/u/dusvlf5950>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10810                          #+#        #+#      #+#     #
#    Solved: 2024/12/09 14:33:45 by dusvlf5950    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
basket = [0] * n
for i in range (m):
    a, b, c = map(int, input().split())
    for j in range(a-1, b):
        basket[j] = c
print(' '.join(map(str, basket))) 