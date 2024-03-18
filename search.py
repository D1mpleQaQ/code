#导入webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# 初始化WebDriver
driver = webdriver.Firefox()

# 货币简称到全称的映射
currency_map = {
    'HKD': '港币',
    'USD': '美元',
    'EUR': '欧元',
    'JPY': '日元',
    'GBP': '英镑',
    'CHF': '瑞士法郎',
    'FRF': '法国法郎',
    'DEM': '德国马克',
    'SGD': '新加坡元',
    'SEK': '瑞典克朗',
    'DKK': '丹麦克朗',
    'NOK': '挪威克朗',
    'CAD': '加拿大元',
    'MOP': '澳门元',
    'AUD': '澳大利亚元',
    'PHP': '菲律宾比索',
    'THB': '泰国铢',
    'NZD': '新西兰元',
    'RUB': '俄罗斯卢布',
    'KRW': '韩元',
    'MYR': '林吉特',
    'TWD': '新台币',
    'NLG': '荷兰盾',
    'ITL': '意大利里拉',
    'ESP': '西班牙比塞塔',
    'BEF': '比利时法郎',
    'INR': '印度卢比',
    'IDR': '印尼盾',
    'FIM': '芬兰马克',
    'BRL': '巴西里亚尔',
    'AED': '阿联酋迪拉姆',
    'ZAR': '南非兰特',
    'SAR': '沙特里亚尔',
    'TRY': '土耳其里拉',
}

# 输入日期和货币代号
date_str_raw = input("请输入日期（格式YYYYMMDD）: ")

# 验证日期输入格式是否正确
if not date_str_raw.isdigit() or len(date_str_raw) != 8:
    print("日期格式不正确，请输入8位数字（YYYYMMDD）。")
    driver.quit()
    exit()

# 将YYYYMMDD格式的日期转换为YYYY-MM-DD格式
year = date_str_raw[:4]
month = date_str_raw[4:6]
day = date_str_raw[6:]
date_str = f"{year}-{month}-{day}"
currency_code = input("请输入货币代号: ")

if currency_code not in currency_map:
    print("无效的货币简称，请输入正确的简称。")
    driver.quit()
    exit()

currency_full_name = currency_map[currency_code]

# 访问网页
driver.get("https://www.boc.cn/sourcedb/whpj/")
wait = WebDriverWait(driver, 10)

# 定位并输入日期
date_input = driver.find_element(By.NAME, "erectDate")
date_input.send_keys(date_str)

# 定位并输入nothing
nothing_input = driver.find_element(By.NAME, "nothing")
nothing_input.send_keys(date_str)

# 定位货币选择框并选中对应的货币
currency_select = Select(driver.find_element(By.NAME, "pjname"))
currency_select.select_by_visible_text(currency_full_name)

# 定位并点击搜索按钮
search_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".invest_t .search_btn")))
search_btn.click()

# 定位并获取现汇卖出价
sell_rate_element = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(2) td:nth-child(4)")
sell_rate = sell_rate_element.text

# 输出结果
print(f"现汇卖出价: {sell_rate}")

# 构造要写入文件的字符串
result_str = f"查询日期: {date_str}\n货币: {currency_full_name}\n现汇卖出价: {sell_rate}\n\n"

# 打开文件并写入内容，使用'a'模式表示追加，这样每次运行都会把新内容追加到文件末尾
with open('result.txt', 'a', encoding='utf-8') as file:
    file.write(result_str)

# 关闭浏览器
driver.quit()