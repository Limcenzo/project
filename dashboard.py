import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('clean_ecom.csv')

st.set_page_config(
    page_title="RetailNova",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- CUSTOM CSS --------------------

st.markdown("""
<style>


/* Global background */
.stApp {
    background: radial-gradient(
        circle at 50% 50%,
        #1e1e2f 0%,
        #0d0d15 100%
    );
    color: white;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Hero section */
.hero {
    padding: 40px 20px;
    text-align: center;
    background: rgba(255, 255, 255, 0.03);
    border-radius: 30px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    margin-bottom: 25px;
}

/* Main title */
.title {
    font-size: 52px;
    font-weight: 800;
    margin: 0;
    background: linear-gradient(to right, #ffffff, #ff7e7e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Inline headings */
.title-inline {
    font-size: 30px;
    font-weight: 800;
    margin-bottom: 20px;
    background: linear-gradient(to right, #ffffff, #ff7e7e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Description */
.desc {
    font-size: 17px;
    color: #cccccc;
    line-height: 1.8;
}

/* Glassmorphism cards */
.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease-in-out;
    margin-bottom: 22px;
    height: 100%;
    backdrop-filter: blur(10px);
}

.card:hover {
    transform: translateY(-5px);
    border-color: #ff4b4b;
    background: rgba(255, 255, 255, 0.08);
    box-shadow: 0 10px 35px rgba(255, 75, 75, 0.15);
}

/* Card list */
.card ul {
    padding-left: 25px;
}

.card li {
    margin-bottom: 12px;
}

/* Streamlit buttons */
div.stButton > button {
    background: linear-gradient(135deg, #ff4b4b, #ff7e7e);
    color: white;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    padding: 12px 22px;
    font-weight: 600;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    color: white;
    border-color: #ffffff;
    box-shadow: 0 8px 20px rgba(255, 75, 75, 0.35);
}

div.stButton > button:active {
    transform: scale(0.98);
}

/* Responsive typography */
@media (max-width: 768px) {
    .title {
        font-size: 38px;
    }

    .title-inline {
        font-size: 25px;
    }

    .card {
        padding: 22px;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------- HERO HEADER --------------------

st.markdown("""
<div class="hero">
    <h1 class="title">RetailNova</h1>
    <p style="color:#bbbbcc; font-size:18px; margin-top:12px;">
        Learn smarter. Build skills. Grow faster.
    </p>
</div>
""", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
     options=[
        "Overview",
        "Sales Analysis",
        "Product Insights",
        "Geographic Analysis",
        "Order & Customer"
    ],
    icons=[
        "grid-1x2-fill",
        "graph-up-arrow",
        "box-seam-fill",
        "globe-asia-australia",
        "people-fill"
    ],
    orientation="horizontal",
    styles={
        "container": {
            "padding": "6px",
            "background-color": "rgba(255,255,255,0.05)",
            "border-radius": "15px",
            "border": "1px solid rgba(255,255,255,0.1)",
        },
        "icon": {
            "color": "#ff7e7e",
            "font-size": "20px",
        },
        "nav-link": {
            "font-size": "17px",
            "text-align": "center",
            "margin": "3px",
            "color": "white",
            "font-weight": "500",
            "border-radius": "10px",
        },
        "nav-link-selected": {
            "background": "linear-gradient(135deg, #ff4b4b, #ff7e7e)",
            "font-weight": "700",
            "border-radius": "10px",
        },
    }
)


# -------------------- OVERVIEW PAGE --------------------

# -------------------- OVERVIEW PAGE --------------------

if selected == "Overview":

    # KPI calculations
    total_revenue = df["revenue"].sum()
    total_orders = df["order_id"].nunique()
    total_customers = df["customer_id"].nunique()
    units_sold = df["quantity"].sum()
    avg_rating = df["customer_rating"].mean()

    # ---------------- KPI + HEADING CSS ----------------

    st.markdown("""
    <style>
    .kpi-card {
        background: linear-gradient(
            135deg,
            rgba(255,255,255,0.07),
            rgba(255,255,255,0.025)
        );
        padding: 22px 18px;
        border-radius: 18px;
        border: 1px solid rgba(255,126,126,0.20);
        box-shadow: 0 5px 22px rgba(0,0,0,0.20);
        min-height: 145px;
        transition: 0.3s ease;
    }

    .kpi-card:hover {
        transform: translateY(-4px);
        border-color: #ff7e7e;
        box-shadow: 0 8px 25px rgba(255,75,75,0.12);
    }

    .kpi-label {
        color: #b9b9ca;
        font-size: 13px;
        margin-bottom: 12px;
    }

    .kpi-value {
        color: white;
        font-size: 25px;
        font-weight: 800;
        margin-bottom: 8px;
        overflow-wrap: anywhere;
    }

    .kpi-caption {
        color: #ff9292;
        font-size: 11px;
    }

    .overview-header {
        padding: 24px 28px;
        margin: 15px 0 25px 0;
        background: linear-gradient(
            120deg,
            rgba(255,75,75,0.10),
            rgba(255,255,255,0.025),
            rgba(255,126,126,0.06)
        );
        border: 1px solid rgba(255,126,126,0.18);
        border-radius: 20px;
        box-shadow: 0 6px 25px rgba(0,0,0,0.18);
    }

    .overview-title {
        font-size: 32px;
        font-weight: 800;
        margin: 0 0 8px 0;
        background: linear-gradient(
            90deg, #ffffff, #ffb0b0, #ff7e7e
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .overview-desc {
        font-size: 15px;
        color: #b9b9ca;
        margin: 0;
        line-height: 1.7;
    }

    .overview-tag {
        color: #ff9292;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
    }

    @media (max-width: 768px) {
        .overview-header {
            padding: 20px;
        }

        .overview-title {
            font-size: 26px;
        }

        .kpi-value {
            font-size: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- OVERVIEW HEADING ----------------

    st.markdown("""
    <div class="overview-header">
        <div class="overview-tag">RETAILNOVA / DASHBOARD</div>
        <h2 class="overview-title">Retail Overview</h2>
        <p class="overview-desc">
            Track sales performance, explore customer insights,
            and discover what's driving your retail business.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- KPI CARDS ----------------

    c1, c2, c3, c4, c5 = st.columns(5)

    kpis = [
        (
            c1, "💰", "Total Revenue",
            f"₹{total_revenue:,.2f}",
            "Total recorded revenue"
        ),
        (
            c2, "🛍️", "Total Orders",
            f"{total_orders:,}",
            "Unique orders"
        ),
        (
            c3, "👥", "Total Customers",
            f"{total_customers:,}",
            "Unique customers"
        ),
        (
            c4, "📦", "Units Sold",
            f"{units_sold:,.0f}",
            "Total quantity"
        ),
        (
            c5, "⭐", "Average Rating",
            f"{avg_rating:.2f}/5"
            if pd.notna(avg_rating) else "N/A",
            "Average customer rating"
        )
    ]

    for col, icon, label, value, caption in kpis:
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">{icon} {label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-caption">{caption}</div>
            </div>
            """, unsafe_allow_html=True)


# -------------------- OTHER PAGES --------------------


    # -------------------- SALES FILTER NAVBAR CSS --------------------

elif selected == "Sales Analysis":

    import seaborn as sns

    sales_df = df.copy()

    sales_df["order_date"] = pd.to_datetime(
        sales_df["order_date"], errors="coerce"
    )
    sales_df["revenue"] = pd.to_numeric(
        sales_df["revenue"], errors="coerce"
    )

    # ---------------- PAGE HEADING ----------------

    st.markdown(
        '<h2 class="title-inline">Sales Analysis</h2>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="desc">'
        'Explore revenue trends, product performance, and order distribution.'
        '</p>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ---------------- SIDEBAR FILTERS ----------------

    categories = sorted(
        sales_df["product_category"].dropna().unique().tolist()
    )
    countries = sorted(
        sales_df["country"].dropna().unique().tolist()
    )
    payments = sorted(
        sales_df["payment_method"].dropna().unique().tolist()
    )
    statuses = sorted(
        sales_df["order_status"].dropna().unique().tolist()
    )

    valid_dates = sales_df["order_date"].dropna()

    with st.sidebar:
        
# ---------------- PREMIUM SIDEBAR FILTERS ----------------

# Add this CSS to your existing custom CSS block

# ---------------- RETAILNOVA SIDEBAR THEME ----------------

                st.markdown("""
                <style>
                /* Match the main page background */
                [data-testid="stSidebar"] {
                    background: radial-gradient(
                        circle at 20% 0%,
                        #242438 0%,
                        #141420 48%,
                        #0d0d15 100%
                    );
                    border-right: 1px solid rgba(255, 126, 126, 0.16);
                }

                /* Sidebar spacing */
                [data-testid="stSidebar"] .block-container {
                    padding-top: 1.5rem;
                    padding-left: 1.1rem;
                    padding-right: 1.1rem;
                }

                /* Branded sidebar header */
                .rn-filter-hero {
                    position: relative;
                    overflow: hidden;
                    padding: 23px 19px;
                    margin: 0 0 22px 0;
                    border-radius: 22px;
                    background: linear-gradient(
                        135deg,
                        rgba(255, 75, 75, 0.19),
                        rgba(255, 126, 126, 0.055) 55%,
                        rgba(255, 255, 255, 0.025)
                    );
                    border: 1px solid rgba(255, 126, 126, 0.22);
                    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.20);
                }

                .rn-filter-hero:after {
                    content: "";
                    position: absolute;
                    width: 100px;
                    height: 100px;
                    right: -35px;
                    top: -38px;
                    border-radius: 50%;
                    background: rgba(255, 100, 120, 0.12);
                    filter: blur(5px);
                }

                .rn-filter-brand {
                    color: #ff9292;
                    font-size: 10px;
                    font-weight: 800;
                    letter-spacing: 2.5px;
                    margin-bottom: 11px;
                }

                .rn-filter-heading {
                    font-size: 27px;
                    line-height: 1.2;
                    font-weight: 800;
                    margin: 0;
                    background: linear-gradient(90deg, #ffffff, #ff9292);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                }

                .rn-filter-description {
                    font-size: 12px;
                    color: #b9b9ca;
                    line-height: 1.7;
                    margin: 10px 0 0 0;
                }

                /* Section headings */
                [data-testid="stSidebar"] h3,
                [data-testid="stSidebar"] h4 {
                    color: #ffffff;
                    font-weight: 750;
                }

                /* Widget labels */
                [data-testid="stSidebar"] label {
                    color: #d7d7e5 !important;
                    font-size: 12px !important;
                    font-weight: 600 !important;
                }

                /* Dark, rounded selection controls */
                [data-testid="stSidebar"] [data-baseweb="select"] > div {
                    background: rgba(255, 255, 255, 0.045);
                    border: 1px solid rgba(255, 255, 255, 0.12);
                    border-radius: 11px;
                    transition: border-color 0.2s ease;
                }

                [data-testid="stSidebar"] [data-baseweb="select"] > div:hover {
                    border-color: rgba(255, 126, 126, 0.65);
                }

                /* Selected values */
                [data-testid="stSidebar"] [data-baseweb="tag"] {
                    background: rgba(255, 75, 75, 0.17);
                    border: 1px solid rgba(255, 126, 126, 0.25);
                    border-radius: 7px;
                }

                /* Date input */
                [data-testid="stSidebar"] [data-testid="stDateInput"] input {
                    background: rgba(255, 255, 255, 0.045);
                    border: 1px solid rgba(255, 255, 255, 0.12);
                    border-radius: 10px;
                    color: white;
                }

                /* Gradient separator */
                .rn-filter-divider {
                    height: 1px;
                    margin: 20px 0;
                    background: linear-gradient(
                        90deg,
                        transparent,
                        rgba(255, 126, 126, 0.4),
                        transparent
                    );
                }

                /* Reset button */
                [data-testid="stSidebar"] div.stButton > button {
                    width: 100%;
                    min-height: 43px;
                    border-radius: 12px;
                    background: linear-gradient(135deg, #ff4b4b, #ff7e7e);
                    color: white;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                    font-size: 13px;
                    font-weight: 700;
                    box-shadow: 0 5px 18px rgba(255, 75, 75, 0.16);
                }

                [data-testid="stSidebar"] div.stButton > button:hover {
                    border-color: #ffffff;
                    box-shadow: 0 7px 23px rgba(255, 75, 75, 0.28);
                    transform: translateY(-2px);
                }

                /* Subtle sidebar captions */
                [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
                    color: #a8a8bc;
                    font-size: 11px;
                }
                </style>
                """, unsafe_allow_html=True)


                # ---------------- SIDEBAR FILTER PANEL ----------------

                with st.sidebar:

                    st.markdown("""
                    <div class="rn-filter-hero">
                        <div class="rn-filter-brand">RETAILNOVA / ANALYTICS</div>
                        <h2 class="rn-filter-heading">Explore Data</h2>
                        <p class="rn-filter-description">
                            Your retail insights, refined.
                            Customize the view using the filters below.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("#### 🛍️  Product & Market")

                    selected_categories = st.multiselect(
                        "Product Category",
                        categories,
                        default=categories,
                        key="sales_category_filter",
                        help="Choose the product categories to include."
                    )

                    selected_countries = st.multiselect(
                        "Country",
                        countries,
                        default=countries,
                        key="sales_country_filter",
                        help="Choose the countries to include."
                    )

                    st.markdown(
                        '<div class="rn-filter-divider"></div>',
                        unsafe_allow_html=True
                    )

                    st.markdown("#### 💳  Order Details")

                    selected_payments = st.multiselect(
                        "Payment Method",
                        payments,
                        default=payments,
                        key="sales_payment_filter"
                    )

                    selected_statuses = st.multiselect(
                        "Order Status",
                        statuses,
                        default=statuses,
                        key="sales_status_filter"
                    )

                    st.markdown(
                        '<div class="rn-filter-divider"></div>',
                        unsafe_allow_html=True
                    )

                    st.markdown("#### 📅  Time Period")

                    if not valid_dates.empty:
                        min_date = valid_dates.min().date()
                        max_date = valid_dates.max().date()

                        date_range = st.date_input(
                            "Order Date Range",
                            value=(min_date, max_date),
                            min_value=min_date,
                            max_value=max_date,
                            key="sales_date_filter"
                        )
                    else:
                        date_range = ()

                    st.markdown(
                        '<div class="rn-filter-divider"></div>',
                        unsafe_allow_html=True
                    )

                    st.caption("REFINE YOUR VIEW")

                    if st.button("↺  Reset All Filters", key="reset_sales_filters"):
                        for key in [
                            "sales_category_filter",
                            "sales_country_filter",
                            "sales_payment_filter",
                            "sales_status_filter",
                            "sales_date_filter"
                        ]:
                            st.session_state.pop(key, None)

                        st.rerun()
