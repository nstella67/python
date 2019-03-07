#/section08/03-numpy3.py
#배열 연산
import numpy
grade=numpy.array([82, 76, 91, 65])
print(grade)        #[82 76 91 65]

#모든 원소에 대하여 2씩 더함
new1=grade+2
print(new1)        #[84 78 93 67]

#모든 원소에 대하여 5씩 뺌
new2=grade-5
print(new2)       #[77 71 86 60]

#배열 원소끼리 연산
#인덱스가 동일한 원소끼리 수행
arr1=numpy.array([10, 15, 20, 25, 30])
arr2=numpy.array([2, 3, 4, 5, 6])

arr3=arr1+arr2
print(arr3)         #[12 18 24 30 36]

arr4=arr1-arr2
print(arr4)         #[ 8 12 16 20 24]

#----------------------------------------------------------------------------------------------------
sample=numpy.array([82, 77, 95, 60])
print("총점:%d"%numpy.sum(sample))           #총점:314
print("평균:%d"%numpy.average(sample))      #평균:78
print("최댓값:%d"%numpy.max(sample))        #최댓값:95
print("최솟값:%d"%numpy.min(sample))        #최솟값:60


