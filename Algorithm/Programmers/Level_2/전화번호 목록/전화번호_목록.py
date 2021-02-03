phone_book = [["119", "97674223", "1195524421"],["123", "456", "789"],["12", "123", "1235", "567", "88"]]

def solution(phone_book):
    phone_book.sort()
    l = len(phone_book)
    for i in range(0,l):
        for j in range(i+1,l):
            if not (phone_book[j].find(phone_book[i])):
                return False
    return True
                
for i in phone_book:
    print(solution(i))