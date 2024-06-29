import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def read_data(file_path):
    """Read dataset from a file."""
    df = pd.read_csv(file_path, sep=" ", header=None, names=["BHKs", "SquareFootage", "Price"])
    return df

# Function to build and train the regression model
def build_model(df):
    """Create and fit a linear regression model."""
    features = df[['BHKs', 'SquareFootage']]
    target = df['Price']
    reg_model = LinearRegression()
    reg_model.fit(features, target)
    return reg_model

def predict_price():
    """Make a house price prediction based on user input."""
    try:
        num_bhks = int(bhks_var.get())
        area_sqft = int(sqft_var.get())

        user_input = pd.DataFrame({'BHKs': [num_bhks], 'SquareFootage': [area_sqft]})
        estimated_price = reg_model.predict(user_input)[0] / 100000  # Convert to lakhs

        price_var.set(f"₹{estimated_price:.2f} Lakhs")

        residuals = df['Price'] - reg_model.predict(df[['BHKs', 'SquareFootage']])
        sse = np.sum(residuals ** 2)
        sse_var.set(f"SSE: {sse:.2f}")

        display_results(reg_model, df, residuals)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for BHKs and Square Footage.")

def display_results(model, df, residuals):
    """Plot the actual vs predicted prices."""
    predictions = model.predict(df[['BHKs', 'SquareFootage']])

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    # BHKs vs Price plot
    axs[0].scatter(df['BHKs'], df['Price'], color='green')
    axs[0].plot(df['BHKs'], predictions, color='red', label='Prediction')
    axs[0].set_xlabel('Number of BHKs')
    axs[0].set_ylabel('Price (INR)')
    axs[0].set_title('BHKs vs Price')
    axs[0].legend()

    # Square Footage vs Price plot
    axs[1].scatter(df['SquareFootage'], df['Price'], color='purple')
    axs[1].plot(df['SquareFootage'], predictions, color='red', label='Prediction')
    axs[1].set_xlabel('Square Footage')
    axs[1].set_ylabel('Price (INR)')
    axs[1].set_title('Square Footage vs Price')
    axs[1].legend()

    plt.tight_layout()

    # Embed the plot into the Tkinter GUI
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10)

# Load data and train the model
file_path = 'DataByCompany.txt'
df = read_data(file_path)
reg_model = build_model(df)

# Initialize the Tkinter GUI
root = Tk()
root.geometry("800x700")
root.title("House Price Predictor")
root.configure(bg="dodgerblue")

# GUI Elements
Label(root, text="House Price Predictor", font=("Helvetica", 16), bg="dodgerblue", fg="white").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

Label(root, text="Enter the number of BHKs:", bg="dodgerblue", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e")
bhks_var = StringVar()
Entry(root, textvariable=bhks_var).grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Enter the square footage:", bg="dodgerblue", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e")
sqft_var = StringVar()
Entry(root, textvariable=sqft_var).grid(row=2, column=1, padx=10, pady=5)

Button(root, text="Predict Price", command=predict_price, bg="green", fg="white").grid(row=3, column=0, columnspan=2, padx=10, pady=10)

Label(root, text="Predicted Price:", bg="dodgerblue", fg="white").grid(row=4, column=0, padx=10, pady=5, sticky="e")
price_var = StringVar()
Label(root, textvariable=price_var, bg="dodgerblue", fg="white").grid(row=4, column=1, padx=10, pady=5)

Label(root, text="Sum of Squared Errors:", bg="dodgerblue", fg="white").grid(row=5, column=0, padx=10, pady=5, sticky="e")
sse_var = StringVar()
Label(root, textvariable=sse_var, bg="dodgerblue", fg="white").grid(row=5, column=1, padx=10, pady=5)

root.mainloop()
