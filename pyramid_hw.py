def makePyramid(num):
  count = 0
  for i in range(1, num + 1):
    if(i % 2 == 0):
      result = '* ' * i
      print(result)
      count += 1
    else:
      half = int((i - 1) / 2)
      result = ('* ' * half + '😊 ' + '* ' * half)
      print(result)
      count += 1
  while count:
    if(count % 2 == 0):
      result = '* ' * count
      print(result)
      count -= 1
    else:
      half = int((count - 1) / 2)
      result = ('* ' * half + '😊 ' + '* ' * half)
      print(result)
      count -= 1
makePyramid(num=5)