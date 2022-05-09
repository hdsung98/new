# 문자열 다루기

string_input = "  abcd ,    abcd  "

# 문자열을 콤마를 기준으로 나누어 각각 저장해보세요
a,b=string_input.split(',')

# 두 개의 문자열이 가진 앞뒤 공백을 제거해볼까요?
a_erase=a.replace(" ","")
b_erase=b.replace(" ","")

# 두 개의 문자열이 같은지 비교하여 결과를 출력해보세요
if(a_erase==b_erase):
  print(a_erase,",",b_erase,"는 같은 문자입니다")
else:
  print("서로 다릅니다")
# 다시 두 개의 문자열을 합쳐 하나의 문자열로 만드세요
combine=a_erase+b_erase

# 합친 문자열의 길이를 출력해보세요
print(combine,"의 문자길이는",len(combine),"입니다")
