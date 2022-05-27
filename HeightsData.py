import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

# display the table
Heights = pd.read_csv(r"resource\Heights.csv")
display(Heights)

# display average and max heights
print("The average height of Class_1 is ", np.average(Heights.Class_1))
print("The average height of Class_2 is ", np.average(Heights.Class_2))
print("The tallest student of Class_1 has height ", np.max(Heights.Class_1))
print("The tallest student of Class_2 has height ", np.max(Heights.Class_2))

# display histogram
fig, (subplot1, subplot2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(15, 5))
subplot1.hist(Heights.Class_1)
subplot1.set_title("Class 1")
subplot1.set_xlabel("Height")
subplot1.set_ylabel("Frequency")
subplot2.hist(Heights.Class_2)
subplot2.set_title("Class 2")
subplot2.set_xlabel("Height")
subplot2.set_ylabel("Frequency")
# plt.show()

# display boxplot
data_to_plot = [Heights.Class_1, Heights.Class_2]
plt.boxplot(data_to_plot)
plt.xlabel("Classroom")
plt.ylabel("Height")
# plt.show()

# convert to excel file
# Heights = Heights.drop(columns=['Unnamed: 0'])
# Heights.to_excel(r"resource\modified.xlsx", index = False)
