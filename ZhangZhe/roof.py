print("Отправить тебя в гулаг")
f = open("roof.csv","r")
data = f.read()
rows = data.split('\n')
print(rows[2:3])
final_data = []
for row in rows:
    split_list = row.split(',')
    final_data.append(split_list)
print(final_data[2][3])
