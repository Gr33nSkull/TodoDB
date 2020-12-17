from exists import Chc_exestance
from load import Load
from fns import Fn
from compare_tm import comp as comp_tm

son = Load()
exists = Chc_exestance()
fn = Fn()


class Ls_exec:

    history = list()

    def del_hs(self):
        if len(self.history) > 250:
            self.history.pop(0)

    def add(self, request):
        ls_ls = son.open_ls_ls()
        ls_exists = exists.ls(request.ls_name, ls_ls)
        if not ls_exists:
            tsk_ls = son.open_tsk_ls()

            d = {
                "name": request.ls_name,
                "bool": False,
                "reminder": request.alarm
            }
            ls_ls.append(d)
            tsk_ls.append([])

            self.history.append(request)
            self.del_hs()
            son.save_ls_ls(ls_ls)
            son.save_tsk_ls(tsk_ls)
        else:
            similar_edits = fn.chc_history(self.history, request)

            for i in similar_edits:
                a = comp_tm(i.time, request.time)
                if a == "second time is older":
                    return

            ls_index = 0
            for i in ls_ls:
                if i["name"] == request.ls_name:
                    break
                ls_index += 1

            ls_ls[ls_index]["reminder"] = request.alarm
            self.history.append(request)
            self.del_hs()
            son.save_ls_ls(ls_ls)

    def myb_add(self, request):
        ls_ls = son.open_ls_ls()

        deleted = fn.chc_ls_del_hs(request, self.history)

        if not deleted:
            tsk_ls = son.open_tsk_ls()

            d = {
                "name": request.ls_name,
                "bool": False,
                # TODO POPRAVI
                "reminder": "+-00:00"
            }
            ls_ls.append(d)
            tsk_ls.append([])
            self.history.append(request)
            self.del_hs()

            son.save_ls_ls(ls_ls)
            son.save_tsk_ls(tsk_ls)

    def del_ls(self, request):
        ls_ls = son.open_ls_ls()

        ls_exists = exists.ls(request.ls_name, ls_ls)

        if not ls_exists:
            return

        tsk_ls = son.open_tsk_ls()

        ls_index = 0
        for i in ls_ls:
            if i["name"] == request.ls_name:
                break
            ls_index += 1

        print("HHHHHHHHHHHHHHHHHMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm")
        tsk_ls.pop(ls_index)
        ls_ls.pop(ls_index)

        self.history.append(request)
        self.del_hs()

        son.save_ls_ls(ls_ls)
        son.save_tsk_ls(tsk_ls)

    def chng_alarm(self, request):
        ls_ls = son.open_ls_ls()
        ls_exists = exists.ls(request.ls_name, ls_ls)
        if not ls_exists:
            return

        similar_edits = fn.chc_history(self.history, request)

        for i in similar_edits:
            a = comp_tm(i.time, request.time)
            if a == "second time is older":
                return

        ls_index = 0
        for i in ls_ls:
            if i["name"] == request.ls_name:
                break
            ls_index += 1

        ls_ls[ls_index]["reminder"] = request.alarm
        self.history.append(request)
        self.del_hs()

        son.save_ls_ls(ls_ls)