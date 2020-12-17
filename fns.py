class Fn:
    def chc_history(self, history, request):
        simlar_edits = list()
        for i in history:
            if request.action == i.action:
                if request.ls_name == i.ls_name:
                    simlar_edits.append(i)
        return simlar_edits

    def chc_tsk_history(self, request, history):
        simlar_edits = list()
        for i in history:
            if i.ls_name == request.ls_name and i.action == request.action and i.tsk_name == request.tsk_name:
                simlar_edits.append(i)

        return simlar_edits

    def chc_tsk_del_history(self, request, history):
        simlar_edits = list()
        for i in history:
            if i.ls_name == request.ls_name and i.action == "rm" and i.tsk_name == request.tsk_name:
                return True
        return False

    def chc_ls_del_hs(self, request, hs):
        for i in hs:
            if "rm" == i.action:
                if request.ls_name == i.ls_name:
                    return True
        return False



