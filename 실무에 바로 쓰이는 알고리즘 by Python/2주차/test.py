from structures import LinkedList
from prac import isPalindrome


l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)


assert isPalindrome(l1)
assert not isPalindrome(l2)