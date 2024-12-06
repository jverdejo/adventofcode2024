text = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def check_report(report):
    report_fail = False
    # check correctly ordered
    if sorted(report) != report and sorted(report, reverse=True) != report:
        report_fail = True

    # check increase
    if not report_fail:
        for i in range(len(report) - 1):
            diff = abs(int(report[i]) - int(report[i + 1]))
            # 0 diff or more than 3 is invalid
            if diff < 1 or diff > 3:
                report_fail = True
                break

    return not report_fail


safe_reports = 0
safe_report_tolerant = 0
for line in text.splitlines():
    # Get each number and convert to int
    report = [int(s) for s in line.split(" ")]
    # check normal report
    if check_report(report):
        safe_reports += 1
        safe_report_tolerant += 1
    else:
        # Create all sublist(removing one element) to check
        sublist = [report[:i] + report[i + 1:] for i in range(len(report))]
        for new_report in sublist:
            # if one sublist is valid, row it´s accepeted
            if check_report(new_report):
                safe_report_tolerant += 1
                break

print(f"Result part 1: {safe_reports}")
print(f"Result part 2: {safe_report_tolerant}")
