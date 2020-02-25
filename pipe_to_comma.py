import sys
def make_this_crap_a_list(filename):
    file = open(filename, 'r')
    full_text = file.read()
    file.close()
    full_text = full_text.split("\n")
    #horizon_dict = {}
    for z in range(len(full_text)):
        full_text[z] = full_text[z].split('|')
        for g in range(len(full_text[z])):
            full_text[z][g] = full_text[z][g].strip('"')
    #if len(full_text[z]) == 4: 
    #    horizon_dict[full_text[z][3]] = full_text[0:3]
    return full_text
#print(len(full_text))
#print(len(horizon_dict))

def arr_csv(arr,filename="out.csv"):
    file = open(filename,'w')
    text_to_write = ""
    for z in arr:
        for g in z:
            #print(g)
            text_to_write += g
            text_to_write += ","
        text_to_write += "\n"
    file.write(text_to_write)
    file.close()


def pipe_delimited_to_csv(filename):
    arr_csv(make_this_crap_a_list(filename+".txt"),filename+".csv")


if __name__ == "__main__":
    #print(sys.argv)
    #try:
        filename = sys.argv[1]
        filename = filename.split(".")
        filename = filename[0]
        pipe_delimited_to_csv(filename)
        print("CSV created with name " + filename + ".csv")
