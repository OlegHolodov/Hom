# Задание 1

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
#driver.get("http://practice.automationtesting.in/")
#driver.implicitly_wait(5)
#driver.maximize_window()


#my_account_menu = driver.find_element_by_link_text("My Account")
#my_account_menu.click()
#user_name_field = driver.find_element_by_id("username")
#user_name_field.send_keys("oleg.hols1@yandex.ru")
#password_field = driver.find_element_by_id("password")
#password_field.send_keys("0001988xxxZZZ!@?")
#login_btn = driver.find_element_by_name("login")
#login_btn.click()
#shop_tab = driver.find_element_by_link_text("Shop")
#shop_tab.click()
#html_5_forms_book = driver.find_element_by_css_selector(".post-181 > a > h3")
#html_5_forms_book.click()
#book_title = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product_title"), 'HTML5 Forms'))

#driver.quit()

# Задание 2

#from selenium import webdriver

#driver = webdriver.Chrome()
#driver.get("http://practice.automationtesting.in/")
#driver.implicitly_wait(5)
#driver.maximize_window()

#my_account_menu = driver.find_element_by_link_text("My Account")
#my_account_menu.click()
#user_name_field = driver.find_element_by_id("username")
#user_name_field.send_keys("oleg.hols1@yandex.ru")
#password_field = driver.find_element_by_id("password")
#password_field.send_keys("0001988xxxZZZ!@?")
#login_btn = driver.find_element_by_name("login")
#login_btn.click()
#shop_tab = driver.find_element_by_link_text("Shop")
#shop_tab.click()
#html_category = driver.find_element_by_link_text("HTML")
#html_category.click()
#items_count = driver.find_elements_by_css_selector("a > h3")
#if len(items_count) == 3:
#print("В категории 3 товара")
#else:
#print("Ошибка. Количество товаров в категории: " + str(len(items_count)))

#driver.quit()

# Задание 3

#from selenium import webdriver
#from selenium.webdriver.support.select import Select

#driver = webdriver.Chrome()
#driver.get("http://practice.automationtesting.in/")
#driver.implicitly_wait(5)
#driver.maximize_window()

#my_account_menu = driver.find_element_by_link_text("My Account")
#my_account_menu.click()
#user_name_field = driver.find_element_by_id("username")
#user_name_field.send_keys("oleg.hols1@yandex.ru")
#password_field = driver.find_element_by_id("password")
#password_field.send_keys("0001988xxxZZZ!@?")
#login_btn = driver.find_element_by_name("login")
#login_btn.click()
#shop_tab = driver.find_element_by_link_text("Shop")
#shop_tab.click()
#items_selector = driver.find_element_by_name("orderby")
#items_selector_default = items_selector.get_attribute("value")
#if items_selector_default == "menu_order":
#    print("Выбрана сортировка по умолчанию")
#else:
#    print("Выбрана сортировка НЕ по умолчанию")
#select = Select(items_selector)
#select.select_by_value("price-desc")
#items_selector = driver.find_element_by_name("orderby")
#items_selector_low = items_selector.get_attribute("value")
#if items_selector_low == "price-desc":
#    print("Выбрана сортировка по убыванию")
#else:
#    print("Выбрана сортировка НЕ по убыванию")

#driver.quit()

# Задание 3

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
#driver.get("http://practice.automationtesting.in/")
#driver.implicitly_wait(5)
#driver.maximize_window()

#my_account_menu = driver.find_element_by_link_text("My Account")
#my_account_menu.click()
#user_name_field = driver.find_element_by_id("username")
#user_name_field.send_keys("oleg.hols1@yandex.ru")
#password_field = driver.find_element_by_id("password")
#password_field.send_keys("0001988xxxZZZ!@?")
#login_btn = driver.find_element_by_name("login")
#login_btn.click()
#shop_tab = driver.find_element_by_link_text("Shop")
#shop_tab.click()
#android_quick_start_book = driver.find_element_by_css_selector(".post-169 h3")
#android_quick_start_book.click()
#book_old_price = driver.find_element_by_css_selector(".price > del > span")
#ook_old_price_text = book_old_price.text
#book_new_price = driver.find_element_by_css_selector(".price > ins > span")
#book_new_price_text = book_new_price.text
#assert book_old_price_text == "₹600.00"
#ssert book_new_price_text == "₹450.00"
#ook_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
#ook_cover.click()
#ook_cover_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
#book_cover_close.click()

#driver.quit()

# Задание 4

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#rom selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Chrome()
#driver.get("http://practice.automationtesting.in/")
#driver.implicitly_wait(5)
#driver.maximize_window()

#shop_tab = driver.find_element_by_link_text("Shop")
#shop_tab.click()
#html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 > a h3")
#html5_webapp_development_book.click()
#html5_webapp_development_book_add_btn.click()
#basket_item_value = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
#basket_item_value_text = basket_item_value.text
#assert basket_item_value_text == "1 Item"
#basket_price_value = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
#basket_price_value_text = basket_price_value.text
#assert basket_price_value_text == "₹180.00"
#basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
#basket_btn.click()l
#subtotal_price = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
#total_price = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00"))

#driver.quit()

# Задание 5

#from selenium import webdriver
#import time

#driver = webdriver.Chrome()
#driver.get("http://practice.automationtesting.in/")
#driver.implicitly_wait(7)
#driver.maximize_window()

#shop_tab = driver.find_element_by_link_text("Shop")
#shop_tab.click()
#driver.execute_script("window.scrollBy(0, 300);")
#html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
#html5_webapp_development_book.click()
#time.sleep(3)
#html5_webapp_development_book.click()
#basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
#basket_btn.click()
#ime.sleep(5)
#remove_first_item_btn = driver.find_element_by_class_name("remove")
#remove_first_item_btn.click()
#undo_btn = driver.find_element_by_link_text("Undo?")
#undo_btn.click()
#quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
#quantity_field.clear()
#quantity_field.send_keys("3")
#update_basket = driver.find_element_by_name("update_cart")
#update_basket.click()
#quantity_field = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
#quantity_field_value = quantity_field.get_attribute("value")
#assert quantity_field_value == '3'
#time.sleep(5)
#apply_coupon = driver.find_element_by_name("apply_coupon")
#apply_coupon.click()
#error_message = driver.find_element_by_css_selector(".woocommerce-error")
#error_message_text = error_message.text
#assert error_message_text == 'Please enter a coupon code.'

#driver.quit()

# Задание 6

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#import time

#driver = webdriver.Chrome()
#driver.get("http://practice.automationtesting.in/")
#driver.implicitly_wait(7)
#driver.maximize_window()

#shop_tab = driver.find_element_by_link_text("Shop")
#shop_tab.click()
#driver.execute_script("window.scrollBy(0, 300);")
#html5_webapp_development_book = driver.find_element_by_css_selector(".post-182 .add_to_cart_button")
#html5_webapp_development_book.click()
#basket_btn = driver.find_element_by_class_name("wpmenucart-contents")
#basket_btn.click()
#checkout_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
#checkout_btn.click()
#first_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
#first_name.send_keys("Oleg")
#last_name = driver.find_element_by_id("billing_last_name")
#last_name.send_keys("Mobi")
#email = driver.find_element_by_id("billing_email")
#email.send_keys("oleg.hols1@yandex.ru")
#phone = driver.find_element_by_id("billing_phone")
#phone.send_keys("89204427588")
#country = driver.find_element_by_id("s2id_billing_country")
#country.click()
#country_search = driver.find_element_by_id("s2id_autogen1_search")
#country_search.send_keys("Christmas Island")
#country_second_field = driver.find_element_by_class_name("select2-match")
#country_second_field.click()
#address = driver.find_element_by_id("billing_address_1")
#address.send_keys("The Wall")
#city = driver.find_element_by_id("billing_city")
#city.send_keys("Winterfell")
#state = driver.find_element_by_id("billing_state")
#state.send_keys("North")
#postcode = driver.find_element_by_id("billing_postcode")
#postcode.send_keys("100200300")
#driver.execute_script("window.scrollBy(0, 600);")
#time.sleep(5)
#payment_check = driver.find_element_by_id("payment_method_cheque")
#payment_check.click()
#place_order_btn = driver.find_element_by_id("place_order")
#place_order_btn.click()
#success_message = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),
#"Thank you. Your order has been received."))
#payment_method_message = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))

#driver.quit()