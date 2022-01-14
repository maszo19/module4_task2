def is_palindrome(word):
    for i in range(len(word) // 2):
        a = word[i]
        b = word[-1 -i]
        if word[i] != word[-1 -i]:
            return False
    return True

word1 = 'palindrome'
word2 = 'kayak'
word3 = 'abcdeedcba'
word4 = 'abcddedcba'

print(is_palindrome(word1))
print(is_palindrome(word2))
print(is_palindrome(word3))
print(is_palindrome(word4))