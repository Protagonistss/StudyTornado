async def divide(x, y):
    return x / y


def bad_call():
    divide(1, 0)


print(bad_call())


async def good_call():
    await divide(1, 0)


print(good_call())
