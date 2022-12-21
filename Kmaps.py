import copy


def opt_function_reduce(l1, l2):
    # CONVERTS THE UPPERCASE LETTERS TO DASHED LITERALS
    def conversion(string):
        x1 = ''
        for g in range(0, len(string)):
            if string[g].isupper():
                x1 += string[g].lower() + "'"
            else:
                x1 += string[g]
        return x1

    # DELETES HASH FROM A GIVEN STRING
    def del_hash(s):
        l = ''
        n1 = len(s)
        for i in range(0, n1):
            if s[i] != '#':
                l += s[i]
        return l

    # PREPARES THE STRING TO PERFORM XOR OPERATION
    def str_to_num(a):
        l = ''
        i = 0
        while i < len(a):
            if a[i].isupper():
                l += '0'
                i += 1
            elif a[i] == '#':
                l += '2'
                i += 1
            else:
                l += '1'
                i += 1
        return (l)

    # CONVERTS THE DASHED LITERALS TO CORRESPONDING UPPERCASE LETTERS
    def reverse_conversion(a):
        i = 0
        l = ''
        while i < len(a):
            if i != len(a) - 1:
                if a[i + 1] == "'":
                    l += a[i].upper()
                    i += 2
                else:
                    l += a[i]
                    i += 1
            else:
                l += a[i]
                i += 1
        return l

    # GIVES THE XOR OF TWO BINARY STRINGS
    def xor(a, b):
        n = len(a)
        ans = ""
        for i in range(n):
            if (a[i] == b[i]):
                ans += "0"
            else:
                ans += "1"
        return ans

    # SIMPLFIES THE ONE XOR LIST TILL MINIMUM SIMPLIFICATION
    val = []  # val IS THE SIMPLIFIED LIST AT EACH ITERATION
    xor_list = []
    yet_another = []

    def simplify(lis):
        yet_another.append(lis)
        n1 = len(lis)
        before_list = lis
        for i in range(0, n1):
            len1 = copy.deepcopy(val)
            if '#' in lis[i]:
                i1 = str(lis[i]).index('#')
                for j in range(i + 1, n1):
                    if '#' in lis[j]:
                        i2 = str(lis[j]).index('#')
                        if i1 == i2 and len(lis[i]) == len(lis[j]):
                            answer = xor(str_to_num(lis[i]), str_to_num(lis[j]))
                            answer = str(answer)
                            if answer.count('1') == 1:
                                xor_list.append(lis[i])
                                xor_list.append(lis[j])
                                q = answer.index('1')
                                a1 = str(lis[i]).replace(lis[i][q], '#')
                                val.append(a1)
                if val == len1:
                    if lis[i] not in xor_list and lis[i] not in val:
                        val.append(lis[i])
            else:
                val.append(lis[i])
        # print(val)

        if val != before_list:
            return simplify(val)
        else:

            return (val)

    def f(fun_True, fun_DC):
        xor_list_sec = []
        for I in range(0, len(fun_True)):
            fun_True[I] = reverse_conversion(fun_True[I])
        for J in range(0, len(fun_DC)):
            fun_DC[J] = reverse_conversion(fun_DC[J])
        list1 = fun_True + fun_DC
        x = []  # THIS IS A LIST WHICH CONTAINS EVERY INPUT IN THE BINARY STRING FORMAT
        n1 = len(list1)
        for t in range(0, n1):
            x.append(str_to_num(list1[t]))
        n2 = len(x)
        fin = []
        for i in range(0, len(fun_True)):
            init = copy.deepcopy(fin)  # INITIALISES THE fin list IN ORDER TO COMPARE IT WITH THE NEW ONE
            for j in range(i + 1, n2):
                ans = xor(x[i], x[j])
                ans = str(ans)
                if ans.count('1') == 1:
                    q = ans.index('1')
                    a1 = str(list1[i]).replace(list1[i][q], '#')
                    fin.append(a1)
                    if list1[i] not in xor_list_sec:
                        xor_list_sec.append(list1[i])
                    if list1[j] not in xor_list_sec:
                        xor_list_sec.append(list1[j])
                    j = 0
            if fin == init:
                if list1[i] not in xor_list_sec:
                    fin.append(list1[i])
        # print(fin)
        fin = simplify(fin)

        def intermediate2(fin):
            global to_append
            n32 = len(fin)
            del_hash_list = []
            for bb in range(0, n32):
                del_hash_list.append(del_hash(fin[bb]))
            answer_list = []
            for m1 in range(0, len(fun_True)):
                to_check = []
                for m2 in range(0, len(del_hash_list)):
                    if set(del_hash_list[m2]).intersection(reverse_conversion(fun_True[m1])) == set(del_hash_list[m2]):
                        to_check.append(del_hash_list[m2])
                min_i = 0
                for m3 in range(0, len(to_check)):
                    if len(to_check[m3]) < len(to_check[min_i]):
                        min_i = m3
                answer_list.append(to_check[min_i])
                answer_list = list(set(answer_list))
            # print(answer_list)
            # THIS PART FINDS THE CELLS CORRESPONDING TO EACH REGION
            if answer_list==['']:
                return None
            major_list = []
            FINAL = []
            for i4 in range(0, len(answer_list)):
                minor_list = []
                for j4 in range(0, len(fun_True)):
                    if set(answer_list[i4]).intersection(set(reverse_conversion(fun_True[j4]))) == set(answer_list[i4]):
                        minor_list.append(fun_True[j4])
                major_list.append(minor_list)
            # print(major_list)
            # WE TAKE INTERSECTION OF ONE REGION WITH ALL OTHER REGIONS AND THEN TAKE UNION OF ALL THE INTERSECTIONS
            # IF THE UNION TURNS OUT TO BE SAME AS THE REGION WE APPEND THAT REGION TO THE DISCARD LIST.
            # ELSE WE APPEND IT TO THE FINAL LIST
            discard_list = []
            for i5 in range(0, len(major_list)):
                int_list = []
                for j5 in range(0, len(major_list)):
                    if i5 != j5:
                        if answer_list[j5] not in discard_list:
                            to_append = list(set(major_list[i5]).intersection(set(major_list[j5])))
                        # print(to_append)
                        int_list.append(to_append)
                # for i6 in range(0,len(int_list))
                # print(int_list)
                res = set()
                for i6 in range(0, len(int_list)):
                    res = res.union((int_list[i6]))
                # print(res)
                if res != set(major_list[i5]):
                    FINAL.append(conversion(answer_list[i5]))
                else:
                    discard_list.append(answer_list[i5])
            # print(FINAL)
            # print(discard_list)
            TO_BE_RETURNED = []
            for t10 in FINAL:
                TO_BE_RETURNED.append(t10)
            new_list = []
            for i7 in range(0, len(answer_list)):
                new_list.append(conversion(answer_list[i7]))
                # ----------------------------------------DEMO PART-------------------------------------------------------
            # WE GIVE THE REGIONS DELETED
            # WE GIVE THE REGIONS CORRESPONDING TO THE DELETED TERMS
            helper_list=[]
            final_helper_list=[]
            print('DELETED REGIONS.................')
            for i8 in range(len(FINAL)):
                (new_list.remove(FINAL[i8]))
            print(new_list)
            print('DELETED TERMS...................')
            for i9 in range(0,len(new_list)):
                maj_list=[]
                ind=answer_list.index(reverse_conversion(new_list[i9]))
                print(new_list[i9],end='')
                print('---->',end='')
                # print((major_list[ind]))
                # maj_list=copy.deepcopy(major_list[ind])

                for t7 in major_list[ind]:
                    maj_list.append(t7)
                for j10 in range(0,len(maj_list)):
                    # print(maj_list[ind])
                    final_helper_list.append(conversion(maj_list[j10]))
                print(final_helper_list)
                helper_list+=major_list[ind]

            # print(helper_list)
                # print(FINAL)
            print('REGIONS CONTAINING DELETED TERMS...............')
            for i10 in range(0,len(helper_list)):
                region=[]
                for i11 in range(0,len(FINAL)):
                    if set((helper_list[i10])).intersection(set(reverse_conversion(FINAL[i11])))==set((reverse_conversion(FINAL[i11]))):
                        region.append(FINAL[i11])
                new_variable=helper_list[i10]
                print(conversion(new_variable),end='')
                print('-------->',end='')
                print(region)

            return TO_BE_RETURNED

        return intermediate2(fin)

    return f(l1, l2)


# print(opt_function_reduce(["a'b'c", "a'bc", "a'bc'", "ab'c'"], ["abc'"]))
# print(opt_function_reduce(["a'bc'd'", "abc'd'", "a'b'c'd", "a'bc'd", "a'b'cd"], ["abc'd"]))
# print(opt_function_reduce(["a'b'c'd", "a'b'cd", "a'bc'd", "abc'd'", "abc'd", "ab'c'd'", "ab'cd"],["a'bc'd'", "a'bcd", "ab'c'd"]))
# print(opt_function_reduce(["a'b'c'd'e'", "a'bc'd'e'", "abc'd'e'", "ab'c'd'e'", "abc'de'", "abcde'", "a'bcde'", "a'bcd'e'", "abcd'e'","a'bc'de", "abc'de", "abcde", "a'bcde", "a'bcd'e", "abcd'e", "a'b'cd'e", "ab'cd'e"], []))
# print(opt_function_reduce(['abcde', "ab'c'de", "ab'cde"], ["ab'c'de'"]))
# print(opt_function_reduce(["a'b'c'", "a'b'c", "a'bc'", "a'bc"], ["ab'c'", "abc'", "ab'c", "abc"]))
# print(opt_function_reduce(["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"],["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]))
# print(opt_function_reduce(["a'bc'defgh", "a'bc'd'efgh", "abc'd'efgh", "abc'defgh", "a'bc'def'gh", "a'bc'd'ef'gh", "abc'd'ef'gh","abc'def'gh"], []))
# print(opt_function_reduce(["a'b", "a'b'"], []))
# print(opt_function_reduce( ["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"],["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]))
# # ------------------------------------------TEST CASES FOR 2 VARIABLES-----------------------------------------------------
# print(opt_function_reduce(["a'b'"], []))
# print(opt_function_reduce(["a'b'"], ["a'b"]))
# print(opt_function_reduce(["a'b'", "ab'"], ["a'b"]))
# # ALL ARE ONE
# print(opt_function_reduce(["a'b'", "a'b", "ab'", "ab"], []))
# -----------------------------------------TEST CASES FOR 3 VARIABLES-----------------------------------------------------------
# print(opt_function_reduce(["a'b'c'", "a'b'c", "a'bc", "a'bc'"], ["ab'c'", "ab'c"]))
# print(opt_function_reduce(["a'b'c'", "a'b'c"], ["ab'c'", "ab'c"]))
# print(opt_function_reduce(["a'b'c'd'e'", "a'b'cd'e", "a'b'cde'", "a'bc'd'e'", "a'bc'd'e", "a'bc'de", "a'bc'de'", "ab'c'd'e'", "ab'cd'e'"],["abc'd'e'", "abc'd'e", "abc'de", "abc'de'"]))
# print(opt_function_reduce(["a'b'c'd'e'f'", "a'b'c'd'e'f", "a'b'cd'e'f'", "a'b'cd'e'f", "a'bc'd'e'f'", "a'bcd'e'f'", "ab'c'd'ef", "abc'de'f'","abc'de'f", "abc'def'", "abc'def"], ["abcde'f'", "abcde'f", "abcdef'", "abcdef"]))
# print(opt_function_reduce(["a'b'c'd'e'f'", "a'b'c'd'e'f", "a'b'cd'e'f'", "a'b'cd'e'f", "a'b'cd'ef'", "a'b'cd'ef", "a'b'cde'f'", "a'b'cde'f","a'b'cdef'", "a'b'cdef", "a'bc'd'e'f'", "a'bcd'e'f'", "ab'c'd'ef", "abc'de'f'", "abc'de'f", "abc'def'", "abc'def"],["abcde'f'", "abcde'f", "abcdef'", "abcdef"]))
# print(opt_function_reduce(['abcd', "ab'c'd", "ab'cd"], ["abcd'"]))
# print(opt_function_reduce(["a'bc'de", "a'bcde"], ["a'b'cde", "a'b'cde'"]))
# print(opt_function_reduce(["a'bcdef", "a'b'c'def", "a'b'c'd'e'f'", "a'b'c'd'ef", "a'b'c'd'e'f", "a'b'cdef"],["ab'cd'ef", 'abcdef', "ab'cdef", "ab'cd'e'f"]))
# print(opt_function_reduce(['abcde', "ab'c'de", "ab'cde"], ["ab'c'de'"]))
# print(opt_function_reduce(["a'b'c'd'e'", "a'bc'd'e'", "abc'd'e'", "ab'c'd'e'", "abc'de'", "abcde'","a'bcde'", "a'bcd'e'", "abcd'e'", "a'bc'de", "abc'de", "abcde","a'bcde", "a'bcd'e", "abcd'e", "a'b'cd'e", "ab'cd'e"],[]))
# print(opt_function_reduce(["a'b'c'd'e'f'", "a'b'c'd'ef'", "a'b'c'd'ef", "a'b'c'de'f", "a'bc'def", "a'bc'd'ef", "a'bcd'ef'", "a'bcd'e'f'", "a'bcde'f'", "a'b'cd'e'f", "a'b'cde'f", "ab'cd'e'f", "abcde'f", "ab'cd'ef", "abcd'ef'", "abc'd'ef'", "ab'c'd'e'f'", "ab'c'de'f'"],["a'b'c'd'e'f", "a'bc'de'f", "a'bc'd'e'f", "a'bcdef'", "abcd'e'f'", 'abcdef', "ab'c'd'ef'", "ab'c'def'", "abc'd'e'f'"]))
# print(opt_function_reduce(["a'b'c'de'fg'h", "a'bc'de'f'g'h'", "a'b'c'de'fgh", "a'bc'de'f'gh'", "a'b'c'defgh", "a'bc'def'gh'", "a'b'c'defg'h", "a'bc'def'g'h'", "ab'cd'e'f'gh", "ab'cd'e'fgh", "ab'cd'e'fgh'", "ab'cde'fgh'", "ab'cd'ef'gh", "ab'cd'efgh", "ab'cd'efgh'", "ab'cdefgh'", "ab'cd'ef'g'h", "ab'cd'efg'h", "ab'cd'efg'h'", "ab'cdefg'h'", "ab'c'd'ef'g'h", "ab'c'd'efg'h", "ab'c'd'efg'h'", "ab'c'defg'h'", "abcde'f'gh", "abcde'fgh", "abcde'fgh'", "abcd'e'fgh'", "abcdef'gh", 'abcdefgh', "abcdefgh'", "abcd'efgh'", "abcdef'g'h", "abcdefg'h", "abcdefg'h'", "abcd'efg'h'", "abc'def'g'h", "abc'defg'h", "abc'defg'h'", "abc'd'efg'h'"],["a'b'c'de'f'g'h", "a'b'c'de'f'g'h'", "a'b'c'de'f'gh", "a'b'c'de'f'gh'", "a'b'c'def'gh", "a'b'c'def'gh'", "a'b'c'def'g'h", "a'b'c'def'g'h'"]))