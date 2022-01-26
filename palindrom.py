def is_palindrome(word):
    """
    Checks if the passed string is palindrome and returns bool.
    :param word
    :return: bool
    """
    word = word.lower()
    return word == word[::-1]


word1 = 'palindrome'
word2 = 'Kayak'
word3 = 'abcDEedcba'
word4 = 'abcddedcba'

print(is_palindrome(word1))
print(is_palindrome(word2))
print(is_palindrome(word3))
print(is_palindrome(word4))
