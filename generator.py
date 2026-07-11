import csv


def csv_to_markdown(filename):
    with open(filename, newline="", encoding="utf-8") as file:
        reader = list(csv.reader(file))

    if not reader:
        return ""

    headers = reader[0]
    rows = reader[1:]

    markdown = ""

    markdown += "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in rows:
        markdown += "| " + " | ".join(row) + " |\n"

    return markdown
