def get_caps():
    return {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",

        "appPackage": "com.motorola.cn.calculator",
        "appActivity": "com.motorola.cn.calculator.Calculator",

        "noReset": True,

        "uiautomator2ServerLaunchTimeout": 60000,
        "uiautomator2ServerInstallTimeout": 120000,
        "adbExecTimeout": 120000,
        "newCommandTimeout": 180
    }