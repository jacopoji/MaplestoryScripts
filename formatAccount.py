
if __name__ == "__main__":
    with open("accounts.txt","r") as f:
        split_str = f.read().split(",")
        count = 0
        with open("accounts_formatted.txt","w") as w:
            for text in split_str:
                frag = text.split(":")
                w.write("{};{}".format(frag[0],frag[1]))

