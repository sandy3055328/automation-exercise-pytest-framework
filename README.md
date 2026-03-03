# Automation Exercise Pytest Framework

A complete Selenium-Pytest automation framework built for [AutomationExercise.com](https://automationexercise.com) using the Page Object Model design pattern.

## Features

- ✅ **14 End-to-End Test Cases** covering registration, login, products, cart, and checkout
- ✅ **Page Object Model** implementation for clean, maintainable code
- ✅ **Cross-browser testing** support (Chrome, Edge)
- ✅ **HTML Reports** with pytest-html
- ✅ **Automatic screenshots** on test failures
- ✅ **Custom markers** for test categorization (TC001-TC014)
- ✅ **Configuration via command line** (`--browser` option)

## 📁 Project Structure

```
automation_exercise/
├── pages/              # Page Object classes
│   ├── login.py
│   ├── contact_page.py
│   ├── products_page.py
│   └── checkout_page.py
├── tests/              # Test files
│   ├── test_login.py
│   ├── test_contact.py
│   ├── test_products.py
│   └── test_checkout.py
├── reports/            # Generated HTML reports
├── screenshots/        # Failure screenshots
├── logs/               # Execution logs
├── conftest.py         # Pytest fixtures and hooks
├── pytest.ini          # Test markers configuration
└── requirements.txt    # Project dependencies
```

## 🛠️ Technologies Used

- Python 3.14
- Selenium WebDriver
- Pytest
- Page Object Model
- pytest-html

## 📋 Test Cases Covered

| TC# | Description | Status |
|-----|-------------|--------|
| TC001 | Register User | ✅ |
| TC002 | Valid Login | ✅ |
| TC003 | Invalid Login | ✅ |
| TC004 | Logout | ✅ |
| TC005 | Existing Email | ✅ |
| TC006 | Contact Us | ✅ |
| TC007 | Test Cases Page | ✅ |
| TC008 | View Products | ✅ |
| TC009 | Search Product | ✅ |
| TC010 | Homepage Subscription | ✅ |
| TC011 | Cart Subscription | ✅ |
| TC012 | Add to Cart | ✅ |
| TC013 | Verify Cart Quantity | ✅ |
| TC014 | Place Order | ✅ |

## 🚦 How to Run

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

### Run Specific Test
```bash
pytest tests/test_login.py::test_register_user -v
```

### Run with Specific Browser
```bash
pytest tests/ -v --browser=Chrome
```

## 📊 Reports

After each test run, HTML reports are automatically generated in the `reports/` folder. Open them in any browser to view detailed results with screenshots of failures.

## Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first.

## License

MIT

##  Author

**Sandeep**  
[GitHub Profile](https://github.com/sandy3055328)


