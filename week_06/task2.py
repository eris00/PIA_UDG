# Zadaci sa fajlovima - peti zadatak
with open("numbers.txt", "w") as f:
    lines = ["0xA\n", "22\n", "ABC\n", "0x3\n", "0xC\n", "121\n", "0xD\n", "0x17"]
    f.writelines(lines)
    f.close()

sum = 0

with open("numbers.txt") as file:
    line = file.read().split("\n")
    #print(line)
    for value in line:
        if value.startswith("0x"):
            hex_num = value
            dec_num = str(int(hex_num, 16))
            if dec_num.endswith("3"):
                sum += int(dec_num)

print("Suma hex brojeva u decimalnom zapisu je: ", sum)
