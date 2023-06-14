# -*- coding: utf-8 -*-
import re
import statistics

def is_number(value):   #数字かチェック
    pattern = r'^[-+]?[0-9]+(\.[0-9]+)?$'   #正規表現パターン！ .を単なる文字として扱うために\でエスケープするらしい
    return re.match(pattern, value) is not None #パターン一致でre.matchオブジェクトとやらが返る 何も返らなかったらFalse
def is_op(value):
    pattern = r'^[+-/*]?$'  #演算子かのチェック これで合ってるのか？
    return re.match(pattern, value) is not None
    
def is_stat(value):
    if value == "Avg" or "Med" or "sum":
        return True
    else:
        return False

def f(data):    #フォーマット
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


def extra(input,values):
    if input == "Avg":
        return round(sum(values)/len(values),3), "平均値："
    elif input == "Med":
        return round(statistics.median(values),3), "中央値："
    elif input == "sum":
        return sum(values), "合計："
    else:
        return None, ""  # 修正点：デフォルトの返り値を指定


input_data, ex_data = [], []
fdata_list = [f"{num:.0f}" if num.is_integer() else str(num) for num in input_data]
data_index = len(input_data)-1
guide = ["\n数値を入力(Xで終了)：", "\n数値または演算子を入力(Xで終了・Cでクリア)："]
guide_index = 0
input_val, op, answer = 0,"",0

print("簡易電卓です。")
print("次のコマンドで、これまで入力した数値の代表値の計算もできます！ 平均値：「Avg」 中央値：「Med」合計：「sum」")

while True:

    input_val = input(guide[guide_index])

    if input_val == "X" or input_val == "x":    #終了
        break
    elif input_val == "C" or input_val == "c":  #初期化
        input_data = list()
        guide_index = 0
        print(f"\n入力値がリセットされました！すっきり！")
        continue

    if is_number(input_val):    #入力されたのは数値か？
        input_data.append(float(input_val))
        print("\nこれまでの入力値：", end = " ")
        f(input_data)
        guide_index = 1
        
    elif guide_index == 1:
        if is_op(input_val): #前に数値が入力された状態で演算子が入力されたか？
            while input_val != "":
                op = input_val
                input_val = input(f"\n計算式：{input_data[data_index]} {op} ")
                #↓計算パート↓
                while not is_number(input_val):
                    print("\n「数値」を入力してください！")
                    input_val = input(f"\n計算式：{input_data[data_index]} {op} ")  #数値入力待ち
                input_data.append(float(input_val)) #入力値追加
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

        elif is_stat(input_val) and len(input_data) >= 2:
            stat = input_val
            answer, type = extra(stat, input_data)
            if answer is not None:
                print(f"\n{type} {answer}")
                ex_data.append(type + str(answer))
            else:
                print("「数値」「演算子」「代表値」を入力してください！")
                print("求められる代表値は平均値：「Avg」 中央値：「Med」合計：「sum」 です")
        

    elif guide_index == 0:  #入力されちゃ困る値を入力されたとき(初回)
        print("\n「数値」を入力してください！")
        continue




print("\n終了します\n")
