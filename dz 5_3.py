def is_check_name(fullname, first_name):
    s = fullname.removesuffix("Old").strip()
    s1 = fullname.removeprefix(first_name).strip()
    s2 = fullname.startswith(first_name)
    if(first_name.lower() != s.lower()):
        print (True)
    else:
        print (False)
    print (f"суфикс строки fullname {s}")
    print (f"префикс строки fullname {s1}")
    print (f"стартсвич строки fullname (True, False) - {s2}")
    # #print(f"fullname - {fullname().removeprefix(fullname)}")
    # print(f"fullname - {fullname()}", f" first - {first_name()}")
    # print(first_name().removeprefix(fullname))
is_check_name("Alex Old", "Alex")

#print('TestHook'.removeprefix('Test'))   # Hook
#print('TestHook'.removeprefix('Hook'))   # TestHook

#print('TestHook'.removesuffix('Hook'))   # Test
#print('TestHook'.removesuffix('Test'))   # TestHook

#Это результат проверки, является ли строка first_name префиксом строки fullname. 