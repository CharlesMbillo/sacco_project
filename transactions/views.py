from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction

def index(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    else:
        form = TransactionForm()
    return render(request, 'index.html', {'form': form})

def transaction_summary(request):
    transactions = Transaction.objects.all()
    return render(request, 'summary_template.html', {'transactions': transactions})

# This view will display transactions in a web page using an HTML table#

from django.shortcuts import render
from .models import Transaction

def transaction_html(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions_html.html', {'transactions': transactions})

# This view will generate a CSV file for download containing the transaction data.#

import csv
from django.http import HttpResponse
from .models import Transaction

def transaction_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Member ID', 'Transaction Type', 'Face Amount', 'Transaction Date'])

    transactions = Transaction.objects.all()
    for transaction in transactions:
        writer.writerow([transaction.member_id, transaction.transaction_type, transaction.face_amount, transaction.transaction_date])

    return response


# This view will generate a PDF report of transactions using ReportLab.#
 
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Transaction

def transaction_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'

    p = canvas.Canvas(response)
    transactions = Transaction.objects.all()
    y = 800
    p.drawString(100, y, "Transaction Report")
    y -= 40

    for transaction in transactions:
        p.drawString(100, y, f"Member ID: {transaction.member_id}, Type: {transaction.transaction_type}, Amount: {transaction.face_amount}, Date: {transaction.transaction_date}")
        y -= 20

    p.showPage()
    p.save()
    return response

# views.py
from django.shortcuts import render

def summary_view(request):
    # Your view logic here
    return render(request, 'summary_template.html')

def success(request):
    return render(request, 'success.html')
