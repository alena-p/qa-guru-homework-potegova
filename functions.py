def function_info(func_name, **kwargs):
    edited_name = ""

    for i, value in enumerate(func_name.split("_")):
        if i == 0:
            value = value.title()
        edited_name += f"{value} "

    return {"function name": edited_name.rstrip(), "arguments": kwargs}


def open_browser(browser_name):
    pass
    print(function_info(open_browser.__name__, browser_name=browser_name))


def go_to_company_name_homepage(page_url):
    pass
    print(function_info(go_to_company_name_homepage.__name__, page_url=page_url))


def find_registration_button_on_login_page(page_url, button_text):
    pass
    print(function_info(find_registration_button_on_login_page.__name__, page_url=page_url, button_text=button_text))


open_browser("chrome")
go_to_company_name_homepage("https://qa.guru/")
find_registration_button_on_login_page("https://qa.guru/", "Submit")


