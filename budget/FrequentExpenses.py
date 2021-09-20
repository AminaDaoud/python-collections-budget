from . import Expense
import collections
import matplotlib.pyplot as plt
import os

scriptpath = os.path.realpath(__file__)
parent_path = os.path.dirname(scriptpath)
filepath = os.path.join(os.path.sep, os.path.dirname(parent_path),"data","spending_data.csv")


expenses = Expense.Expenses()
expenses.read_expenses(filepath)


spending_categories = []
for expense in expenses.list:
	spending_categories.append(expense.category)


spending_counter = collections.Counter(spending_categories)
top5 = spending_counter.most_common(5)


categories, count = zip(*top5)


fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title("# of purchases by category")

plt.show()
