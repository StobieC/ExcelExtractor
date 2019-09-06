import pandas as pd

filePathRead = input("Enter Excel file path / ファイルアドレスを入力してください ")
sheetName = input("Enter sheet name / シート名を入力してください")
column = input("Enter column name / 一行名を入力してください")

print("Creating file...")

data = pd.read_excel(filePathRead, sheet_name=sheetName)
df = pd.DataFrame(data, columns=[column])

editedFile = open("Keys.xml", "w")

for i in df.itertuples():
    editedFile.write("<string name=\"" + str(i[1]) + "\" translatable=\"false\">"+str(i[1])+"</string>\n")
