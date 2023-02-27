

from ex06 import all_sum

def create_string(num):
    return f"this is num - {num}"
#result = all_sum(*[n for in range (100)])
def main():
    srt_result = create_string(all_sum(*[n for n in range (100)]))
    print(srt_result)
if __name__ == "__main__":
    print(main())
