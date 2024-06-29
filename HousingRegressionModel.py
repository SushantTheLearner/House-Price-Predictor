import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def load_data(file_path):
    """Load the dataset from a text file."""
    data = pd.read_csv(file_path, sep=" ", header=None, names=["BHKs", "SquareFootage", "Price"])
    return data

#regression model

def create_model(data):
    """Create and train a linear regression model."""
    X = data[['BHKs', 'SquareFootage']]
    y = data['Price']
    model = LinearRegression()
    model.fit(X, y)
    return model


def predict_house_price():
    """Predict house price based on user input."""
    try:
        bhks = int(bhks_var.get())
        sqft = int(sqft_var.get())

        input_data = pd.DataFrame({'BHKs': [bhks], 'SquareFootage': [sqft]})
        predicted_price = model.predict(input_data)[0] / 100000  # Convert to lakhs

        price_var.set(f"₹{predicted_price:.2f} Lakhs")

        residuals = data['Price'] - model.predict(data[['BHKs', 'SquareFootage']])
        sse = np.sum(residuals ** 2)
        sse_var.set(f"SSE: {sse:.2f}")

        plot_results(model, data, residuals)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for BHKs and Square Footage.")


def plot_results(model, data, residuals):
    """Plot the actual and predicted prices."""
    y_pred = model.predict(data[['BHKs', 'SquareFootage']])

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # Plot BHKs vs Price
    axs[0].scatter(data['BHKs'], data['Price'], color='green')
    axs[0].plot(data['BHKs'], y_pred, color='red', label='Predicted Line')
    axs[0].set_xlabel('Number of BHKs')
    axs[0].set_ylabel('Price (INR)')
    axs[0].set_title('Number of BHKs vs Price')
    axs[0].legend()

    # Plot Square Footage vs Price
    axs[1].scatter(data['SquareFootage'], data['Price'], color='purple')
    axs[1].plot(data['SquareFootage'], y_pred, color='red', label='Predicted Line')
    axs[1].set_xlabel('Square Footage')
    axs[1].set_ylabel('Price (INR)')
    axs[1].set_title('Square Footage vs Price')
    axs[1].legend()

    plt.tight_layout()

    # Embed the plot into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10)


# Load data and train the model
file_path = 'DataByCompany.txt'
data = load_data(file_path)
model = create_model(data)

# Initialize the Tkinter GUI
app = Tk()
app.geometry("800x700")
app.title("House Price Predictor")
app.configure(bg="dodgerblue")

# GUI Elements
Label(app, text="House Price Predictor", font=("Helvetica", 16), bg="dodgerblue", fg="white").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

Label(app, text="Enter the number of BHKs:", bg="dodgerblue", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
bhks_var = StringVar()
Entry(app, textvariable=bhks_var).grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Enter the square footage:", bg="dodgerblue", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
sqft_var = StringVar()
Entry(app, textvariable=sqft_var).grid(row=2, column=1, padx=10, pady=5)

Button(app, text="Predict Price", command=predict_house_price, bg="green", fg="white").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

Label(app, text="Predicted Price:", bg="dodgerblue", fg="white").grid(row=4, column=0, padx=10, pady=5, sticky="e")
price_var = StringVar()
Label(app, textvariable=price_var, bg="dodgerblue", fg="white").grid(row=4, column=1, padx=10, pady=5)

Label(app, text="Sum of Squared Errors:", bg="dodgerblue", fg="white").grid(row=5, column=0, padx=10, pady=5, sticky="e")
sse_var = StringVar()
Label(app, textvariable=sse_var, bg="dodgerblue", fg="white").grid(row=5, column=1, padx=10, pady=5)

app.mainloop()
