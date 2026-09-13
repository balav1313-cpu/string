text = "Python is Fun.Learn it Well "
count = 0
sentence =""
for char in text:
    if char == ".":
        break
    sentence = sentence + char
for char in text:
    if char.lower() in "aeiou":
       count += 1
print("Vowel Count:",count)
if "." in text:
    print("Cleaned sentence: ",sentence.upper())
else:
    print("There is no cleaned sentence")
