# Optimal Price Calculator

Optimal Price Calculator is a Python desktop application that helps determine the optimal selling price of a product using a basic economic demand model. The application calculates revenue and profit across a range of prices, identifies the price that maximizes profit, and visualizes the results using an interactive profit graph.

The project features a simple graphical user interface (GUI) built with Tkinter and uses Matplotlib for data visualization.

---

## Features

- Calculate product demand using a linear demand model
- Compute revenue and profit across multiple price points
- Determine the optimal selling price for maximum profit
- Display maximum achievable profit
- Interactive desktop GUI built with Tkinter
- Profit vs. Price graph with the optimal point highlighted
- Simple and easy-to-use interface

---

## Technologies Used

### Programming Language

- Python

### Libraries

- Tkinter
- NumPy
- Matplotlib

---

## Project Structure

```text
Optimal_Price_Calculator/
│
├── main.py
└── README.md
```

---

## Mathematical Model

The application uses a simple linear demand model.

### Demand Function

```
Quantity = a − b × Price
```

Where:

- **a** = Base Demand
- **b** = Price Sensitivity

### Revenue

```
Revenue = Price × Quantity
```

### Profit

```
Profit = (Price − Cost per Unit) × Quantity
```

The application evaluates profit across a range of prices and identifies the selling price that generates the maximum profit.

---

## How It Works

1. Enter the **Base Demand (a)**.
2. Enter the **Price Sensitivity (b)**.
3. Enter the **Cost per Unit (c)**.
4. Click the **Calculate** button.
5. The application computes:
   - Quantity Sold
   - Revenue
   - Profit
   - Optimal Selling Price
   - Maximum Profit
6. A Profit vs. Price graph is displayed with the optimal price highlighted.

---

## Installation

Clone the repository.

```bash
git clone https://github.com/MahimaSinghRathore/optimal_price_calculator.git
```

Navigate to the project directory.

```bash
cd optimal_price_calculator
```

Install the required libraries.

```bash
pip install numpy matplotlib
```

> **Note:** Tkinter is included with most standard Python installations. If it is not available, install it according to your operating system's Python distribution.

---

## Running the Application

Run the application using:

```bash
python main.py
```

---

## Input Parameters

| Parameter | Description |
|-----------|-------------|
| Base Demand (a) | Expected demand when the selling price is zero |
| Price Sensitivity (b) | Rate at which demand decreases as price increases |
| Cost per Unit (c) | Cost of producing one unit of the product |

---

## Output

The application provides:

- Optimal Selling Price
- Maximum Profit
- Profit vs. Price Graph
- Optimal Price Highlight on the Graph

---

## Applications

- Pricing Strategy Analysis
- Profit Optimization
- Business Decision Support
- Economic Modeling
- Educational Demonstrations
- Operations Research

---

## Future Improvements

- Support multiple demand models
- Export results to CSV
- Save generated graphs
- Interactive sliders for input parameters
- Break-even analysis
- Cost and demand sensitivity analysis
- Modernized GUI interface

---

## Author

**Mahima Singh**

B.Tech Computer Science Engineering

Jaypee University of Information Technology (JUIT)

GitHub: https://github.com/MahimaSinghRathore

---

## License

This project was developed for educational purposes to demonstrate pricing optimization using Python, Tkinter, NumPy, and Matplotlib.
