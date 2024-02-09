
print("\n                                           >>> HOMEWORK <<<")
print("\nTask-2")
File = open("BANK.txt", mode='r')
List = []
List2 = []
Dict = {}
File_read = File.readlines()
for lines in File_read:
    List2.append(lines)
    for digits in lines.split(" "):
        if digits.isdigit():
            List.append(digits)
            Set = set(List)
            List.clear()
            List = list(Set)
            List.sort(reverse=True)


for newlines in List2:
    if List[0] in newlines:
        Dict["1 - ENG QIMMAT SOTIB OLISH"] = newlines
    if List[1] in newlines:
        Dict["2 - ENG QIMMAT SOTIB OLISH"] = newlines
    if List[2] in newlines:
        Dict["3 - ENG QIMMAT SOTIB OLISH"] = newlines
print(Dict)

Dict.clear()
List.reverse()
for newlines in List2:
    if List[0] in newlines:
        Dict["1 - ENG ARZON SOTIB OLISH"] = newlines
    if List[1] in newlines:
        Dict["2 - ENG ARZON SOTIB OLISH"] = newlines
    if List[2] in newlines:
        Dict["3 - ENG ARZON SOTIB OLISH"] = newlines
print(Dict)
File.close()











