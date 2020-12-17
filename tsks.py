from exists import Chc_exestance
from load import Load
from fns import Fn
from compare_tm import comp as comp_tm


son = Load()
fn = Fn()
exists = Chc_exestance()


class Tsk_Exec:

    history = list()

    def del_hs(self):
        if len(self.history) > 250:
            self.history.pop(0)

    def ad(self, request):
        ls_ls = son.open_ls_ls()
        tsk_ls = son.open_tsk_ls()
        ls_exists = exists.ls(request.ls_name, ls_ls)

        if not ls_exists:
            return "O:"

        tsk_exist = exists.tsk(request.ls_name, request.tsk_name, ls_ls, tsk_ls)

        if not tsk_exist:
            ls_index = 0
            for i in ls_ls:
                if i["name"] == request.ls_name:
                    break
                ls_index += 1

            d = {
                "name": request.tsk_name,
                "desc": request.ending,
                "completed": False
            }

            tsk_ls[ls_index].append(d)

            son.save_tsk_ls(tsk_ls)

            self.history.append(request)
            self.del_hs()

        else:
            similar_edits = fn.chc_tsk_history(request, self.history)
            do = True
            for i in similar_edits:
                print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
                a = comp_tm(i.time, request.time)
                if a == "second time is older":
                    print("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
                    do = False
                    return ""

            if do:
                ls_index = 0

                for i in ls_ls:
                    if i["name"] == request.ls_name:
                        break
                    ls_index += 1

                tsk_index = 0

                for i in tsk_ls[ls_index]:
                    if i["name"] == request.tsk_name:
                        tsk_ls[ls_index][tsk_index]["desc"] = request.ending
                        son.save_tsk_ls(tsk_ls)
                        break
                    tsk_index += 1
                self.history.append(request)
                self.del_hs()

        return ""

    # TODO test del
    def del_tsk(self, request):
        ls_ls = son.open_ls_ls()
        tsk_ls = son.open_tsk_ls()
        ls_exists = exists.ls(request.ls_name, ls_ls)

        if not ls_exists:
            return

        tsk_exist = exists.tsk(request.ls_name, request.tsk_name, ls_ls, tsk_ls)

        if tsk_exist:
            ls_index = 0
            for i in ls_ls:
                if i["name"] == request.ls_name:
                    break
                ls_index += 1

            for i in tsk_ls[ls_index]:
                if i["name"] == request.tsk_name:
                    tsk_ls[ls_index].remove(i)
                    son.save_tsk_ls(tsk_ls)
                    break

            self.history.append(request)
            self.del_hs()


    def change_desc(self, request):
        ls_ls = son.open_ls_ls()

        ls_exists = exists.ls(request.ls_name, ls_ls)
        if not ls_exists:
            return

        tsk_ls = son.open_tsk_ls()
        tsk_exist = exists.tsk(request.ls_name, request.tsk_name, ls_ls, tsk_ls)

        if not tsk_exist:
            if not fn.chc_tsk_del_history(request, self.history):
                ls_index = 0
                for i in ls_ls:
                    if i["name"] == request.ls_name:
                        break
                    ls_index += 1

                d = {
                    "name": request.tsk_name,
                    "desc": request.ending,
                    "completed": False
                }

                tsk_ls[ls_index].append(d)

                son.save_tsk_ls(tsk_ls)

                self.history.append(request)
                self.del_hs()

            return

        similar_edits = fn.chc_tsk_history(request, self.history)

        for i in similar_edits:
            a = comp_tm(i.time, request.time)
            if a == "second time is older":
                return

        ls_index = 0
        for i in ls_ls:
            if i["name"] == request.ls_name:
                break
            ls_index += 1

        tsk_index = 0
        for i in tsk_ls[ls_index]:
            if i["name"] == request.tsk_name:
                tsk_ls[ls_index][tsk_index]["desc"] = request.ending
                son.save_tsk_ls(tsk_ls)
                break
            tsk_index += 1
        self.history.append(request)
        self.del_hs()

    def change_name(self, request):
        ls_ls = son.open_ls_ls()

        ls_exists = exists.ls(request.ls_name, ls_ls)
        if not ls_exists:
            print("D")
            return

        tsk_ls = son.open_tsk_ls()
        tsk_exist = exists.tsk(request.ls_name, request.tsk_name, ls_ls, tsk_ls)

        if not tsk_exist:
            print("C")
            return

        similar_edits = fn.chc_tsk_history(request, self.history)

        for i in similar_edits:
            a = comp_tm(i.time, request.time)
            print(a)
            if a == "second time is older":
                print("B")
                return

        ls_index = 0
        for i in ls_ls:
            if i["name"] == request.ls_name:
                break
            ls_index += 1

        tsk_index = 0

        for i in tsk_ls[ls_index]:
            if i["name"] == request.tsk_name:
                tsk_ls[ls_index][tsk_index]["name"] = request.ending
                son.save_tsk_ls(tsk_ls)
                break
            tsk_index += 1

        self.history.append(request)
        self.del_hs()

    def change_state(self, request):
        ls_ls = son.open_ls_ls()

        ls_exists = exists.ls(request.ls_name, ls_ls)
        if not ls_exists:
            print("ls")
            return

        tsk_ls = son.open_tsk_ls()
        tsk_exist = exists.tsk(request.ls_name, request.tsk_name, ls_ls, tsk_ls)

        if not tsk_exist:
            print("tsk")
            return

        similar_edits = fn.chc_tsk_history(request, self.history)

        print(similar_edits)

        for i in similar_edits:
            a = comp_tm(i.time, request.time)
            if a == "second time is older":
                print("age ")
                # i.time.print_all()
                # print("what")
                # request.time.print_all()
                return

        if tsk_exist:
            ls_index = 0
            for i in ls_ls:
                if i["name"] == request.ls_name:
                    break
                ls_index += 1

            tsk_index = 0

            for i in tsk_ls[ls_index]:
                if i["name"] == request.tsk_name:
                    print(request.ending)
                    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
                    # if request.ending[0] == "T":
                    if request.ending == "True":
                        tsk_ls[ls_index][tsk_index]["completed"] = True
                        print("im here")
                    else:
                        tsk_ls[ls_index][tsk_index]["completed"] = False
                        print("im in else")

                    son.save_tsk_ls(tsk_ls)
                    break
                tsk_index += 1

        self.history.append(request)
        self.del_hs()
