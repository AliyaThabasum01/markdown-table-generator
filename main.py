from generator import csv_to_markdown

print("=" * 50)
print("📋 Markdown Table Generator")
print("=" * 50)

input_file = input("Enter CSV file name (e.g. sample.csv): ")

try:
    output = csv_to_markdown(input_file)

    with open("output.md", "w", encoding="utf-8") as file:
        file.write(output)

    print("\n✅ Markdown table saved as output.md")

except Exception as e:
    print("\n❌ Error:", e)
