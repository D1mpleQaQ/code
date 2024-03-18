#导入webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(30)

driver.get("https://www.boc.cn/sourcedb/whpj/")

with open('result1.txt', 'w', encoding='utf-8') as f:
    # 查找第一页tbody中的第一个tr，并打印其内容到文件
    header_tr = driver.find_element(By.CSS_SELECTOR, "table tbody tr.odd")
    header_cells = header_tr.find_elements(By.TAG_NAME, "th")

    # 横向打印表头单元格内容，并用空格连接
    header_content = ' '.join([cell.text.strip() for cell in header_cells])  # 使用strip()去除前后空白
    f.write(header_content + '\n')  # 写入文件并换行

    # 需要遍历网站所有10页
    for page_number in range(1, 11):
        print(f"正在爬取第 {page_number} 页...")

        # 点击“下一页”链接
        if page_number > 1:
            try:
                next_page_link = driver.find_element(By.LINK_TEXT, "下一页")
                next_page_link.click()
                # 等待页面加载完成
                driver.implicitly_wait(10)
            except Exception as e:
                print(f"在第 {page_number} 页遇到错误: {e}")
                break

        # 查找当前页的所有tr元素（除了第一个，因为它已经在上面处理过了）
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr:not(:first-child)")

        # 遍历每一行并打印内容到文件
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_content = ' '.join([cell.text if cell.text.strip() else "空" for cell in cells])  # 检查每个单元格的文本，如果为空则替换为"空"
            f.write(row_content + '\n')  # 写入文件并换行

    print("爬取完成，结果已保存到 result1.txt 文件中。")

# 关闭浏览器
driver.quit()