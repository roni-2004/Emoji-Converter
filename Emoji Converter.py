from unittest import result


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ";)": "😏",
        ":|": "😐",
      
    }
    output = ""
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output


message = input("> ") 
result = emoji_converter(message)
print(result)