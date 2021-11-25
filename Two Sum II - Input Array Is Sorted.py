def twoSum(numbers,target):
    l,h = 0,len(numbers) -1
    answer = []
    while l < h :
        if numbers[l] + numbers[h] == target:
            answer.append(l+1)
            answer.append(h+1)
        if numbers[l] + numbers[h] > target :
            h -= 1
        else:
            l += 1
    return answer

a1 =[2, 7, 11, 15]
a2 = 9
#Output: [1, 2]
b1 = [2,3,4]
b2 = 6
#Output: [1,3]
c1 = [-1,0]
c2 = -1
#Output: [1,2]
print(twoSum(a1,a2))
print(twoSum(b1,b2))
print(twoSum(c1,c2))