from tm import Time
from tsks import Tsk_Exec
from tsk_request import Tsk
from ls_request import Ls
from lss import Ls_exec

tsk_exec = Tsk_Exec()
ls_exec = Ls_exec()


class Translate:
    tokens = list()
    for i in range(255):
        tokens.append("done")
    tk = 0

    def ping(self):

        self.tk += 1

        if self.tk == 256:
            self.tk = 0

        while self.tokens[self.tk - 1] == "pending":
            self.tk += 1

        a = str(self.tk)
        while len(a) != 3:
            a = "0" + a
        self.tokens[self.tk - 1] = "pending"
        return a

    def tsk(self, query):

        print(query)

        action = query[4] + query[5]
        time = query[7] + query[8] + query[9] + query[10] + query[11] + query[12] + query[13] + query[14] + query[15] + query[16] + query[17] + query[18] + query[19] + query[20] + query[21] + query[22] + query[23] + query[24] + query[25] + query[26] + query[27] + query[28] + query[29] + query[30] + query[31] + query[32]
        t = Time(time)
        token = query[34] + query[35] + query[36]
        ls_name = query[39:query.find("'-'")]
        tsk_name = query[query.find("'-'") + 3:query.find("':")]
        ending = query[query.find("':") + 3: -1]

        if self.tokens[int(token) - 1] == "done":
            return "done"

        request = Tsk(action, t, token, ls_name, tsk_name, ending)
        if action == "ad":
            h = tsk_exec.ad(request)
            if h == "O:":
                ls_exec.myb_add(request)
                h = tsk_exec.ad(request)

        elif action == "rm":
            tsk_exec.del_tsk(request)
        elif action == "ct":
            tsk_exec.change_name(request)
        elif action == "cd":
            tsk_exec.change_desc(request)
        elif action == "cs":
            tsk_exec.change_state(request)

        self.tokens[int(token) - 1] = "done"

        return "done"

    def ls(self, query):
        action = query[3] + query[4]
        time = query[6] + query[7] + query[8] + query[9] + query[10] + query[11] + query[12] + query[13] + query[14] + query[15] + query[16] + query[17] + query[18] + query[19] + query[20] + query[21] + query[22] + query[23] + query[24] + query[25] + query[26] + query[27] + query[28] + query[29] + query[30] + query[31]
        token = query[33:36]
        ls_name = query[38:query.find("':")]
        t = Time(time)
        alarm = query[query.find("':'") + 2:]

        request = Ls(action, t, token, ls_name, alarm)

        print(token)

        if self.tokens[int(token) - 1] == "done":
            return "done"

        if action == "ad":
            ls_exec.add(request)
            print("#################################")
        if action == "rm":
            ls_exec.del_ls(request)
        if action == "ca":
            ls_exec.chng_alarm(request)

        self.tokens[int(token) - 1] = "done"

        return "done"
