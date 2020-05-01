import matplotlib.pyplot as plt
import numpy as np
from Db.DbHandler import dbHandler

db = dbHandler.getInstance()


def get_data():
    print('creating graph')
    salesPerMonth = "SELECT strftime('%m/%Y',DATE(InvoiceDate)) as date, count(total) as total_sales from invoices group by strftime('%m/%Y',DATE(InvoiceDate))"
    activeCustomersPerMonth = "SELECT distinct strftime('%m/%Y',DATE(InvoiceDate))as date, count (CustomerId)as active_customers from invoices where total>0 GROUP by strftime('%m/%Y',DATE(InvoiceDate))"
    query1 = db.select(salesPerMonth)
    query2 = db.select(activeCustomersPerMonth)
    dates = []
    sales = []
    active_customers = []

    for row in query1:
        dates.append(row[0])
        sales.append(row[1])
    for row in query2:
        active_customers.append(row[1])

    create_graph(dates, sales, active_customers)


def create_graph(label, val1, val2):
    x = np.arange(len(label))
    width = 0.30
    fig, ax = plt.subplots()
    ax.bar(x - width/2, val1, width, label='sales', color='aquamarine')
    ax.bar(x + width/2, val2, width, label='active_customers', color='mediumpurple')
    ax.legend(bbox_to_anchor=(1.0, 1.2))
    plt.xticks([r for r in range(len(label))], label, rotation=90)
    fig.tight_layout()
    plt.title('Total sales and active customer per month')
    plt.show()
