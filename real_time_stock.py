import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons
import pandas as pd
import datetime
import matplotlib.dates as mdates

# Generate Sample Data
dates = pd.date_range(start="2026-01-01", periods=30)
product_A = np.random.randint(100, 200, 30)
product_B = np.random.randint(80, 150, 30)

df = pd.DataFrame({
    "Date": dates,
    "Product A": product_A,
    "Product B": product_B
})

current_product = "Product A"

fig, ax = plt.subplots(figsize=(10,5))
plt.subplots_adjust(left=0.3)

line, = ax.plot(df["Date"], df[current_product], linewidth=2)

ax.set_title("Interactive Sales Dashboard", fontsize=14)
ax.set_xlabel("Date")
ax.set_ylabel("Sales")

# Format Date Axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.xticks(rotation=45)

# Radio Buttons
ax_radio = plt.axes([0.05, 0.6, 0.2, 0.2])
radio = RadioButtons(ax_radio, ("Product A", "Product B"))

def update_product(label):
    line.set_ydata(df[label])
    ax.relim()
    ax.autoscale_view()
    plt.draw()

radio.on_clicked(update_product)

# Real-time Update
def real_time_update(event):
    new_date = df["Date"].iloc[-1] + datetime.timedelta(days=1)
    
    new_A = np.random.randint(100, 200)
    new_B = np.random.randint(80, 150)

    df.loc[len(df)] = [new_date, new_A, new_B]

    selected_product = radio.value_selected
    line.set_xdata(df["Date"])
    line.set_ydata(df[selected_product])

    ax.relim()
    ax.autoscale_view()
    plt.draw()

ax_button = plt.axes([0.05, 0.4, 0.2, 0.1])
button = Button(ax_button, "Update Data")
button.on_clicked(real_time_update)

plt.show()