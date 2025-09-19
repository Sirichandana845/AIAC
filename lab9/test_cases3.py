import random
import string

def is_sentence_palindrome(sentence):
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]

def generate_palindrome_sentence():
    # Generate a random palindrome word
    half = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7)))
    palindrome = half + half[::-1]
    # Randomly insert spaces and punctuation
    chars = list(palindrome)
    for _ in range(random.randint(1, 3)):
        idx = random.randint(0, len(chars)-1)
        chars.insert(idx, random.choice([' ', ',', '.', '!', '?']))
    # Randomly capitalize some letters
    chars = [c.upper() if random.random() < 0.3 else c for c in chars]
    return ''.join(chars)

def generate_non_palindrome_sentence():
    # Generate a random non-palindrome word
    word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 12)))
    while word == word[::-1]:
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 12)))
    # Randomly insert spaces and punctuation
    chars = list(word)
    for _ in range(random.randint(1, 3)):
        idx = random.randint(0, len(chars)-1)
        chars.insert(idx, random.choice([' ', ',', '.', '!', '?']))
    # Randomly capitalize some letters
    chars = [c.upper() if random.random() < 0.3 else c for c in chars]
    return ''.join(chars)

def generate_test_cases(num_cases=5):
    test_cases = []
    # Palindrome cases
    for _ in range(num_cases):
        sentence = generate_palindrome_sentence()
        test_cases.append((sentence, True))
    # Non-palindrome cases
    for _ in range(num_cases):
        sentence = generate_non_palindrome_sentence()
        test_cases.append((sentence, False))
    random.shuffle(test_cases)
    return test_cases

if __name__ == "__main__":
    test_cases = generate_test_cases(5)
    for idx, (sentence, expected) in enumerate(test_cases, 1):
        result = is_sentence_palindrome(sentence)
        print(f"Test case {idx}: '{sentence}'")
        print(f"Expected: {expected}, Got: {result}")
        print("Pass" if result == expected else "Fail")
        print("-" * 40)