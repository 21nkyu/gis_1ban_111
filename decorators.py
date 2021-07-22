
#
# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작!')
#         func(input_text)
#         print('함수 끝!')
#     return decorated
#
#
# @decorator
# def hello_world(input_text):
#     print(input_text)
#
#
#
# hello_world('Hello_World!')
# #
# width
# hight

def decorator(func):
    def decorated(width, height):
        if width > 0 and height > 0:
            func(width, height)
        else:
            print('Error')
    return decorated


@decorator
def area(width, height):
    print((width * height) * 1/2)

area(5, 6)

@decorator
def tri_area(width, height):
    print((width * height))

tri_area(5, 6)
#
#
# area(4, 5)
#
#
# def check_integer(func):
#     def decorated(width, height):
#         if width >= 0 and height >= 0:
#             return func(width, height)
#         else:
#             raise ValueError('input must be positive value')
#     return decorated
#
# @check_integer
# def rect_area(width, height):
#     return width * height
#
# def rect_
#
# print(rect_area(5, 6))


# class User:
#     def __init__(self, auth):
#         self.is_autenticated = auth
#
# user =User(auth=False)


