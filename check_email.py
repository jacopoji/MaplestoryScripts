import pyperclip


if __name__ == "__main__":
    with open("accounts_check.txt","r") as f:
        replaced_str = f.read().replace("\n",";")
        split_str = replaced_str.split(";")
        count = 0
        for strings in split_str:
            pyperclip.copy(strings)
            if(count % 2 == 0):
                print("The email account is : {}".format(strings))
                input("Hit enter for password")
            else:
                print("The email password is : {}".format(strings))
                input("Hit enter for account")
            count += 1