class Chc_exestance:
    def ls(self, ls_name, ls_ls):
        for i in ls_ls:
            if i["name"] == ls_name:
                return True

    def tsk(self, ls_name, tsk_name, ls_list, tsk_list):
        ls_index = 0
        print(ls_list)
        print(tsk_list)
        for i in ls_list:
            if i["name"] == ls_name:
                print("==================================")
                print(ls_index)
                break
            ls_index += 1

        if ls_index > len(tsk_list) - 1:
            return False

        for i in tsk_list[ls_index]:
            if i["name"] == tsk_name:
                return True

        return False
