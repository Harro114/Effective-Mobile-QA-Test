import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.usefixtures
def test_automate_form():
    # Переменные
    url = "https://www.saucedemo.com/"
    login_text = "standard_user"
    password_text = "secret_sauce"

    with sync_playwright() as p:
        # Инициализация браузера
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)

        # Логин в приложение
        login = page.wait_for_selector(f"#{"user-name"}")
        password = page.wait_for_selector(f"#{"password"}")
        login.fill(login_text)
        password.fill(password_text)
        button_login = page.wait_for_selector(f"#{"login-button"}")
        button_login.click()

        # Добавление товара в корзину
        add_card_button = page.query_selector(f"#{"add-to-cart-sauce-labs-backpack"}")
        add_card_button.click()

        # Переход в корзину
        basket_button = page.query_selector(f".{"shopping_cart_container"}")
        basket_button.click()

        # Проверка товара в корзине
        assert "Sauce Labs Backpack" in page.inner_text(f".{"cart_item"}")
        checkout_button = page.query_selector(f"#{"checkout"}")
        checkout_button.click()

        # Ввод данных о покупателе
        name = page.wait_for_selector(f"#{"first-name"}")
        surname = page.wait_for_selector(f"#{"last-name"}")
        post_code = page.wait_for_selector(f"#{"postal-code"}")
        name.fill("Maxim")
        surname.fill("Vlasov")
        post_code.fill("192342")
        continue_button = page.wait_for_selector(f"#{"continue"}")
        continue_button.click()

        # Проверка оформления товара
        finish_button = page.query_selector(f"#{"finish"}")
        finish_button.click()
        assert "Thank you for your order!" in page.inner_text(f".{'complete-header'}")
