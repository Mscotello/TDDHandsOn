def check_pwd(pwd):
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    lowerCaseFlag = 0
    for char in pwd:
        if str.islower(pwd):
            lowerCaseFlag = 1
    if lowerCaseFlag == 0:
        return False
    return True
