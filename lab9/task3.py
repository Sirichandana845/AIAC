import string

def is_sentence_palindrome(sentence):
    # Remove punctuation and spaces, convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]

# Example usage
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(is_sentence_palindrome(s))  # Output: True
    s2 = "Hello, World!"
    print(is_sentence_palindrome(s2))  # Output: False
    s3 = "No 'x' in Nixon"
    print(is_sentence_palindrome(s3))  # Output: True
    s4 = "Was it a car or a cat I saw?"
    print(is_sentence_palindrome(s4))  # Output: True