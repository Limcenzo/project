# RetailNova - Retail Analytics Dashboard 🎓🛍️

**RetailNova** is an interactive, modern, real-time retail analytics dashboard built with **Streamlit**, **Pandas**, and **Seaborn/Matplotlib**. The application is designed to give e-commerce and retail businesses quick insights into revenue performance, product distributions, customer satisfaction, and key business metrics through a sleek glassmorphism UI.

---

## 🌟 Key Features

* **Overview Dashboard**: High-level KPIs displaying Total Revenue, Total Orders, Total Customers, Units Sold, and Average Customer Ratings with custom styled KPI cards.
* **Interactive Sales Analysis**: Filter sales data dynamically by **Product Category**, **Country**, **Payment Method**, **Order Status**, and **Date Range**.
* **Modern Aesthetic**: Glassmorphism design system using CSS, gradient headers, and styled sidebar navigation using `streamlit-option-menu`.
* **Data Visualizations**: Built-in visual analysis (Histograms, Distributions) using Seaborn and Matplotlib.

---

## 📁 Repository Structure

```text
├── dashboard_2.py       # Main Streamlit application file
├── clean_ecom.csv       # Cleaned e-commerce dataset (required)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📊 Dataset Requirements (`clean_ecom.csv`)

The application expects a CSV file named `clean_ecom.csv` in the root directory with the following columns:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `order_id` | String/Int | Unique identifier for each order |
| `customer_id` | String/Int | Unique identifier for each customer |
| `order_date` | Date | Date when the order was placed (`YYYY-MM-DD`) |
| `product_category`| String | Category of the purchased item |
| `product_name` | String | Name of the product |
| `quantity` | Int | Number of units purchased |
| `unit_price` | Float | Price per single unit |
| `discount_pct` | Float | Applied discount percentage |
| `payment_method` | String | Method of payment (e.g., Credit Card, UPI, Paypal) |
| `shipping_city` | String | City where the item was delivered |
| `country` | String | Country of delivery |
| `order_status` | String | Status of the order (e.g., Delivered, Pending, Cancelled) |
| `customer_rating` | Float | Rating given by the customer (1 to 5) |
| `revenue` | Float | Calculated revenue for the order line |

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have **Python 3.8+** installed on your machine.

### 2. Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-username/RetailNova.git
cd RetailNova
```

Install the required Python packages:

```bash
pip install streamlit streamlit-option-menu pandas matplotlib seaborn
```

*(Optional)* You can create a `requirements.txt` file containing:
```text
streamlit
streamlit-option-menu
pandas
matplotlib
seaborn
```

### 3. Run the Streamlit Application

Execute the following command to launch the dashboard:

```bash
streamlit run dashboard_2.py
```

The app will automatically open in your default browser at `http://localhost:8501`.

---

## 📱 Navigation & App Layout

1. **Header Banner**: Branded RetailNova hero section.
2. **Top Navigation Bar**: Horizontal menu featuring:
   * 📊 **Overview**: Top-level executive metrics.
   * 📈 **Sales Analysis**: Filterable revenue & order performance.
   * 📦 **Product Insights**: *(Extensible)* Detailed breakdown by product.
   * 🌐 **Geographic Analysis**: *(Extensible)* Sales distribution across countries.
   * 👥 **Order & Customer**: *(Extensible)* Customer rating and order metrics.
3. **Sidebar**: Premium dark theme sidebar for interactive filtering (Categories, Countries, Payment Methods, Order Status, and Date Range).

---

## 🛠️ Built With

* [Streamlit](https://streamlit.io/) - Web framework for data apps
* [streamlit-option-menu](https://github.com/victr/streamlit-option-menu) - Custom navigation menu component
* [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
* [Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/) - Visualizations