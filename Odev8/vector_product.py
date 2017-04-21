def vector_product(vec1, vec2):
  toplam = 0
  if len(vec1) != len(vec2):
    return 0
  for x in range(len(vec1)):
    toplam += vec1[x] * vec2[x]
  return toplam

vector1=[1, 2, 3]
vector2=[4, 5, 6]
print(vector_product(vector1, vector2))
