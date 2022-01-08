# wehelp week-2

# 要求一
print("----- Python 要求一 -----")

def calculate(min, max):
    # print(min,max)
    sum=0
    for a in range(min,max+1):
        sum += a
    print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30

print("------------------------\n")

#要求二
print("----- Python 要求二 -----")

def avg(data):
    # print(data["count"])
    sumSalary = 0
    avgSalary = 0
    for b in range(data["count"]):
        # print(data["employees"][b]["salary"])
        sumSalary += data["employees"][b]["salary"]
    avgSalary = sumSalary / data["count"]
    # print(sumSalary)
    print(avgSalary)
    print(round(avgSalary*100)/100)

# Tuple() -> 字典{} -> List[] -> 字典{}
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

print("------------------------\n")

# #要求三
print("----- Python 要求三 -----")

def maxProduct(nums):
    # print(list(enumerate(nums)))
    indexNums = list(enumerate(nums))
    # print(indexNums)
    newNums = []

    #檢查函式執行
    # print(nums[0])

    #list長度
    # print(len(nums)) 
    
    #list中第幾筆資料
    # for idx in range(len(nums)):
    #     print(index)

    #list中資料內容
    # for c in nums:
    #     # print("第一層 " + str(c)) # 字串數字不可直接相加
    #     print("第一層" , c)
    #     for d in nums:
    #         print("第二層" , d)

    for index, item in indexNums:
        # print("第一層",index, item)
        for index2, item2 in indexNums:
            # print(index2, item2)
            if(index == index2):
                # print("不計算")
                continue
            else:
                multi = item * item2
                # print(multi)
                newNums.append(multi)
    # print(newNums)

    #篩選陣列裡重複資料 
    finalNums =filter(newNums)
    for e in finalNums:
        # print(e)    #相乘後不重複之資料
        print(max(e)) #取最大值


#篩選列表裡重複資料 
def filter(array):
    filterList = set(array)
    # filter_set = set(array)
    # filter_list = list(filter_set)
    yield filterList
            

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

print("------------------------\n")

# #要求四
print("----- Python 要求四 -----")

def twoSum(nums, target):
    # print(nums,target)
    indexNums = list(enumerate(nums))
    # print(indexNums)
    add = 0
    final = []

    for index, item in indexNums:
        # print("第一層",index, item)
        for index2, item2 in indexNums:
            # print(index2, item2)
            if(index == index2):
                # print("不計算")
                continue
            else:
                add = item + item2
                # print(add)
                if(add == target):
                    # print(item, item2)
                    final.append(index)
                    # final.append(index2)
                else:
                    # print("??")
                    continue

    # print(final)

    return final

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
# print(twoSum([11, 11, 7, 15], 22))

print("------------------------\n")
