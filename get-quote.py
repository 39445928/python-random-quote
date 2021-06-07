# _*_ coding:utf-8 _*_
def testmain():
    print("Keep it logically awesome.")

    f = open("quotes.txt")

    quotes = f.readlines()
    f.close()

    # with open("quotes.txt") as f:
    #     quotes = f.readlines()

    print(quotes)


if __name__ == "__main__":
    testmain()
