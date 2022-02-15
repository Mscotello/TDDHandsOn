def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    symbols = "~`!@#$%^&*()_+-="
    symbolFlag = 0
    lowerCaseFlag = 0
    upperCaseFlag = 0
    numberFlag = 0
    for char in pwd:
        if str.islower(char):
            lowerCaseFlag = 1
        if str.isupper(char):
            upperCaseFlag = 1
        if str.isnumeric(char):
            numberFlag = 1
        if char in symbols:
            symbolFlag = 1
    if lowerCaseFlag == 0 or upperCaseFlag == 0 or numberFlag == 0 or symbolFlag == 0:
        return False

    return True
