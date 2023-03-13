# List (리스트)
numbers = [2,3,4,5,6,7,11]
names = ['jake','성재','KIM']

print(numbers)
print(names)

# Indexing (인덱싱)
print(names[1])
print(names[0] + names[1] + names[2])
print(numbers[1] + numbers[3])

# List Slicing (리스트 슬라이싱)
numbers[0:4] # 인덱스 0부터 3까지 짜른다.
print(numbers[0:4])
print(numbers[:3])
print(numbers[2:5])

# 인덱스 변경하기
print(numbers)
numbers[0] = 7
print(numbers)

# 리스트 길이 재기
# len
print(len(numbers))
lists = []
# 인덱스 추가하기 
# append
lists.append(5)
lists.append(8)
print(lists)
print(len(lists))
# 인덱스 삭제하기
# del
numbers = [2,3,4,5,6,7,11]
del numbers[3] # 인덱스 3번 삭제
print(numbers)
# 특정 위치에 인덱스 삽입하기
numbers.insert(4, 37)
print(numbers)

# 리스트 정렬
numbers = [19, 13, 2, 5, 3, 11, 7, 17]
# 방법1 sorted
# sorted함수는 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트 리턴 
new_list = sorted(numbers)
print(numbers)
print(new_list)
# 방법1-1 reverse
new_list = sorted(numbers, reverse=True)
print(new_list)

# 방법2 sort
# sort함수는 아무것도 리턴하지 않고, 기존 리스트 정렬
print(numbers.sort()) # None
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)


