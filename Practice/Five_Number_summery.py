#IstikJaved
#11180120186
#8A

dataset = []
print("Please Input your Data: ", end="")
dataset = list(map(int, input().split()))
dataset.sort()
length_dataset = len(dataset)

print("Data Is: ",end="")
for i in range(0,length_dataset):
    print(dataset[i],end=" ")
print()

def quartile_median(dataset):
    length = len(dataset)
    start = (length)//2
    if length%2:
        start = start
        end = start + 1
        median = sum(dataset[start:end])
    else:
        start = start - 1
        end = start + 2
        median = sum(dataset[start:end]) / 2.


    #Calculate Quatrile 1
    q1start = start//2
    flag = False
    if start%2:
        q1start = q1start
        q1end = q1start + 1
        q1 = sum(dataset[q1start:q1end])
    else:
        flag = True
        q1start = q1start - 1
        q1end = q1start + 2
        q1 = sum(dataset[q1start:q1end]) / 2.
    #Calculate Quartile 3
    q3start = end + q1start
    q3end = end + q1end
    if flag:
        q3 = sum(dataset[q3start:q3end]) / 2.
    else:
        q3 = sum(dataset[q3start:q3end])
    return q1, median, q3

print("----------5 Number Summery-----------")

print("Min Value: ",dataset[0])
print("Max Value: ",dataset[-1])
print("Q1:Median:Q3: ",quartile_median(dataset))




