def prettify(json_text):
    tabs = [0]
    text = ''
    index = 0
    while index < len(json_text):
        if index < len(json_text)-1:
            if (json_text[index] == '{' or json_text[index] == '[') and json_text[index-1] != "'":
                text += f'{json_text[index]}£'
                tabs.append(tabs[-1]+1)
            elif json_text[index] == ',':
                text += ',£'
                if json_text[index+1] == ' ':
                    index += 1
                tabs.append(tabs[-1])
            elif (json_text[index] == '}' or json_text[index] == ']') and json_text[index+1] != "'":
                if json_text[index+1] == ',':
                    text += f'£{json_text[index]},£'
                    tabs.append(tabs[-1]-1)
                    tabs.append(tabs[-1])
                    index += 1
                    if json_text[index+1] == ' ':
                        index += 1
                else:
                    text += f'£{json_text[index]}'
                    tabs.append(tabs[-1]-1)
            else:
                text += f'{json_text[index]}'
        index += 1

    new = text.split('£')
    for index, word in enumerate(new):
        print("    "*tabs[index]+word)
    print('}')

mytext = open("json_text.txt")
prettify(mytext.readline())
mytext.close()


