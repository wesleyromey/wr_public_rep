# NOTE: This program 'encrypts' sentences using simple rules
#   such that the resulting sentence structure is readable by a human.
#   Essentially, this program can be used to create informal languages
#   like pig latin.
#   I'm not guaranteeing that pig latin is actually a language
#   one can make using this program, but the languages you can make
#   have the exact same feel


import sys


# These functions define how a sentence is 'encrypted'
ALPHA_NUMERIC_SET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def reverseStr(strOrig: str) -> str:
    return strOrig[::-1]
def findNextWord(strOrig: str, i0: int):
    i1 = i0
    while i1 < len(strOrig) and strOrig[i1] in ALPHA_NUMERIC_SET:
        i1 += 1
    return strOrig[i0:i1], i1 # str, int
def applyNewOrdering(ordering: list, strOrig: str) -> str:
    def solveOneCycle(cycleNum: int, ordering: list, strOrig: str) -> str:
        iMin = cycleNum * (max(ordering) + 1)
        iMax = min(iMin + max(ordering), len(strOrig) - 1)
        strOut = ""
        for i in ordering:
            iMod = i + iMin
            if iMod < iMin or iMod > iMax:
                continue
            strOut += strOrig[iMod]
        return strOut
    # Applies a new ordering to a particular word,
    #   NOTE: All indices from 0 to len(strOrig)-1 MUST be included in ordering at least once each
    #   If len(strOrig) > len(ordering), then apply ordering cyclically
    strOut = ""
    assert len(ordering) > 0 and len(strOrig) > 0
    numCycles = (len(strOrig) - 1) // max(ordering) + 1
    for cycleNum in range(numCycles):
        strOut += solveOneCycle(cycleNum, ordering, strOrig)
    return strOut
def changeLetterOrderPerWord(ordering: list, strOrig: str) -> str:
    # A word is any set of alphanumeric characters
    #   grouped together. The characters included here
    #   are defined in ALPHA_NUMERIC_SET
    # ordering: Modify the ordering of each word.
    #   If len(ordering) < len(word), then this the order cycles for all letters in the word 
    i0, i1 = 0, 0
    strOut = ""
    while i1 < len(strOrig):
        if strOrig[i1] in ALPHA_NUMERIC_SET:
            i1 += 1
        elif strOrig[i0] in ALPHA_NUMERIC_SET:
            strOut += applyNewOrdering(ordering, strOrig[i0:i1])
            i0 = i1
        else:
            strOut += strOrig[i0]
            i0 += 1
            i1 += 1
    if i0 < len(strOrig):
        strOut += applyNewOrdering(ordering, strOrig[i0:i1])
    return strOut
def doSentenceEncryption(strOrig: str, ordering = [], doReverse = False,
        prefix = "", postfix = "", charConversionDict = {}) -> str:
    # Order of operations: doReverse, ordering, prefix or postfix
    strOut = strOrig
    if charConversionDict:
        strOut = convertCharToChar(strOut, charConversionDict)
    if doReverse:
        strOut = reverseStr(strOrig)
    if ordering:
        strOut = changeLetterOrderPerWord(ordering, strOut)
    if prefix or postfix:
        strOut = appendToEachWord(strOut, prefix, postfix)
    return strOut
def appendToEachWord(origStr: str, prefix: str, postfix: int) -> str:
    # Add a prefix and / or a postfix to a word
    i0 = 0
    outputStr = ""
    while i0 < len(origStr):
        if origStr[i0] not in ALPHA_NUMERIC_SET:
            outputStr += origStr[i0]
            i0 += 1
            continue
        word, i0 = findNextWord(origStr, i0)
        outputStr += prefix + word + postfix
    return outputStr
def convertCharToChar(origStr: str, charConversionDict: dict):
    # If a character is NOT in charConversionDict, then keep it unchanged
    ans = ""
    for item in origStr:
        ans += charConversionDict[item] if item in charConversionDict else item
    return ans



# Unit Testing
def testCase_convertCharToChar(origStr: str, charConversionDict: dict, targetOutput: str):
    ans = convertCharToChar(origStr, charConversionDict)
    print(f"origStr: {origStr}, charConversionDict: {charConversionDict}, ans: {ans}")
    if ans != targetOutput:
        raise AssertionError(f"The answer should be {targetOutput}, but isn't! Aborting program!")
def testCase(ordering: list, origStr: str, doReverse: bool, targetOutput: str, prefix = "", postfix = ""):
    assert type(ordering) is list and type(origStr) is str and type(doReverse) is bool
    print(f"ordering: {ordering}, input string: \"{origStr}\", doReverse: {doReverse}, output: ", end = "")
    ans = doSentenceEncryption(origStr, ordering, doReverse, prefix, postfix)
    print(f"\"{ans}\"")
    if ans != targetOutput:
        raise AssertionError(f"The answer should be {targetOutput}, but isn't! Aborting program!")
def testCases():
    # Place the test cases here
    if False:
        testCase([0], "", False, "", "", "")
        testCase([0], "a", False, "a", "", "")
        testCase([2,1,0], "a", False, "a", "", "")
        testCase([2,1,0], "abc", False, "cba", "", "")
        testCase([2,1,0], "abcd", False, "cbad", "", "")
        testCase([], "abcdefg hijk!", True, "!kjih gfedcba", "", "")
        testCase([0,1,2,3], "abcdefg 12345 123.today!", False, "abcdefg 12345 123.today!", "", "")
        testCase([1,0], "abcd.efg.12..5 or else(1)", False, "badc.feg.21..5 ro lees(1)", "", "")
        testCase([10,9,8,7,6,5,4,3,2,1,0], "A sentence.", True, ".sentence A", "", "")
        testCase([], "This sentence", False, "preThispost presentencepost", "pre", "post")
        testCase([2,3,1,0], "This sentence", True, "pre_neceesnt_post pre_hTis_post", "pre_", "_post")
        #   "ecnetnes sihT", "neceesnt hTis"
        testCase([0,0,1,2], "This is a super long doubleTheDoublingWords!!!", False, 
                "TThiss iis aa ssupeer llongg ddoubbleTTheDDoubblinngWoordss!!!", "", "")
    testCase_convertCharToChar("abcdefg ...", {'b': 'a', 'c': 'a', '.': 'Q'}, "aaadefg QQQ")

# Format the inputs correctly
def constructArrFromStr(arrStr: str) -> list:
    if arrStr == "" or arrStr == "[]" or arrStr == "_":
        return []
    digitSet = "0123456789"
    ans = []
    i0 = 0
    for i1, item in enumerate(arrStr):
        if arrStr[i0] not in digitSet:
            i0, i1 = i0 + 1, i0 + 1
        elif item not in digitSet:
            ans.append(int(arrStr[i0:i1]))
            i0 = i1
        else:
            i1 += 1
    if len(arrStr) > 0 and arrStr[i0] in digitSet:
        ans.append(int(arrStr[i0:]))
    return ans
def convStrToBoolean(origStr: str) -> bool:
    convToFalse = {0, False, "0", "False", "false", "no", "n", "_", ""}
    convToTrue = {1, True, "1", "True", "true", "yes", "y"}
    if origStr in convToFalse: return False
    if origStr in convToTrue: return True
    raise AssertionError("Type 0 for False and 1 for True")
def constructCharConversionDict(charConvStr: str):
    # NOTE: If you want to convert capital letters,
    #   then you MUST define separate pairs of values for them!!!
    ans = dict()
    if charConvStr == "_":
        return ans
    assert len(charConvStr) % 2 == 0
    for i in range(0, len(charConvStr), 2):
        ans[charConvStr[i]] = charConvStr[i+1]
    return ans
def main(*args, **kwargs):
    DEBUG = False
    if DEBUG:
        print(f"sys.argv (command terminal arguments): {sys.argv}")
        testCases()
        return
    # Ensure the command terminal arguments (e.g. sys.argv) are formatted correctly
    if len(sys.argv) == 0:
        raise AssertionError("len(sys.argv[0]) should be the file which is run!!!")
    elif len(sys.argv) == 1:
        # User input (no command terminal arguments except for file name / path)
        orderingStr = input("Type in the ordering you want (ex. [3,2,0,1]): ")
        origStr = input("Type in the sentence you want to encrypt: ")
        doReverseStr = input("Reverse the sentence? ")
        prefix = input("Prefix to add at the end of each word (if none, leave blank): ")
        postfix = input("Postfix to add at the end of each word (if none, leave blank): ")
        charConversionStr = input("charConversionDict (convert a character to another - leave blank if not used): ")
    elif len(sys.argv) == 7:
        _, orderingStr, origStr, doReverseStr, prefix, postfix, charConversionStr = sys.argv
    else:
        msg = "\nIf using the command terminal, type either \"python main.py\" or "
        msg += "\"python main.py <ordering> \"<strOrig>\" <doReverse> <prefix> <postfix> <charConvStr>\""
        msg += "\n\tFor example: python main.py \"[2,3,1,0]\" \"This sentence will be modified\" True \"pre-\" \"-post\" \"bacada\""
        msg += "\n\tFor example: python main.py [0,1] oneWord. 0 pre_ _post bacad5"
        msg += "\n\tFor example: python main.py [] oneWord _ _ _ _"
        msg += "\n\tFor example: python main.py _ \"A sentence.\" 0 _ _ _"
        msg += "\n\t\t(NOTE: _ means the argument is being set to empty!)"
        msg += "\n"
        raise AssertionError(msg)
    ordering = constructArrFromStr(orderingStr)
    doReverse = convStrToBoolean(doReverseStr)
    if prefix == "_": prefix = ""
    if postfix == "_": postfix = ""
    charConversionDict = constructCharConversionDict(charConversionStr)
    ans = doSentenceEncryption(origStr, ordering, doReverse, prefix, postfix, charConversionDict)
    print("\n\n" + ans)

if __name__ == "__main__":
    main()