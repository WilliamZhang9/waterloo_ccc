instructions = input()
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4','5','6','7','8','9']
note = ""
isNewInstruction = False
for i in range(0,len(instructions)):
    if instructions[i] in letters:
        if isNewInstruction:
            print(note)
            note = ""            
            isNewInstruction = False   
        note += instructions[i]
    elif instructions[i] == "+":
        note += " tighten "
    elif instructions[i] == "-":
        note += " loosen "
    elif instructions[i] in numbers:
        note += instructions[i]
        isNewInstruction = True

print(note)
