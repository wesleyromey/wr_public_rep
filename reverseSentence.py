# This program is designed to reverse the characters in a string
def reverseStr(str1: str) -> str:
    str2 = ""
    for i in range(len(str1)-1, -1, -1):
        str2 += str1[i]
    return str2

def __main__():
    print("Input a sentence you want reversed: ")
    strIn = input()
    ans = reverseStr(strIn)
    print()
    print(ans)

if __name__ == "__main__":
    __main__()