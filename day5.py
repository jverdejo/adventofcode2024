import re

text="""47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

regex_rules=r"((\d+)\|(\d+))"
updates_regex=r"(\d+(,\d+)+)"

rules={}
updates=[]

def sort(x,y):
    # check X
    rule_x=rules.get(x,None)
    if rule_x is not None and y in rule_x:
        return 1




#Get rules with regex
matches = re.findall(regex_rules, text)

for match in matches:
    _,x,y=match

    #Convert to int to simplify
    x=int(x)
    y=int(y)

    if x in rules:
        rules[x].append(y)
    else:
        rules[x]=[y]



#Get pages
matches = re.findall(updates_regex, text)

for match in matches:
    page,_=match
    #Convert to int to simplify
    updates.append([int(x) for x in page.split(",")])


updated_ok=list(updates)
updated_errors=[]
# go through each update
for update in updates:
    page_valid=True
    # go through each page
    for i,page in enumerate(update):
        # for each page, check nexts
        actual_rule=rules.get(page,None)
        if actual_rule is not None:
            for j in range(i+1,len(update)):
                if update[j] not in actual_rule:
                    updated_ok.remove(update)
                    updated_errors.append(update)
                    page_valid=False
                    break
            # Check the last it´s ok
            if i == len(update)-1 and page_valid:
                for j in range(len(update)-1):
                    if update[j] in actual_rule:
                        updated_ok.remove(update)
                        updated_errors.append(update)
                        break
        if not page_valid:
            break



# Gte miidle element and sum

total_part_1=sum([x[len(x) // 2] for x in updated_ok])

print(total_part_1)

#print(f"Result part 1: {total}")
#print(f"Result part 2: {total_part2}")
