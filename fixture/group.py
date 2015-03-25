__author__ = 'pvarenik'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new"))):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # new group
        wd.find_element_by_name("new").click()
        # edit group fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # create group
        wd.find_element_by_name("submit").click()
        self.return_to_the_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        #select
        wd.find_element_by_name("selected[]").click()
        #delete
        wd.find_element_by_name("delete").click()
        self.return_to_the_group_page()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        #select
        wd.find_element_by_name("selected[]").click()
        #edit
        wd.find_element_by_name("edit").click()
        #edit group fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        #update group
        wd.find_element_by_name("update").click()
        self.return_to_the_group_page()

    def return_to_the_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))