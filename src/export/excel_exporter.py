from openpyxl import Workbook

def export_to_excel(data):
    wb = Workbook()
    ws = wb.active

    ws.append(["Source URL", "Text", "Link"])

    for item in data:
        ws.append([
            item["source_url"],
            item["text"],
            item["link"]
        ])

    wb.save("output.xlsx")
