
def short_words1(inp_list: list[str]) -> list[str]:
    """Filter out the shorter words"""
    ret_list: list[str] = []
    i = 0
    while i < len(inp_list):
        if len(inp_list[i]) < 5:
            ret_list.append(inp_list[i])
        else:
            print(f"{inp_list[i]} is too long!")
        i += 1
    return ret_list


    
my_words: list[str] = ["color", "oerkr", "er", "tyry", "df"]
print(short_words1(my_words))
#print(short_words(my_words))
