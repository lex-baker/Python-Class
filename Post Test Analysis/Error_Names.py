try:
    x = 5 / 0
except Exception as e:
    print(e)
    print(type(e).__name__)