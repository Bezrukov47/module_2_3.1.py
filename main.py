my_list: int = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print (my_list)
index = 0
while index < len(my_list):
   index += 1
   if my_list[index] < 0:
       break
   if my_list[index] > 0:
       print (my_list[index])
       continue
   if my_list[index] == -6:
       break
       print (my_list[index])
