def emoji_converter(message):
    words = message.split(' ') # split() splits the string based on the condition given in brackets, condition is space in this case
    output = ''
    emojis = {
        ":)" : "🙂",
        ":(" : "😞",
        ":D" : "😀",
        "xD" : "😆",
        ":O" : "😯"
    }

    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
print(emoji_converter(message))