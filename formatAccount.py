# Account original format email@aol.com:Password:DoB:EmailPassword:Kylie:Lopez, 
#
#
#

def FormatAccount(formatType = 1):
    if formatType == 1:
        with open("accounts.txt","r") as f:
            split_str = f.read().split(",")
            count = 0
            with open("accounts_formatted.txt","w") as w:
                for text in split_str:
                    frag = text.split(":")
                    w.write("{};{};{}/spw=000111;r=2000;w=45;i=0".format(frag[0].replace(" ","").split("@")[0],frag[0].replace(" ","").replace("\n",""),frag[1]).replace(" ",""))
            with open("accounts_check.txt","w") as w:
                for text in split_str:
                    frag = text.split(":")
                    w.write("{};{}\n".format(frag[0].replace(" ","").replace("\n",""),frag[3].replace(" ","")))
    elif formatType == 2:
        with open("accounts.txt","r") as f:
            split_str = f.read().split(",")
            count = 0
            with open("accounts_formatted.txt","w") as w:
                for text in split_str:
                    frag = text.split(":")
                    w.write("{};{};{}/spw=000111;r=2000;w=45;i=0".format(frag[0].replace(" ","").split("@")[0],frag[0].replace(" ","").replace("\n",""),frag[1]).replace(" ",""))
            with open("accounts_check.txt","w") as w:
                for text in split_str:
                    frag = text.split(":")
                    w.write("{};{}\n".format(frag[0].replace(" ","").replace("\n",""),frag[1].replace(" ","")))



if __name__ == "__main__":
    # with open("accounts.txt","r") as f:
    #     split_str = f.read().split(",")
    #     count = 0
    #     with open("accounts_formatted.txt","w") as w:
    #         for text in split_str:
    #             frag = text.split(":")
    #             w.write("{};{};{}/spw=000111;r=2000;w=45;i=0".format(frag[0].replace(" ","").split("@")[0],frag[0].replace(" ","").replace("\n",""),frag[1]).replace(" ",""))
    #     with open("accounts_check.txt","w") as w:
    #         for text in split_str:
    #             frag = text.split(":")
    #             w.write("{};{}\n".format(frag[0].replace(" ","").replace("\n",""),frag[3].replace(" ","")))
    FormatAccount(2)

