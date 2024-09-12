from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(transaction_id, date, customer_name, items, total_amount, file_name="receipt.pdf"):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Payment Receipt")

    # Transaction ID and Date
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Transaction ID: {transaction_id}")
    c.drawString(50, height - 120, f"Date: {date}")

    # Customer Name
    c.drawString(50, height - 160, f"Customer Name: {customer_name}")

    # Line Items Header
    c.drawString(50, height - 200, "Item")
    c.drawString(300, height - 200, "Price")

    # Line Items
    y_position = height - 240
    for item, price in items.items():
        c.drawString(50, y_position, item)
        c.drawString(300, y_position, f"Rs.{price:.2f}")
        y_position -= 20

    # Total Amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_position - 20, f"Total Amount: Rs.{total_amount:.2f}")

    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(50, 50, "Thank you for your purchase!")
    
    c.save()

    print(f"Receipt created successfully: {file_name}")

# Example Usage
transaction_id = "1234567890"
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
customer_name = "Rishabh Tiwari"
items = {
    "HeadPhone": 1500.00,
    "Redmi 12 5g": 13499.00,
    "Keyboard": 999.00
}
total_amount = sum(items.values())

create_receipt(transaction_id, date, customer_name, items, total_amount)
