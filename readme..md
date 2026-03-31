# Mobile Calculator Automation

Automated tests for the **Motorola Calculator** on **Android emulators** using **Appium** + **Pytest**.

---

## Features

- Cross-operation support: add, subtract, multiply, divide  
- Page Object Model for maintainability  
- HTML reporting via `pytest-html`  

---

## Requirements

- Python 3.10+  
- **Android Studio** with a running emulator  
- **Appium server** running (`appium`)  
- Android SDK Platform Tools (`adb`)  

---

## Usage

1. Start your Android emulator from Android Studio.  
2. Start Appium server (`appium`).  
3. Run tests:

```bash
pytest --html=report.html --self-contained-html