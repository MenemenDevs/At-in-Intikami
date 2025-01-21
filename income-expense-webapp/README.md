# Income Expense Web Application

This project is a simple web application for calculating income and expenses using Flask. It allows users to input their income and expenses and displays the results.

## Project Structure

```
income-expense-webapp
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd income-expense-webapp
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python run.py
```

Visit `http://127.0.0.1:5000` in your web browser to access the application.

## Features

- Input fields for income and expenses
- Calculation of total income and expenses
- Simple and user-friendly interface

## License

This project is licensed under the MIT License.