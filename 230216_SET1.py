"""SET"""
set1 = set()
set2 = {1, 2}
set3 = set("ababagalamaga")

print(set3)
set4 = set([(1, 2), (3, 5)])
print(set4)
lst1 = ["hello", "world", "word"]
def has_doubles(lst):
    # result = False
    if len(lst) == len(set(lst)):
        return False
    return True

if __name__ == "__main__":
    print(has_doubles(lst1))