# Understanding Scopes in Python
count = 1

def increase_count():
    count = 2
    print(f"Count inside function: {count}")

increase_count()
print(f"Count Outside function: {count}")