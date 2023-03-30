def solution(n, num_list):

    leftidx, rightidx = 0, len(num_list)-1
    ans = abs(num_list[leftidx] + num_list[rightidx])
    ansleft, ansright = leftidx, rightidx

    while leftidx<rightidx:
        total = num_list[leftidx] + num_list[rightidx]
        if abs(total)<ans:
            ansleft, ansright = leftidx, rightidx
            ans = abs(total)

            if ans==0:
                break

        if total<0:
            leftidx+=1
        else:
            rightidx-=1

    return num_list[ansleft], num_list[ansright]

n = int(input())
num_list = list(map(int, input().split()))
leftvalue, rightvalue = solution(n, num_list)
print(leftvalue, rightvalue)