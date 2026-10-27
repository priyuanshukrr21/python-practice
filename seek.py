with open("data.txt", "r", encoding="utf-8") as f:
    print(f.tell())
    f.read(5)
    f.seek(0)
    print(f.tell())
    f.read(5)
    print(f.read(5))