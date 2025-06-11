# Healthcare Analytics Dashboard

A comprehensive healthcare data visualization dashboard built with Python Dash and Plotly, providing insights into patient demographics, medical conditions, billing analytics, and admission trends.

![Healthcare Dashboard](https://img.shields.io/badge/Python-Dash-blue)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-green)
![Healthcare](https://img.shields.io/badge/Healthcare-Analytics-red)

## 📊 Dashboard Overview

This interactive dashboard provides healthcare professionals and administrators with comprehensive insights into patient data, including:

- **Patient Demographics Analysis** - Age and gender distribution visualization
- **Medical Condition Tracking** - Distribution of various health conditions
- **Billing Analytics** - Insurance provider analysis and billing amount distributions
- **Admission Trends** - Time-based patient admission patterns

## 🎯 Key Features

### 📈 Analytics Modules

1. **Patient Demographics**
   - Interactive age distribution charts by gender
   - Gender-based filtering capabilities
   - Visual representation of patient population

2. **Medical Condition Distribution**
   - Pie chart visualization of condition prevalence
   - Covers major conditions: Diabetes, Arthritis, Hypertension, Obesity, Cancer, Asthma
   - Percentage breakdown for each condition

3. **Insurance Provider Analysis**
   - Multi-provider billing comparison (Aetna, Blue Cross, Cigna, Medicare, UnitedHealthcare)
   - Medical condition breakdown by insurance type
   - Total billing amount analysis

4. **Billing Distribution**
   - Interactive billing amount histogram
   - Adjustable range slider ($2K - $52K)
   - Frequency distribution of billing amounts

5. **Admission Trends**
   - Time-series analysis of patient admissions
   - Filterable by medical condition
   - Line and bar chart options

### 🔧 Interactive Features

- **Dynamic Filtering** - Filter data by gender, medical condition, and billing ranges
- **Responsive Design** - Professional blue-themed interface
- **Real-time Updates** - Interactive charts that update based on user selections
- **Comprehensive Metrics** - Key performance indicators displayed prominently

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/healthcare-analytics-dashboard.git
cd healthcare-analytics-dashboard
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Dashboard

1. Start the Dash application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:8050
```

## 📁 Project Structure

```
healthcare-analytics-dashboard/
│
├── app.py                 # Main Dash application
├── assets/
│   ├── healthcare.csv     # Patient healthcare dataset
│   ├── style.css          # Custom CSS styling
│   ├── style.css.map      # CSS source map
│   └── style.scss         # SCSS source file
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # Project documentation
```

## 📊 Data Overview

The dashboard processes healthcare data with the following key metrics:

- **Total Patient Records**: 55,500
- **Average Billing Amount**: $25,539
- **Medical Conditions Covered**: 6 major conditions
- **Insurance Providers**: 5 major providers

### Sample Data Structure

The `healthcare.csv` file contains patient data with fields including:
- Patient demographics (age, gender)
- Medical conditions
- Insurance provider information
- Billing amounts
- Admission dates

## 🛠️ Technologies Used

- **Python 3.7+** - Core programming language
- **Dash** - Web application framework
- **Plotly** - Interactive visualization library
- **Pandas** - Data manipulation and analysis
- **CSS/SCSS** - Custom styling

## 🎨 Design Features

- **Professional Theme** - Clean blue and white color scheme
- **Responsive Layout** - Adapts to different screen sizes
- **Interactive Elements** - Hover effects, clickable filters, and dynamic updates
- **Modern UI Components** - Cards, dropdowns, and sliders

## 📈 Use Cases

This dashboard is ideal for:

- **Healthcare Administrators** - Track patient demographics and billing
- **Insurance Companies** - Analyze claims and condition distributions
- **Medical Researchers** - Study patient admission patterns
- **Hospital Management** - Monitor operational metrics

## 🔮 Future Enhancements

- [ ] Add patient outcome tracking
- [ ] Implement predictive analytics
- [ ] Include geographic distribution maps
- [ ] Add export functionality for reports
- [ ] Integrate with electronic health records (EHR)
- [ ] Add real-time data streaming capabilities
