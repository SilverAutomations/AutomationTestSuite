from entity.ExcelData import TestRow


def create_element_obj(tr: TestRow):
    tr.locator = tr.locator.replace("\"", "\'")
    if tr.timeout == "":
        tr.timeout = 0
    return f"page.wait_for_selector(\"{tr.locator}\",timeout= {tr.timeout})"


def create_exec_str(tr: TestRow, element: None):
    code = ""
    if "click" in tr.action:
        code = create_element_obj(tr) + ".click()"
    elif "fill" in tr.action:
        code = create_element_obj(tr) + ".fill(\"" + tr.value + "\")"
    elif "text content" in tr.action:
        code = create_element_obj(tr) + ".textContent()"
    elif "loop new window" in tr.action:

    else:
        code = create_element_obj(tr)

    return code

