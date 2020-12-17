import json

class Load:

    def open_ls_ls(self):
        with open("server_ls.txt", "r") as a:
            a = json.load(a)
        return a

    def open_tsk_ls(self):
        with open("server_tsk.txt", "r") as a:
            a = json.load(a)
        return a

    def save_tsk_ls(self, tsk_ls):
        with open("server_tsk.txt", "w") as a:
            json.dump(tsk_ls, a)

    def save_ls_ls(self, ls_ls):
        with open("server_ls.txt", "w") as a:
            json.dump(ls_ls, a)
