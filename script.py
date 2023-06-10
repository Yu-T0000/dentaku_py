import re

def is_number(value):   #数字かチェック
    pattern = r'^[-+]?[0-9]+(\.[0-9]+)?$'   #正規表現パターン！ .を単なる文字として扱うために\でエスケープするらしい
    return re.match(pattern, value) is not None #パターン一致でre.matchオブジェクトとやらが返る 何も返らなかったらFalse
def is_op(value):
    pattern = r'^[+-/*]+$'  #演算子かのチェック これで合ってるのか？
    return re.match(pattern, value) is not None
def f(data):
    formatted_numbers = [f"{num:.0f}" if num.is_integer() else str(num) for num in data]
    for formatted_num in formatted_numbers:
        print(formatted_num,end = " ")
    print("")

def calc(op,num_a,num_b):
    if op == "+":
        return num_a + num_b
    elif op == "-":
        return num_a - num_b
    elif op == "/":
        return round(num_a / num_b, 3)
    elif op == "*":
        return round(num_a * num_b, 3)


input_data = []
fdata_list = [f"{num:.0f}" if num.is_integer() else str(num) for num in input_data]
data_index = len(input_data)-1
guide = ["\n数値を入力(Xで終了)：", "\n数値または演算子を入力(Xで終了・Cでクリア)："]
guide_index = 0
input_val, op, answer = 0,"",0

while True:

    input_val = input(guide[guide_index])

    if input_val == "X" or input_val == "x":    #終了
        break
    elif input_val == "C" or input_val == "c":  #初期化
        input_data = list()
        guide_index = 0
        print(f"\n入力値がリセットされました！すっきり！")

    if is_number(input_val):
        input_data.append(float(input_val))
        print("\nこれまでの入力値：", end = " ")
        f(input_data)
        guide_index = 1

    elif is_op(input_val) and guide_index == 1:
        while input_val != "":
            op = input_val
            input_val = input(f"\n計算式：{input_data[data_index]} {op} ")
            while not is_number(input_val):
                print("\n「数値」を入力してください！")
                input_val = input(f"\n計算式：{input_data[data_index]} {op} ")
            input_data.append(float(input_val))
            answer = calc(op,input_data[data_index-1],input_data[data_index])
            input_val = input(f"{answer} ")
            if is_op(input_val):
                input_data.append(answer)
            else:
                input_data.append(answer)
                if is_number(input_val):
                    input_data.append(float(input_val))
                print("\nこれまでの入力値：", end = " ")
                f(input_data)
                guide_index = 1
                break



    elif guide_index == 0:
        print("\n「数値」を入力してください！")
        continue

    else:
        print("\n「数値」をまたは「演算子」を入力してください！")



print("\n終了します\n")
