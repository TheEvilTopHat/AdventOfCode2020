def get_answers():
    answers = []
    with open("input.txt", "r") as f:
        people = 0
        group = ""
        while True:
            line = f.readline()
            if line:
                if line == "\n":
                    answers.append((people,group))
                    people = 0
                    group = ""
                    continue
                line = line.replace("\n","")
                line = line.strip()
                #validation of correct answers not required
                #a = ""
                #for char in line:
                #    if char in "abcxyz":
                #        a += char
                group += line
                people += 1
            else:
                answers.append((people,group))
                break
    return answers

def sum_counts(answers):
    sum = 0
    for group in answers:
        s = set(group[1])
        sum += len(s)
    return sum

def sum_counts_for_full_group(answers):
    sum = 0
    for group in answers:
        for char in set(group[1]):
            if group[1].count(char) == group[0]:
                sum += 1
    return sum

if __name__ == "__main__":
    answers = get_answers()
    print("SUM OF ANSWERS", sum_counts(answers))
    print("SUM OF ANSWERS FOR FULL GROUP", sum_counts_for_full_group(answers))
