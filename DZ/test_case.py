from elements import Search, Button, Pic, Text
from page import Page

home1 = Search('body > div.page_layout.page_layout-clear > header > div.layout.widget-type_widget_v4_header_4_6b677bbb4943ee7655d464f5e60d70e2 > div > div.header.header_no-languages > div.header__content > div.header-part-main > div > div.header__area-search > div > form > input.form-control.form-control_size-l.header__search-field')
home1.exist(Page.url)

home2 = Button('body > div.page_layout.page_layout-clear > header > div.layout.widget-type_widget_v4_header_4_6b677bbb4943ee7655d464f5e60d70e2 > div > div.header.header_no-languages > div.header__content > div.header-part-main > div > div.header__area-search > div > form > button')
home2.exist(Page.url)

home3 = Pic('body > div.page_layout.page_layout-clear > header > div.layout.widget-type_widget_v4_header_4_6b677bbb4943ee7655d464f5e60d70e2 > div > div.header.header_no-languages > div.header__content > div.header-part-main > div > div.header__area-logo > span > img')
home3.exist(Page.url)

home4 = Text('body > div.page_layout.page_layout-clear > header > div.layout.widget-type_system_widget_v4_delimeters_text > div > div > div.delimeter_text')
home4.exist(Page.url)

