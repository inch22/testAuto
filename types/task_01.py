
# def dis(a):
#
#     if a != 6:
#         return True
#     else:
#          return "Только не 6!"
#
# print(dis(6))

def dis(a):

    if a == 6 and isinstance(a, int):

         return 'Только не 6!'

    return True

print(dis(6))