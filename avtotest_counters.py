import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.webkit.launch()
        yield browser
        browser.close()

@pytest.mark.parametrize("counter_name, selector", [
    ("avito-1", "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E"),
    ("avito-2", "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(2)"),
    ("avito-5", "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(4)"),
    ("avito-8", "#app > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > div.desktop-impact-items-F7T6E > div:nth-child(6)")
])
def test_screenshot_counters(browser, counter_name, selector):
    page = browser.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    screenshot_path = f"output/{counter_name.lower()}.png"
    element = page.wait_for_selector(selector)
    element.screenshot(path=screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

# Создаем папку "output", если ее нет
if not os.path.exists("output"):
    os.makedirs("output")
