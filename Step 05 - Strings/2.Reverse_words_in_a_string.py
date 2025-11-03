# Brute Force
def reverseWords(s: str) -> str:
    words = s.split()
    stack = []
    for w in words:
        stack.append(w)
    result = ""
    while stack:
        result += stack.pop()
        if stack:
            result += " "
    return result
# Example
print(reverseWords("this is an amazing program"))  # "program amazing an is this"
# Time Complexity - O(N)
# Space Complexity - O(N)

# Optimal
def reverseWordsOptimized(s: str) -> str:
    s = s.strip()  # remove leading/trailing spaces
    i = len(s) - 1
    result = ""
    word = ""
    while i >= 0:
        if s[i] != " ":
            word = s[i] + word
        else:
            if word:
                result += word + " "
                word = ""
        i -= 1
    if word:  # add last word
        result += word
    return result.strip()
# Example
print(reverseWordsOptimized("this is an amazing program"))  # "program amazing an is this"
# Time Complexity - O(N)
# Space Complexity - O(1)