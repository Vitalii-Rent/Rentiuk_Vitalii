from factory import PageFactory


def run_scenario(job_name='Data Science engineer', description='Middle seniority', notes='123'):
    factory = PageFactory()
    login_page = factory.create_login_page()

    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login_btn()

    admin_page = factory.create_admin_page()
    admin_page.click_admin_btn()
    admin_page.click_job_btn()
    admin_page.click_job_titles_btn()
    admin_page.click_add_btn()

    titles_page = factory.create_titles_page()
    titles_page.enter_title(job_name)
    titles_page.enter_description(description)
    titles_page.enter_notes(notes)
    titles_page.click_save_btn()

    added_title_row = admin_page.find_title_row(job_name)

    # test_addition(added_title_row)

    admin_page.del_title(added_title_row)
    del_title_row = admin_page.find_title_row(job_name)
    # test_delition(del_title_row)

    factory.driver.quit()
    return added_title_row, del_title_row
