import  re

a= '导演:弗兰克·德拉邦特FrankDarabont主演:蒂姆·罗宾斯TimRobbins/...'
b = "主演: 罗宾斯 Tim Robbins /..."
# pat = "导演:([\u4e00-\u9fa5]+[·| /s][\u4e00-\u9fa5]+)"

# pat = "导演:([^\x00-\xff]+)"
pat = "导演:(.*)主演"
pat2 = "主演:(.*)/"
rst11 = re.compile(pat).findall(a)
rst22 = re.compile(pat2).findall(b)
print(rst11[0])
print(rst22[0])