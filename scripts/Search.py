

class Search:
    def __init__(self, urls):
        self.urls = urls

    def search_admin(self):
        admin_list = []
        keyword = "admin"
        for url in self.urls:
            if keyword in url:
                admin_list.append(url)
        return admin_list