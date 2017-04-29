# parses the file with the LDA output and adds it to the array bigrams

def parse(filename):
    with open(filename) as f:
        content = f.readlines()
        # print content

        first = False
        array = []
        for line in content:
            if line.find("====") != -1:
                # print line
                first = True
            elif first:
                 words = line.split()
                 # print line
                 if len(words[0]) > 2:
                    array.append(words[0])
                    first = False
        return array

print(parse("out.txt"))