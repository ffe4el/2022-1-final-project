<!--Heading-->

# <**프로그래밍 원리와 실습**>
## ✨final project✨
### *202116266 김솔아👧 202116302 전혜진🧔*

<!--Quote-->
> 이수업을 통해 프로그래밍의 세계로 빠져들어버린 2인..!!
> 프로그래밍 집착광공이 되어버리는데...

### 목차
____
#### 1. 원예실습 환경데이터 자동화 구현
* 주제를 선정하게 된 이유
* *Pandas* 라이브러리
* *OpenPyXL* 모듈
* *Numpy* 라이브러리
* 구체적인 환경데이터 자동화 구현 방법
* 느낀점과 아쉬운점

#### 2. 틀린그림찾기 게임 제작
* 주제를 선정하게 된 이유
* *Pygame* 라이브러리
* 구체적인 게임 구현 방법
* 느낀점과 아쉬운 점

<br><br><br><br>
## <1. 원예실습 환경 데이터 자동화 구현>

---


### 주제를 선정하게 된 이유
우리는 1학기 동안 원예작물 재배 및 실습 과목을 전공필수로 수강하게 되었다. 해당 수업에서는 바질이나 상추를 키우고, 그 작물에 센서를 달아 온도, 습도, 광도를 측정하는 실습을 진행했다.
 약 분 단위로 측정되는 데이터들이 thingspeak라는 사이트에 csv파일 형태로 기록되었는데, 그 데이터를 일별로 정리하고 그래프를 그려 데이터를 시각화 하는것이 매주 과제로 진행되었다. 
그런데 엄청난 양의 데이터를 직접 엑셀 정리하다보니 **귀찮음**을 느꼈다. 과제를 하다보니 단순 반복이라는 것이 느껴졌고 또 조원이 격주로 돌아가면서 하다보니 형식도 조금씩 어긋나게 되었다.

*"분명 알고리즘은 하나인데... 이걸 **단일화**하고, **자동화**할 수 있는 방법은 없을까..? 
될 것 같은데..?!*

프로그래밍 원리 실습의 기말 프로젝트 주제를 찾던 중에 더 또렷하게 느껴지는 이 과제의 귀찮음...
여기서부터 우리의 프로젝트는 시작되었다.

*"엄청 대단한 주제 찾지말고, 우리가 정말로 **필요한** 프로그램을 만들어보자!"*

기존에 우리는 엑셀이라는 프로그램을 이용해서 데이터를 계산하고 분석했다. (아래 그림 참고)
![execl image](https://drive.google.com/uc?id=1jVxYlm8JthRru44xnhQn9uduqsyLE7vY)
이를 Python을 이용해서 자동화를 시킬 예정인데...
자동화를 시키기 앞서 이 프로젝트의 알고리즘을 생각해보았다!

**엑셀파일 만들기  ➡  csv 데이터 받아오기  ➡  환경데이터 계산표 만들기  ➡  그래프 생성**

일단 Python에서 엑셀을 다루기 위해선 그에 맞는 라이브러리 사용이 필요하다.
Python에서 엑셀을 다루는 라이브러리는 크게 2가지가 있다.
##### ☝Pandas 
##### ✌OpenPyXL

환경데이터 자동화를 하기 위해선 위 두가지 라이브러리에 대한 학습이 필요했다.

<br>
<br>
<br>
<br>



### ➰*Pandas* 라이브러리
---
#### 팬더스(pandas)란?
![Pandas image](https://miro.medium.com/max/1080/1*Io7MqMWpE5flq67RRD3lRw.jpeg)
파이썬 언어로 작성된 데이터를 분석 및 조작하기 위한 소프트웨어 라이브러리이다.
##### <pandas의 주요 특성>
- 통합 인덱싱을 활용한 데이터 조작을 가능하게 하는 데이터프레임(DataFrame) 오브젝트
- 인메모리(in-memory) 데이터 구조와 다양한 파일 포맷들 간의 데이터 읽기/쓰기 환경 지원
- 데이터 결측치의 정렬 및 처리
- 데이터셋의 재구조화 및 피보팅
- 레이블 기반의 슬라이싱, 잘 지원된 인덱싱, 대용량 데이터셋에 대한 서브셋 지원
- 데이터 구조의 칼럼 추가 및 삭제
- 데이터셋의 분할-적용-병합을 통한 GroupBy 엔진 지원
- 데이터셋 병합(merging) 및 조인(joining) 지원
- 저차원 데이터에서의 고차원 데이터 처리를 위한 계층적 축 인덱싱 지원
- date range, 빈도 변환, 이동 창 통계, 이동 창 선형회귀, 날짜 이동 등의 시계열 작업 지원, 데이터 필터 지원
  
[출처 Cliclk](https://namu.wiki/w/Pandas)
<br>

pandas라이브러리를 공부하며 정리해둔 코드를 기록해보려고 한다.
<br>

1. pandas DataFrame을 이용해서 표 만들기
<!-- Code -->
```py
import pandas as pd
def df_maker(col_num, ind_num, fill):
    col = []
    ind = []
    con = []
    for i in range(0,col_num):
        col.append(fill)
    for i in range(0,ind_num):
        ind.append(fill)
    for i in range(0,ind_num):
        con.append(col)

    df = pd.DataFrame(con, columns=col, index=ind)
    return print(df)

df_maker(10,10,"ㅋ")
```
이를 통해 10행, 10열이고 내용이 ㅋ으로 구성된 표를 만들 수 있다.

<br><br>
2. 행열의 사이즈를 정하고, 안에 내용을 수정해서 넣어 표 만들기

```py
import pandas as pd
col = [0, 0, 0]
ind = [0, 0, 0, 0, 0, 0, 0]
con = [[0, 0, 0], [0, 0, 0],[0, 0, 0], [0, 0, 0],[0, 0, 0], [0, 0, 0], [0, 0, 0]]
df = pd.DataFrame(con, columns=col, index=ind)

print(df.columns) #Int64Index([0, 0], dtype='int64')
print(df.index) #Int64Index([0, 0], dtype='int64')
df.columns=["Temp", "RH", "Lux"]                                 #열제목
df.index=["날짜1", "날짜2", "날짜3", "날짜4", "날짜5", "날짜6", "날짜7"]  #행제목
print(df) #행열 출력

print("-"*30)
# 가로 방향 선택하는 방법
# ① index의 내용으로 선택하는 방법 :  df.loc
print(df.loc['날짜1'])
# ② index의 순서로 선택하는 방법 : df.iloc
print(df.iloc[0])

print("-"*30)
#content 채우는 방법
df.loc["날짜1"] = [20.2, 52.9, 2558]
df.loc["날짜2"] = [20.5, 53, 2600]
df.loc["날짜3"] = [20.2, 52.9, 2558]
df.loc["날짜4"] = [20.5, 53, 2600]
df.loc["날짜5"] = [20.2, 52.9, 2558]
df.loc["날짜6"] = [20.5, 53, 2600]
df.loc["날짜7"] = [20.2, 52.9, 2558]
print(df)
```

print(df)의 결과는 이렇게 나온다. 

>            Temp   RH   Lux
>     날짜1  20.2  52.9  2558
>     날짜2  20.5  53.0  2600
>     날짜3  20.2  52.9  2558
>     날짜4  20.5  53.0  2600
>     날짜5  20.2  52.9  2558
>     날짜6  20.5  53.0  2600
>     날짜7  20.2  52.9  2558

<br><br>
3. 이런식으로 행과 열의 정보만 수정할 수도 있다.
```py
import pandas as pd

def df_maker(col_num, ind_num, fill):
    col = []
    ind = []
    con = []
    for i in range(0,col_num):
        col.append(0)
    for i in range(0,ind_num):
        ind.append(0)
    for i in range(0,ind_num):
        con.append(0)

    df = pd.DataFrame(con, columns=col, index=ind)
    return print(df)


df = df_maker(3, 3, 0) # 3X3 데이터 프레임 생성 0으로 채움
col = ["A","B","C"]
ind = [1,2,3]
df.columns = col  # 컬럼 col 리스트로 덮어씌움
df.index = ind    # 인덱스 ind 리스트로 덮어씌움
```



<br><br><br><br>
### ➰*OpenPyXL* 모듈

---

#### OpenPyXL이란? 
![OpenPyXL Image](https://w3cschoool.com/public/file/Python/python-openpyxl-tutorial.png)

OpenPyXL은 Excel 파일을 읽고 쓰기를 Python으로 할 수 있는 일종의 모듈이다. 
예를 들어 아래와 같은 조작이 가능하다.
- 셀 번호를 지정해서 이미지나 문자열을 입력할 수 있다.
- Excel 파일의 시트 데이터를 복사해서 다른 시트에 붙여넣기 할 수 있다.
- 시트를 추가하거나 삭제할 수 있다.
다만 이 모듈을 사용하기 위해서 주의해야할 점이 한 가지가 있는데 바로 확장자가 ".xlsx"여야한다는 것이다.
<!-- Link -->
[출처 Cliclk](https://engineer-mole.tistory.com/211)
<br><br>
OpenPyXL모듈을 공부하면서 작성한 코드를 기록해보고자 한다.
<br><br>

1. 새 워크시트 파일 열기

```py
#open_file.py
from openpyxl import load_workbook

wb = load_workbook('xb.xlsx')

ws = wb['Sheet']              #해당 시트 지정
print(ws['A1'].value)
ws['A1'] = "TEST DATA"        #A1셀에 내용 넣기
print(ws['A1'].value)

print(ws.cell(row=1, column=1))

wb.save('wb_insert.xlsx')     #엑셀 파일 저장하기

```

2. 엑셀파일 만들기 

```py
from openpyxl import Workbook
wb = Workbook()

ws = wb.active

ws1 = wb.create_sheet("시트0") # 가장 뒤에 시트 생성 (기본값)
ws2 = wb.create_sheet("시트1", 0) # 가장 앞에 시트 생성 
ws3 = wb.create_sheet("시트2", -1) # 끝에서 두 번째에 시트 생성

print(wb.sheetnames)

wb.save('xb.xlsx')
```

3. 엑셀 파일에 내용 수정하기

```py
from openpyxl import Workbook
import os ; os.remove("wb_subtitle.xlsx") 
#os 모듈에서 불러와 remove() 함수로 삭제하며 ;으로 한 줄로 사용

wb = Workbook()

ws = wb.active # 기본 시트 가져오기 (활성 중인 워크 시트 가져오기)

# 첫째행 타이틀 적기 예제
# 제목 적기
sub = ['created_at', 'entry_id', 'temp', 'humid', 'lux', '', 'date', 'SVP', 'VPD']
for kwd, j in zip(sub, range(1, len(sub)+1)): #for zip을 이용해서 2번째 행에 순서대로 제목을 적는다.
    ws.cell(row=2, column=j+1).value = kwd

wb.save("wb_subtitle.xlsx") #저장
```

4. 구구단 입력 엑셀 파일 만들어보기

```py
from openpyxl import Workbook

wb = Workbook()

ws = wb.active

# 구구단 단 입력

for i in range(1, 6):
    ws.cell(row=2, column=i+1).value = f"{i}단"

# - 내용 입력
for row in range(1, 9): 
    for column in range(1, 6): # 1단부터 5단까지
        # 초기화하면서 데이터 입력
        c = ws.cell(row=row+2, column=column+1, value=row*column)
        # 데이터 수정
        c.value=row*column

wb.save("wb_multiplication.xlsx")
```

5. 엑셀파일에서 데이터 읽어오기

```py
from openpyxl import load_workbook

wb = load_workbook('wb_multiplication.xlsx')
ws = wb['Sheet']

#지난 글에서 ws의 시트 객체에서 ['A1'] 형식으로 덱싱하면 A1 셀을 지칭하여 값을 가져올 수 있었다.
#- ['C']처럼 행 번호를 생략하고 열 문자만 작성하면 열에 있는 셀들이 전체 지정된다.
#- ['2']처럼 열 문자를 생략하고 행 번호만 작성하면 행에 있는 셀들이 전체 지정된다.
#- 각 셀 객체는 지난 글에서 dir() 함수로 살펴본 것처럼 value와 같은 여러 속성과 함수를 지원한다.
#밑에 참조

print(ws["C"]) #열 문자는 대문자로 작성한다.
for cell in ws["C"]:
    print(cell.value)

print(ws["2"])
for cell in ws["2"]:
    print(cell.value)


#for 반복문으로 데이터를 입력한 것처럼 for문을 사용해 엑셀 시트의 내용을 읽어와보자.

#- n단은 리스트컴프리헨션으로 None 값이 아닌 2행 셀 값 전체를 가져와서 띄어쓰기로 구분해 문자열로 묶었다.

#- 구구단 내용은 입력을 했을 때 사용했던 것과 마찬가지 형식을 사용했다.

#- 내용 출력 시 %3d 및 % 포맷팅을 사용해 띄어쓰기를 맞춰주었다.

#for 반복문으로 데이터를 입력한 것처럼 for문을 사용해 엑셀 시트의 내용을 읽어와보자.

#- n단은 리스트 컴프리헨션으로 None 값이 아닌 2행 셀 값 전체를 가져와서 띄어쓰기로 구분해 문자열로 묶었다.

#- 구구단 내용은 입력을 했을 때 사용했던 것과 마찬가지 형식을 사용했다.

#- 내용 출력 시 %3d 및 % 포맷팅을 사용해 띄어쓰기를 맞추기.

print("".join([cell.value for cell  in ws["2"] if cell.value is not None]))
for row in range(1,9):
    for column in range(1,6):
        c = ws.cell(row=row+2, column=column+1)
        print("%3d" %(c.value), end='')
    print()

#특정 범위 셀 값을 읽어올 때 iter_rows()나 iter_cols() 함수를 사용할 수도 있다.
#iter_rows와 iter_cols는 반복 가능한 객체(iterable)를 반환하여 반복문으로 열 객체를 가져와 사용한다.

for row in ws.iter_rows(min_row=1, max_col=3):
    for cell in row:
        print(cell)
        
# values_onely를 이용하여 값만 확인할 수 있다.
for row in ws.iter_rows(min_row=1, max_col=3, values_only=True):
    for cell in row:
        print(cell)
```

추가로 엑셀에서 범위 지정이 가능하다.

특정 범위 접근 : cell_range = sheet['A1':'C2']

특정 행 접근 : sheet[10]

특정 행 범위 접근 : sheet[5:10]

특정 열 접근 : sheet['C']

특정 열 범위 접근 : sheet['C:D']

파이썬의 2차원 배열 인덱싱 형식에 따라 : sheet[3][2]와 같이도 가능 (C열 = 3, 2행 =2)

<br><br>
6. 엑셀 함수 사용하고 적용하기
```py
#openpyxl의 단점은 pandas와 같이 쉽게 데이터를 불러오거나 저장하기 어렵다는 점
#구구단 숫자 표에서 기초 통계를 구한다.

from openpyxl import load_workbook

wb=load_workbook('wb_multiplication.xlsx')
ws = wb['Sheet']


#구구단 헤드 지정 및 n단까지 있는지 확인
wrow = ws["2"]
wrow_data = [cell.value for cell in wrow if cell.value is not None]
# => 있는 정적 데이터에 따라 계산하는 것이 아닌 유동적으로 처리할 수 있도록 2행에서 
# None 값이 아닌 데이터를 전부 가져와서 wrow_data에 담는다.


#사용할 통계 함수
func_table = {
    '합계': "SUM",
    "평균": "AVERAGE",
    "최댓값": "MAX",
    "최솟값": "MIN"
}
# =>사용할 통계 함수 설명 텍스트와 함수 이름을 func_table 변수에 담는다.


#사용할 통계 텍스트 입력
start_row = 11
sub = list(func_table.keys())    #-> keys()는 왜 필요한 코드인지 잘 모르겠음
for kwd,j in zip(sub, range(1, len(sub)+1)):
    ws.cell(row=start_row+j, column=1).value = kwd  #-> kwd는 왜 여기에 필요한 부분일까?
# =>func_table에서 텍스트만 먼저 입력한다. 텍스트가 입력될 셀은 A12:15 셀이다. 
# 추가로 함수를 사용해도 문제 없도록 table에서 keys()를 꺼내 리스트를 만들고 길이에 따라 값을 꺼내와서 사용한다. 
# column은 1로 고정에 행 값만 row만 12부터 시작해 길이까지 반복해서 텍스트를 입력한다.


#통계 함수 적용
#반복문 테스트를 위해 한 셀에 함수를 먼저 사용해본다. 
# 첫 번째로 함수가 들어가는 합계를 구할 셀은 B12셀이며 B3부터 B11까지 더하라고 함수를 입력했다.
ws["B12"].value = "=SUM(B3:B11)"

#함수 입력 자동화
func_list = list(func_table.values())
for row in range(1, len(sub)+1):
    func=func_list[row-1]

    for column in range(1, len(wrow_data)+1):
        work_col = chr(65+column) #65=A
        formula_range = f"{work_col}3:{work_col}11" #->f는 왜 쓰는걸까요?
        ws[start_row+row][column].value = f"={func}({formula_range})"
#- func 변수 :  행 단위로 먼저 반복해서 사용할 함수를 정한다.
#- work_col 변수 : column마다는 현재 컬럼 index에 따라 2번째면 아스키코드 66에 대응하는 B부터 시작하도록 설정했다.
#- formula_range 변수에는 work_col를 사용해 f-string으로 함수에 사용할 수식 범위를 만든다.


wb.save("wb_mutiple_func.xlsx")
```

OpenPyXL을 이용하여 엑셀에 있는 함수들까지 쓸 수 있기 때문에 이를 이용해서 환경데이터를 계산할 수 있다.

<br><br><br><br>
### ➰*Numpy* 라이브러리
---
#### Numpy란?
![Numpy Image](https://t1.daumcdn.net/cfile/tistory/993270495B18DDE322)

Numpy는 C언어로 구현된 파이썬 라이브러리로써, 고성능의 수치계산을 위해 제작되었다. Numerical Python의 줄임말이기도 한 Numpy는 벡터 및 행렬 연산에 있어서 매우 편리한 기능을 제공한다.
Numpy의 핵심이라고 불리는 다차원 행렬 자료구조인 ndarray를 통해 벡터 및 행렬을 사용하는 선형 대수 계산에서 주로 사용된다. Numpy는 편의성뿐만 아니라, 속도면에서도 순수 파이썬에 비해 압도적으로 빠르다는 장점이 있다.

[출처1 Cliclk](https://doorbw.tistory.com/171)

[출처2 Cliclk](https://wikidocs.net/32829)

Numpy 또한 리스트 배열을 통해 표형태를 만들 수 있지만 엑셀과의 호환성은 떨어진다.
그렇기 때문에 Numpy는 학습만 하고 프로젝트에 응용하진 못했다.

<br><br>
1. 리스트를 가지고 배열만들기

```py
# 1차원 배열
vec = np.array([1, 2, 3, 4, 5])
print(vec)
# 2차원 배열
mat = np.array([[10, 20, 30], [ 60, 70, 80]]) 
print(mat)

# 모든 값이 0인 2x3 배열 생성.
zero_mat = np.zeros((2,3))
print(zero_mat)

# 모든 값이 특정 상수인 배열 생성. 이 경우 7. 
same_value_mat = np.full((2,2), 7)  #np.full()은 배열에 사용자가 지정한 값을 삽입한다.
print(same_value_mat)

# 대각선 값이 1이고 나머지 값이 0인 2차원 배열을 생성.
eye_mat = np.eye(3)   #np.eye()는 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성 => 단위행열
print(eye_mat)

# 임의의 값으로 채워진 배열 생성
random_mat = np.random.random((2,2)) # 임의의 값으로 채워진 배열 생성
print(random_mat)

# 0부터 9까지
range_vec = np.arange(10) 
#np.arange(n)은 0부터 n-1까지의 값을 가지는 배열을 생성
print(range_vec)

# 1부터 9까지 +2씩 적용되는 범위
n = 2
range_n_step_vec = np.arange(1, 10, n) 
#np.arange(i, j, k)는 i부터 j-1까지 k씩 증가하는 배열을 생성
print(range_n_step_vec)
```

2. Numpy 연산

```py
x = np.array([1,2,3])
y = np.array([4,5,6])
# result = np.add(x, y)와 동일.
result = x + y
print(result)
#-> [5 7 9]

# result = np.subtract(x, y)와 동일.
result = x - y
print(result)
#-> [-3 -3 -3]

# result = np.multiply(result, x)와 동일.
result = result * x
print(result)
#-> [-3 -6 -9]

# result = np.divide(result, x)와 동일.
result = result / x
print(result)
#-> [-3. -3. -3.]

#Numpy에서 벡터와 행렬곱 또는 행렬곱을 위해서는 dot()을 사용
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
mat3 = np.dot(mat1, mat2)
print(mat3)
#-> [[19 22]
#   [43 50]]
```

<br><br><br><br>

### 구체적인 환경데이터 자동화 구현 방법

---

```py
from openpyxl import load_workbook #엑셀 파일 열기
import pandas as pd

# 해당이름의 csv파일을 읽어옴
r_csv = pd.read_csv("C:/Users/user/OneDrive/바탕 화면/data/feeds.csv")
```

```py
week = (int(input("몇주차 자료입니까? =>")))
start_date = str(input("시작하고자 하는 날짜를 입력해주세요. => "))
start_day = start_date.split("-")
start_day1=int(start_day[2])
start_day2=("{:02d}".format(start_day1))
print(start_day2)
start_day3=int(start_day2)
rd_csv= r_csv[r_csv['created_at']> '{}'.format(start_date)].copy()
rd_csv['Date'] = pd.to_datetime(rd_csv['created_at']).dt.normalize()
```
시작하고자 하는 날짜를 받아서 날짜를 int화 시키고 
입력한 날짜 이후로의 데이터만 추출해낸다.


```py
# 저장할 xlsx파일의 이름을 정함
# save_xlsx = pd.read_excel("C:/Users/codka/OneDrive/바탕 화면/data/feeds.xlsx")
# r_csv.to_excel(save_xlsx, index = False) # xlsx 파일로 변환
# save_xlsx.save() #xlsx 파일로 저장
```
이부분은 굳이 csv파일을 xlsx로 전환하지 않아도 되기 때문에 제외시켰다.
```py
wb = load_workbook("C:/Users/user/OneDrive/바탕 화면/data/원예작물재배및실습_11주차_4조_형식자료.xlsx")
ws = wb.active
# print(ws.max_row) 맨 마지막 행 번호를 출력해서 확인하는 용
for i in range(2,ws.max_row+1):
    ws.cell(i,1).value = None
    ws.cell(i,2).value = None
    ws.cell(i,3).value = None
    ws.cell(i,4).value = None
    ws.cell(i,5).value = None
    ws.cell(i,7).value = None
    ws.cell(i,8).value = None
    ws.cell(i,9).value = None
```
그래프 양식을 참고할 엑셀파일을 불러오고 그 안에 있는 기존 환경 데이터를 삭제시켜준다.
```py
line = 0
for i, row in rd_csv.iterrows():
    ws.cell(line+2,1).value = row['created_at']
    ws.cell(line+2,2).value = row['entry_id']
    ws.cell(line+2,3).value = row['field1']
    ws.cell(line+2,4).value = row['field2']
    ws.cell(line+2,5).value = row['field3']
    ws.cell(line+2,7).value = "=LEFT(A{}, 10)".format(line+2)
    ws.cell(line + 2, 8).value = "=0.61078*EXP(C{}/(C{}+233.3)*17.2694)".format(line + 2, line + 2)
    ws.cell(line + 2, 9).value = "=H{}*(1-D{}/100)".format(line + 2, line + 2)
    line +=1
```
센서로 실시간 인식된 환경 데이터가 저장되어 있는 csv파일에서 필요한 날짜의 데이터만 뽑아서 참고 엑셀파일의 해당 열에 값을 넣어준다.
또한 SVP와 VPD의 계산식만 입력해주면 계산된 결과값이 자동으로 입력된다.
```py
for i in range(7):
    ws.cell(3+i,11).value = "2022-06-{}".format(start_day3+i)
    date = "2022-06-{}".format(start_day3+i)
    ws.cell(3 + i, 12).value = rd_csv[rd_csv['Date'] == date].max()["field1"]
    ws.cell(3 + i, 14).value = rd_csv[rd_csv['Date'] == date].min()["field1"]
    ws.cell(3 + i, 15).value = rd_csv[rd_csv['Date'] == date].max()["field2"]
    ws.cell(3 + i, 17).value = rd_csv[rd_csv['Date'] == date].min()["field2"]
    ws.cell(3 + i, 18).value = rd_csv[rd_csv['Date'] == date].max()["field3"]
    ws.cell(3 + i, 20).value = rd_csv[rd_csv['Date'] == date].min()["field3"]
    # ws.cell(3+i,12).value = "=MAXIFS(C:C,G:G,K{})".format(3+i)
    ws.cell(3+i,13).value = "=AVERAGEIFS(C:C,G:G,K{})".format(3+i)
    # ws.cell(3+i,14).value = "=MINIFS(C:C,G:G,K{})".format(3+i)
    # ws.cell(3+i,15).value = "=MAXIFS(D:D,G:G,K{})".format(3+i)
    ws.cell(3+i,16).value = "=AVERAGEIFS(D:D,G:G,K{})".format(3+i)
    # ws.cell(3+i,17).value = "=MINIFS(D:D,G:G,K{})".format(3+i)
    # ws.cell(3+i,18).value = "=MAXIFS(E:E,G:G,K{})".format(3+i)
    ws.cell(3+i,19).value = "=AVERAGEIFS(E:E,G:G,K{})".format(3+i)
    # ws.cell(3+i,20).value = "=MINIFS  (E:E,G:G,K{})".format(3+i)
    ws.cell(3+i,22).value = "=(S{} * 0.023 * 60 * 60 * 24) / 1000000".format(3+i)  #DLI

    for i in range(6):
    ws.cell(3,23).value=""
    ws.cell(4+i,23).value = "=W{}-4.4+M{}".format(3+i, 4+i)    #GDD
```
반복문을 만들어 7일간의 환경데이터 표를 만들 수 있다.
엑셀에는 MAXIFS와 MINIFS가 있지만 Python의 OpenPyXL에서는 해당 함수가 현시점까지 도입되지 않았기 때문에 날짜 조건을 잡아준 후 max 또는 min을 이용해 계산해주었다.

```py
wb.save('C:/Users/user/OneDrive/바탕 화면/data/원예작물재배및실습_{}주차_4조_final.xlsx'.format(week))
```
이렇게 계산이 완료된 엑셀파일을 저장해주면 괄호에 넣은 경로와 이름으로 새로 저장된다.



<br><br><br><br>

### 느낀점과 아쉬운점😊

---
OpenPyXL과 Pandas를 이용해서 환경 데이터를 정리해보니, 이젠 정말 엑셀만 다룰 줄 아는 사람은 뒤쳐지겠구나... 라는 생각이 들었다.

다른 직장동료들은 Python을 이용해 엑셀 자동화를 시켜 빠르게 빠르게 일을 처리하는데...

물론 이번 프로젝트를 진행하면서 비교적 짧은 코드를 였어도 자동화를 구현해내는데 엄청난 노력과 시간이 들었다.
짧은 코드를 작성하지만 그 코드를 작성해내기 위해선 해당 라이브러리에 대해 확실한 이해가 필요했다. 왜 그 코드를 쓰는지, 그 코드를 쓰면 어떤 변화가 일어나는지 알고리즘을 이해하는데 시간을 충분히 들이고자 노력했다.
하지만 이런식의 업무가 처음엔 익숙하지 않아 많은 시간이 걸리겠지만 익숙해지면 정말 많은 시간을 절약할 수 있다는 것을 활동 내내 느꼈다.

이번 프로젝트를 통해 배우게 된 총 3가지의 라이브러리는 일상에 혹은 사무에 매우 도움이 되는 라이브러리 인것 같다. 앞으로 엑셀 파일로 데이터 정리를 하게 될때 Python을 이용해서 정리해보는 연습을 계속 하게 된다면 내가 취직을 할 때쯤 익숙해지지 않을까? 감히 생각해본다.
연습만이 살길이다...!! 아자아자


새로운 데이터를 불러와서 계산 및 정리 후 엑셀파일의 형태로 저장하는것은 성공했지만, 시간 관계상 그 데이터를 한글 보고서 형태로 정리하지 못한것이 좀 아쉽다.
엑셀파일의 형태로도 데이터는 쉽게 분석될 수 있지만. 엑셀에서는 데이터에 대한 설명을 하지 못한다.

한글 파일에서 보고서 형태로 데이터를 정리해 놓으면 그러한 데이터가 왜 나왔는지. 이러한 데이터가 어떤 의미를 가지는지에 대해서 설명할 수 있기때문에 읽은 사람에게로 하여금 이해하기 쉽게 풀어쓸  수 있다. 시간이 된다면 프로젝트 이후에 Python으로 한글파일 보고서를 쓰는 활동을 추가적으로 해보고싶다.
<br><br><br><br>
## <2. 원예실습 환경 데이터 자동화 구현>

---

### 주제를 선정하게 된 이유

실용적인 측면을 강조한 엑셀 자동화 프로그래밍으로 주제를 결정했지만 친구들의 반응도 중요한 이번 기말 프로젝트에서 발표하기엔 퍼포먼스적인 요소가 부족한 것 같았다. 그래서 시각적인 효과를 보여줄 수 있는 프로그램을 만들면 좋을 것 같았고 그동안 궁금했었던 Pygame 패키지를 이용해 ‘틀린그림찾기’게임을 만들기로 결정하게 되었다.
<br><br>

### ➰*Pygame* 라이브러리
---
#### Pygame이란?
![Pygame Image](https://camo.githubusercontent.com/1971c0a4f776fb5351c765c37e59630c83cabd52/68747470733a2f2f7777772e707967616d652e6f72672f696d616765732f6c6f676f2e706e67)
Python으로 작성 가능한 게임 등의 멀티미디어 표현을 위한 라이브러리이고 SDL 기반이다. 

오픈 소스이자 무료 도구이며, Python을 돌릴 수 있는 플랫폼이라면 어디서든 실행할 수 있다. 게임 개발 도구이지만 이미지 프로세스 또는 조이스틱 입력, 음악 재생 등의 기능만 떼어다 쓸 수도 있다.
[출처 Cliclk](https://namu.wiki/w/Pygame)
공식사이트에서 더욱 많은 정보들을 확인해볼 수 있다.
[Pygame 공식사이트](https://www.pygame.org/news)

<br><br><br><br>

### 구체적인 환경데이터 자동화 구현 방법

---

pygame 라이브러리를 사용해서 게임을 만들고자 코드의 알고리즘을 생각해보았다.

1. pygame 시작 선언
2. 게임 윈도우(창) 설정 - 프레임, 컬러, 크기 등등
3. 게임에서 실행될 오브젝트 설정 및 게임루프에서 실행될 이벤트(함수) 설정
4. 게임 루프 설정 (게임이 진행되는 동안 실행되는 루프 및 게임종료 설정)

이 구조를 따라서 코드를 작성하였다. 
1. pygame 시작 선언

```py
# pygame 선언
import pygame
import sys

# pygame 초기화(init)
pygame.init()
```

2. 게임 윈도우(창) 설정

```py
# pygame 게임창 옵션 설정
size = [1400, 800]
screen = pygame.display.set_mode(size)

title = "game"
pygame.display.set_caption(title)
```

3. 게임에서 실행될 오브젝트 설정 및 게임루프에서 실행될 이벤트(함수) 설정

```py
# 게임내 필요한 설정
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font("fonts/Galmuri11.ttf", 30)
font2 = pygame.font.Font("fonts/Galmuri11.ttf", 50)
pygame.mouse.set_visible(False)
yesImg = pygame.image.load("image/yes.png")
noImg = pygame.image.load("image/no.png")
pygame.transform.scale(yesImg, (90, 130))
pygame.transform.scale(noImg, (90, 130))
mySound = pygame.mixer.Sound("bgm/answer.wav")
wr_sound = pygame.mixer.Sound("bgm/worng.wav")
compl = pygame.mixer.Sound("bgm/clear.wav")
loser = pygame.mixer.Sound("bgm/lose.mp3")
cong = pygame.mixer.Sound("bgm/yeah.mp3")
mySound.set_volume(1.0)
wr_sound.set_volume(1.0)
```

RGB를 설정해서 색을 설정하고, 폰트설정, 이미지 설정, 소리 설정 등 객체를 지정해서 하였다.

```py
# 코드에서 사용할 이미지 불러오는 클래스( 로드 ,사이즈, 위치) 지정
class Obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sx = 0
        self.sy = 0
        self.img = None

    def put_img(self, address):
        if address[-3] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))
```

‘틀린그림찾기’ 게임이다보니 이미지를 자주 불러 와야해서 이미지를 불러오는 클래스를 만들었다.
위에서부터 매소드를 설명하자면 이미지를 불러오는 메소드, 사이즈를 설정하는 메소드, 위치를 지정해서 출력하는 매소드이다. 

```py
pb2 = Obj()
pb2.put_img("image/pb2.png")
pb2.change_size(1200, 620)
pb2.x = round(size[0] / 2 - pb.sx / 2)
pb2.y = round(size[1] - pb.sy + 40)

pb4 = Obj()
pb4.put_img("image/pb3-removebg-preview.png")
pb4.change_size(1200, 700)
pb4.x = round(size[0] / 2 - pb.sx / 2)
pb4.y = round(size[1] - pb.sy - 5)
```
클래스를 사용해서 간단하게 이미지를 불러왔다

이 클래스를 만드는 것은 유튜브 영상(초보코딩)을 참고 하였다.

[초보코딩 링크]("https://www.youtube.com/watch?v=9oIkFAZM7DY")


그 외에 전체적인 게임 이벤트가 마우스 클릭으로 발생하기 때문에
 마우스 클릭 값을 좌표로 나타내주는 pygame.mouse.get_pos() 함수와 마우스 클릭 이벤트를 받을 수 있는 pygame.MOUSEBUTTONUP 함수를 사용하여 게임 루프를 만들었다. 
```py
   for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                p = pygame.mouse.get_pos()
                if 314 - 40 <= p[0] <= 314 + 40 and 570 - 40 <= p[1] <= 570 + 40 or 873 - 40 <= p[
                    0] <= 873 + 40 and 570 - 40 <= p[1] <= 570 + 40:
                    mySound.play()
                    cr = Obj()
                    cr.put_img("image/123.png")
                    cr.change_size(80, 80)
                    cr.x = 274
                    cr.y = 530
                    cr.show()

                    cr2 = Obj()
                    cr2.put_img("image/123.png")
                    cr2.change_size(80, 80)
                    cr2.x = 833
                    cr2.y = 530
                    cr2.show()
```


게임 이벤트 중 마우스를 클릭한 곳의 좌표값이 지정되고 만약 클릭한 곳이 그 좌표가 설정(정답) 범위 안에 있으면 효과음이 출력되는 동시에 동그라미 이미지가 출력되는(클래스) 코드이다. 

또한 텍스트를 따로따로 불러 오는 것도 번거로워서 함수를 따로 설정하였다. 

```py
def draw_text(font_name, text, size, color, x, y):
    ft = pygame.font.Font(font_name, size)
    text_surface = ft.render(text, True, color)
    text_rect = (x, y)
    screen.blit(text_surface, text_rect)
```
폰트파일, 출력할 글자, 크기, 색상, 좌표값을 입력하면 한번에 글자가 화면에 출력되는 함수이다. 


틀린그림찾기 게임의 전체적인 진행 흐름이 틀린 부분을 찾아서 맞추고 다음 스테이지로 넘어가는 것이 반복 되기 때문에 앞서 설명한 코드들로 하나의 스테이지를 먼저 만들고 그 구조를 그대로 약간 변형 시켜서 다음 스테이지를 만드는 방식으로 진행하였다. 


<br><br><br><br>

### 느낀점과 아쉬운점😂

---

우선 느낀점은 하나의 효과를 나타나게 하는 것도 많은 시간이 노력이 들었던 것에서 프로그래밍이 쉽지 않다는 것을 여실히 느꼈다... 그저 게임을 플레이하는 입장에서는 쉬워보였던 것이 만들 때는 계속 오류가 나고... 원하던 대로 실행이 안됬었다.. 처음에 틀린그림찾기도 다른 게임들보다는 보여지는 이펙트가 덜 해서 쉬울 것이라고 생각했지만.. 쉽지 않았다... 코드가 1000줄이 넘어갔다..
코드를 짤 때도 그냥 코드를 입력하면 화면에 계속 출력 될 것이라고 생각했지만 
1초에 몇 번에 화면에 계속 새로 그리는 원리로 게임화면이 출력 되고 있어서 코드를 짤 때 
출력될 순서를 고려해서 짜야하는 부분도 굉장히 어려웠다..
하지만 직접 프로그램 하나를 만들고 나니 파이썬에 대해서 조금은..이해가 갈 것 같기도 하다.. 
아쉬웠던 점은 시간상 코드를 축약을 못했다는 것이다. 마우스 클릭에서 좌표를 받아 정답 처리하는 부분이 전부 다 같은 형식이라 반복되는 부분이 굉장히 많다...체감상 한 300줄이상은 되는 것 같다.. 함수를 만들려고 했지만 괜히 잘못짜서 오류가 발생하면 방대한 범위를 수정하기가 매우 겁났다.. 그래서 코드를 집약적으로 쓰지 못한 점이 매우 아쉬웠다..
그리고 플레이 할 때 마다 점수를 저장되게 해서 첫 번째 플레이는 몇 점, 두 번째 플레이는 몇 점, 이런 식으로 볼 수 있게 하고 싶었지만..이것 역시 시간상..하지 못한 것이 아쉬웠다.
<br><br>
확실히 게임을 만드는 프로젝트였기 때문에 시각적 효과도 매우 중요하다고 생각했다. 그 어떤 글자라도 허투루 쓸 수 없었고, 뭔가 그냥 맹짜로 쓰기에는 심심했다. 뭔가 더 예!쁘!게! 꾸미고 싶었다. 글씨색을 예쁜걸로 바꾸고 싶었고, 예쁜 그림을 넣고 싶었고, 글자를 깜빡이는 효과도 주고싶었다...
하지만 무얼 원하든, 생각보다 내가 원하는데로 구현해내는게 정말 어려웠다. 글자 깜빡이는효과도 장장 3-4시간은 걸린듯 싶다. 하지만 확실히 노력해서 조금이라도 데코를 하니. 그 효과는 예상보다 더 큰 만족으로 다가왔다.
Pygame으로 구현해낼 수 있는 효과는 매우 방대하지만 이번 프로젝트에서 그 재미있고 신박한 효과들을 사용하지 못한점이 아쉬움점으로 남는다... 그리고 게임 클리어 창에서 움직이는 사진(gif)를 간절하게 넣고 싶었지만 pygame에서는 gif를 취급하지 못한다고 한다... 연속된 시간으로 있는 여러 사진을 불러와 for문을 이용하여 gif형태로 나타낼 수는 있었지만, 시간상... 하하 아쉽다..
다음에는 너구리, 테트리스, 날아오는 물체 피하기 등등 한번 더 pygame에 대해 배워볼 수 있는 시간이 있었으면 좋겠다. 

그리고 마지막으로, 정말 이번 프로젝트 우여곡절 힘들었고.. 스트레스도 정말 많이 받았지만
인내심과 프로그래밍 능력을 키울 수 있는 기회를 주신 김태곤 교수님께 감사의 말씀 남긴다..

그리고 이 프로젝트를 진행하면서 들었던 얘기 중 가장 기억에 남는 말이다.

*"그걸 언제 하나하나 배우면서 구현하고 있어. 너가 필요한 부분의 코드만 발췌해서 쓰는거지..
개발자들도 다 아는거 아니야. 다들 필요한 코드 배워서 갔다 쓰는거지"*

기말 프로젝트를 다 마치고나니.. 저 말씀이 백번 맞는 말이다...
더 잘할 수 있었는데.. 여운이 남는다.
