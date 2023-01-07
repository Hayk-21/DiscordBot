def change_permission(tag, name, flag):
    file = open("permission.py", "r", encoding="utf-8")
    text = ''
    i = 0
    # print(tag, name, flag)
    tag_founded = False
    for x in file:
        line = x.split(" ")
        # print(tag, line)
        if tag in line and not tag_founded:
            tag_founded = True
        # print(tag_founded, line)
        if tag_founded and ']\n' in line:
            tag_founded = False
            if flag == 'добавить':
                x = f"    '{name}',\n"+x
        # print(i, line, tag_founded)
        # print(flag, tag_founded, name in str(line))
        if flag == 'удалить' and tag_founded and name in str(line):
            continue
        text += x
        i += 1
    # print(text)
    file.close()
    file = open("permission.py", "w", encoding="utf-8")
    file.write(text)
    file.close()
# change_permission('channels', 'general', 'добавить')