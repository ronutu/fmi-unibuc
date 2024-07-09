import random
import re
import collections
import copy
import os
from graphviz import Digraph



InfiniteLong = 50  # control the length of the infinite E


def myfind(x,y):
    # select the index of x in y, the type of return is list
    return [a for a in range(len(y)) if y[a] == x]


# label the input file
Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])


def tokenize(code):
    # generate a token list of input text

    # ORDER MATTERS here: more complex tokens (e.g. >= are checked before >) to avoid incorrect parsing
    token_specification = [
        ('NUMBER_FLOAT',  r'\d+\.\d+'),    # Float number
        ('NUMBER',        r'\d+'),         # Integer number

        ('OPERATOR_NOT_EQUAL', r'\!\='),   # Not equal operator (!=)
        ('OPERATOR_EQUAL', r'\=\='),       # Equal operator (==)
        ('OPERATOR_LESS_EQUAL', r'\<\='),  # Less or equal operator (<=)
        ('OPERATOR_GREATER_EQUAL', r'\>\='),  # Greater or equal operator (>=)

        ('ASSIGN',        r'='),           # Assignment operator '='
        ('OPERATOR_MULTIPLY',        r'\*'),     # OPERATOR_MULTIPLY operator '*'
        ('END',           r';'),           # Statement terminator ';'
        ('DELAY',         r':'),           # Statement delay ':'
        ('ID',            r'[\w]+'),       # Identifiers
        ('L_BRACE',       r'\('),          # Left brace '('
        ('R_BRACE',       r'\)'),          # Right brace ')'
        ('L_CURLY_BRACE', r'{'),           # Left curly brace '{'
        ('R_CURLY_BRACE', r'}'),           # Right curly brace '}'
        ('L_BRACKET', r'\['),              # Left bracket (straight brace) '['
        ('R_BRACKET', r'\]'),              # Right bracket (straight brace) ']'
        ('COLUMN',        r','),           # column ','

        ('PROD_DISTRIB_SEPARATOR', r'->'), # Program production and distribution component separator sign '->'
        ('OPERATOR_POWER', r'\^'),         # Power operator (^)

        ('NEWLINE',       r'\n'),          # Line endings
        ('COMMENT',       r'#'),           # Comment (anything after #, up to the end of the line is discarded)
        ('SKIP',          r'[ \t]+'),      # Skip over spaces and tabs
        ('CONNECT',     r'\-'),             # Neuronal connections
        ('OPERATOR_ADD', r'\+'),  # Addition operator (+)
        ('NeuronalSTATE', r'\/'),           # Neuronal state
        ('MISMATCH',      r'.'),           # Any other character
    ]
    # join all groups into one regex expr; ex:?P<NUMBER>\d+(\.\d*)?) | ...
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    in_comment = False
    # iteratively search and return each match (for any of the groups)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup  # last group name matched
        value = mo.group(kind)  # the last matched string (for group kind)
        # print("kind = %s, value = %s" % (kind, value))
        if kind == 'COMMENT':
            in_comment = True
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            in_comment = False  # reset in_comment state
        elif kind == 'SKIP':
            pass
        elif (kind == 'MISMATCH') and (not in_comment):
            raise RuntimeError('%r unexpected on line %d' % (value, line_num))
        else:
            # skip normal tokens if in comment (cleared at the end of the line)
            if in_comment:
                continue
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)


# Random combination
def product_sequence(rule_use_all):
    sum_count = 1
    rule_use = []

    for i in range(len(rule_use_all)):
        sum_count *= len(rule_use_all[i])
    while len(rule_use) != sum_count:
        temp = []
        for i in range(len(rule_use_all)):
            tempIndex = int(random.uniform(0, len(rule_use_all[i])))
            temp.append(rule_use_all[i][tempIndex])
        i=0
        while(i < len(rule_use)):
            if rule_use[i] == temp:
                break
            i += 1
        if i == len(rule_use):
            rule_use.append(temp)
    return sum_count,rule_use

# return the index of rule_use
def rule_index(rule_use):
    rule_use_local = rule_use.copy()
    sum_count = len(rule_use_local)
    index = []
    for i in range(sum_count):
        index.append([])
        for j in rule_use_local[i]:
            if j[-1] == 's':
                j = j[0]+'-0'
            index[i].append(int(j[-1])-1)
    return index

#generate a class
class Neural():
    def __init__(self):
        pass

#snp system
class SNP_System():

    def __init__(self):
        self.Neural = Neural() #store the neural
        self.Number = [] #the number of neural
        self.rule = []  #the rule
        self.synapses = [] #the Connection relationship
        self.initial = [] #Initial form
        self.out = []   #the output neural
        self.draw_flag = 0 #the flag of form transfer diagram

    def runSimulationStep(self,system,filename = None):
        use_rule_all = []
        copy_sys = copy.deepcopy(system)
        copy_init_static_delay = copy_sys.initial.delayStep.copy()
        copy_init_static_impulse = copy_sys.initial.impulseNum.copy()
        copy_init = copy_sys.initial.delayStep

        for i in range(copy_sys.Number):
            if copy_sys.Neural.__dict__['Neural_%d' % (i + 1)].state == 0:
                pass
            else:
                copy_sys.Neural.__dict__['Neural_%d' % (i + 1)].state -= 1
        for i in range(len(copy_init)):
            if copy_init[i] >= 1:
                copy_init[i] -= 1

        temp_save_state = []
        #use the rule
        for neural_i in range(copy_sys.Number):
            temp_save_state.append([])
            if copy_init_static_delay[neural_i] == 0:
                for ruleIndex in range(copy_sys.Neural.__dict__['Neural_%d' % (neural_i+1)].NeuralNumber):
                    temp_save_state[neural_i].append([])
                    if ((copy_init_static_impulse[neural_i] in copy_sys.Neural.__dict__['Neural_%d' % (neural_i + 1)].__dict__['Index_%d' % (ruleIndex + 1)].E.power) and (copy_sys.Neural.__dict__['Neural_%d' % (neural_i + 1)].__dict__['Index_%d' % (ruleIndex + 1)].Eject.power <= copy_init_static_impulse[neural_i])):
                        temp_save_state[neural_i][ruleIndex].append((copy_sys.initial.impulseNum[neural_i]-copy_sys.Neural.__dict__['Neural_%d' % (neural_i + 1)].__dict__['Index_%d' % (ruleIndex + 1)].Eject.power))
                        temp_save_state[neural_i][ruleIndex].append(copy_sys.Neural.__dict__['Neural_%d' % (neural_i + 1)].__dict__['Index_%d' % (ruleIndex + 1)].Recieve.power)
                        temp_save_state[neural_i][ruleIndex].append(copy_sys.Neural.__dict__['Neural_%d' % (neural_i + 1)].__dict__['Index_%d' % (ruleIndex + 1)].delay)
        # print(temp_save_state)
        circle_return = 0 #the flag of whether use the rule or not
        for i in range(len(temp_save_state)):
            for j in range(len(temp_save_state[i])):
                if len(temp_save_state[i][j]) != 0:
                    circle_return += 1
        circle_return_delay = 0 #the flag of whether the neural is closed or not
        for i in range(len(copy_init_static_delay)):
            if copy_init_static_delay[i] != 0:
                circle_return_delay += 1
        if ((circle_return==0)and(circle_return_delay==0)):
            return 0,[],[],[],[]

        #describe the used rules
        for i in range(len(temp_save_state)):
            use_rule_all.append([])
            rule_0 = 0
            for j in range(len(temp_save_state[i])):
                if len(temp_save_state[i][j]) == 3:
                    use_rule_all[i].append('%d-%d'%((i+1),(j+1)))
                else:
                    rule_0 += 1
            if rule_0 == len(temp_save_state[i]):
                if len(temp_save_state[i])==0:
                    use_rule_all[i].append('%d-s' % (i + 1))
                else:
                    use_rule_all[i].append('%d-%d' % ((i + 1), 0))
        # print(use_rule_all)
        #generate the all used rules combination
        sum_count,rule_use_index = product_sequence(use_rule_all)
        # print(rule_use_index)
        #obtain the index of rules
        index = rule_index(rule_use_index)

        # the rules is used or not,-1 represent not
        save_state = []
        for i in range(sum_count):
            save_state.append([])
            for j in range(len(index[i])):
                if index[i][j] == -1:
                    save_state[i].append([])
                    continue
                save_state[i].append(temp_save_state[j][index[i][j]])
        # print(save_state)

        # copy
        for i in range(sum_count):
            globals()['system%i' %i] = copy.deepcopy(copy_sys)
        for i in range(sum_count):
            for j in range(globals()['system%i' %i].Number):
                if len(save_state[i][j])==0:
                    continue
                globals()['system%i' %i].Neural.__dict__['Neural_%d' % int(j+1)].retain =save_state[i][j][1]
                globals()['system%i' %i].Neural.__dict__['Neural_%d' % int(j + 1)].state = save_state[i][j][2]
                globals()['system%i' %i].initial.delayStep[j] = save_state[i][j][2]
                globals()['system%i' %i].initial.impulseNum[j] = save_state[i][j][0]

        #if d =0,then eject the former generation impulse
        for i in range(sum_count):
            for j in range(globals()['system%i' %i].Number):
                if globals()['system%i' %i].Neural.__dict__['Neural_%d' % int(j + 1)].state == 0:
                    eject_index = myfind((j + 1), globals()['system%i' %i].synapses.ejectNeural)
                    for m in range(len(eject_index)):
                        if globals()['system%i' %i].synapses.recieveNeural[eject_index[m]] == 'env':
                            continue
                        else:
                            if globals()['system%i' %i].Neural.__dict__['Neural_%d' %(globals()['system%i' %i].synapses.recieveNeural[eject_index[m]])].state == 0:
                                globals()['system%i' %i].initial.impulseNum[globals()['system%i' %i].synapses.recieveNeural[eject_index[m]]-1] += globals()['system%i' %i].Neural.__dict__['Neural_%d' % (j + 1)].retain
                    globals()['system%i' %i].Neural.__dict__['Neural_%d' % (j + 1)].retain = 0
        #for the form transfer
        initial = []
        for i in range(copy_sys.Number):
            initial.append('%d/%d'%(copy_init_static_impulse[i],copy_init_static_delay[i]))
        for i in range(sum_count):
            locals()['form%i' % i] = []
            for j in range(copy_sys.Number):
                locals()['form%i' % i].append('%d/%d' % (globals()['system%i' %i].initial.impulseNum[j], globals()['system%i' %i].initial.delayStep[j]))
        form_trans = ''
        for i in range(sum_count):
            form_trans += '%s->%s use rules:%s\n'%(initial,locals()['form%i' % i],rule_use_index[i])
        form_trans = re.sub("'",'',form_trans)
        with open('output/result_%s.txt'%filename, 'a+') as f:
            f.write(form_trans)

        returnList =[]
        return_state =[]
        for i in range(sum_count):
            returnList.append(globals()['system%i' % i])
            return_state.append(locals()['form%i' % i])

        #eliminate the symbol of ''
        initial = re.sub("'", '', str(initial))
        for i in range(sum_count):
            rule_use_index[i] = re.sub("'",'',str(rule_use_index[i]))
            return_state[i] = re.sub("'", '', str(return_state[i]))
        return sum_count,rule_use_index,returnList,initial,return_state


    def runSimulation(self,system,step=1,filename = None):
        if step < 1:
            raise ValueError('step must more than 1')
        node_count = 0
        returnSNP = []
        sum_count =1
        returnSNP.append(system)
        record_out_step=0 #record the step
        count_th =0
        while (step >= 1):
            step -= 1
            record_out_step += 1
            itera = count_th
            sum_counts_sub = 0
            if count_th != 0:
                with open('output/result_%s.txt'%filename, 'a+') as f:
                    f.write('\n')
            while(itera < sum_count):
                sum_counts_temp, rule_use_index_sub, returnList_sub,initial,return_state = self.runSimulationStep(returnSNP[itera],filename)

                # Painting form transfer diagram
                try:
                    if self.draw_flag == 0:
                        self.draw_flag = 1
                        from graphviz import Digraph
                        dot = Digraph(comment='The Round Table')
                        dot.node('returnSNP_%d' % node_count, label='%s' % initial, shape='box')

                    for dot_i in range(sum_counts_temp):
                        node,label = return_node_label(dot)
                        node_index_initial = myfind(initial, label)[0]
                        if return_state[dot_i] not in label:
                            node_count += 1
                            dot.node('returnSNP_%d' % node_count, label='%s' % return_state[dot_i], shape='box')
                            dot.edge('returnSNP_%d'%node_index_initial, 'returnSNP_%d' % node_count, label='%s'%rule_use_index_sub[dot_i]+'%d'%record_out_step)
                        else:
                            node_index = myfind(return_state[dot_i], label)
                            for node_index_i in range(len(node_index)):
                                dot.edge('returnSNP_%d' % node_index_initial, 'returnSNP_%d' % node_index[node_index_i],label='%s' % rule_use_index_sub[dot_i]+'%d'%record_out_step)

                except:
                    print('not found moudle graphviz')

                sum_counts_sub += sum_counts_temp
                returnSNP.extend(returnList_sub)
                itera += 1
                count_th = itera
            if sum_counts_sub==0:
                record_out_step -= 1
            initial_returnSNP = []
            for i in range(len(returnSNP)):
                initial_returnSNP.append([])
                for k in range(returnSNP[i].Number):
                    initial_returnSNP[i].append('%d/%d' % (returnSNP[i].initial.impulseNum[k], returnSNP[i].initial.delayStep[k]))
            # delet the same snp
            delete_index = []
            for i in range(len(initial_returnSNP)):
                j = i + 1
                for k in range(j, len(initial_returnSNP)):
                    if initial_returnSNP[i] == initial_returnSNP[k]:
                        delete_index.append(k)
            delete_index = list(set(delete_index))
            delete_index.sort(reverse = True)
            for i in range(len(delete_index)):
                del returnSNP[delete_index[i]]
                sum_counts_sub -= 1
            sum_count += sum_counts_sub

            if sum_counts_sub <= 0 or step == 0:
                try:
                    from graphviz import Digraph
                    # dot.view()
                    dot.render('output/simulation_result', view=True)
                except:
                    print(' ')
                break
        return record_out_step,returnSNP

#rules
class Rule():

    def __init__(self):
        self.Neural = []
        self.newNeural = []

# Connection relationship
class Synapses():
    def __init__(self):
        self.synap = []
        self.ejectNeural = []
        self.recieveNeural = []

#Initial form
class Initial():
    def __init__(self):
        self.init = []
        self.impulseNum =[]
        self.delayStep = []

#obtain the node and label of dot
def return_node_label(dot):
    dot_body_copy = dot.body.copy()
    record_edge = []
    for i in range(len(dot_body_copy)):
        j = 0
        while (j < len(dot_body_copy[i])):
            if dot_body_copy[i][j] == '-':
                if dot_body_copy[i][j + 1] == '>':
                    record_edge.append(i)
            j += 1
    record_edge.sort(reverse=True)
    for i in range(len(record_edge)):
        del dot_body_copy[record_edge[i]]
    record_node = []
    for i in range(len(dot_body_copy)):
        j = 0
        filee = ''
        while (j < len(dot_body_copy[i])):
            if dot_body_copy[i][j] == '[' and dot_body_copy[i][j + 1] == 'l':
                j += 1
                while (dot_body_copy[i][j] != '='):
                    filee += dot_body_copy[i][j]
                    j += 1
            j += 1
        if filee == 'label':
            record_node.append(i)
    node = []
    label = []
    for i in range(len(dot_body_copy)):
        if i in record_node:
            j = 0
            temp_node = ''
            temp_label = ''
            while (j < len(dot_body_copy[i])):
                if dot_body_copy[i][j] == '\t':
                    j += 1
                    while (dot_body_copy[i][j] != ' '):
                        temp_node += dot_body_copy[i][j]
                        j += 1
                if dot_body_copy[i][j] == '"':
                    j += 1
                    while (dot_body_copy[i][j] != '"'):
                        temp_label += dot_body_copy[i][j]
                        j += 1
                j += 1
            node.append(temp_node)
            label.append(re.sub("'",'',temp_label))
    return node,label

#Shallow recognition input string
def process_tokens(tokens,parent, index):
    result = parent
    prev_token = tokens[index]

    while (index < len(tokens)):
        token = tokens[index]

        if (type(parent) == SNP_System):
            if (token.type == 'ASSIGN'):
                if (prev_token.value == 'neuronNum'):
                    index, result.Number = process_tokens(tokens, int(), index + 1);

                # if the prev_token is the name of a membrane
                elif (prev_token.value == 'rule'):
                    index, result.rule = process_tokens(tokens, Rule(), index + 1);

                elif (prev_token.value == 'synapses'):
                    index, result.synapses  = process_tokens(tokens, Synapses(), index + 1);

                elif (prev_token.value == 'initial'):
                    index, result.initial = process_tokens(tokens, Initial(), index + 1);

                else:
                    raise RuntimeError("Unexpected token '%s' on line %d" % (prev_token.value, prev_token.line))

        elif (type(parent) == Rule):
            if (token.type not in ('L_CURLY_BRACE', 'R_CURLY_BRACE','MISMATCH','END')):
                parent.Neural.append(token)
            if (token.type == 'END'):
                return index, result;
            # else:
            #     raise RuntimeError("Unexpected token '%s' on line %d" % (token.value, token.line))

        elif (type(parent) == Synapses):
            if (token.type in ('ID', 'NUMBER', 'CONNECT','COLUMN','L_BRACKET', 'R_BRACKET')):
                parent.synap.append(token)

            elif (token.type == 'END'):
                return index, result;
            else:
                raise RuntimeError("Unexpected token '%s' on line %d" % (token.value, token.line))

        elif (type(parent) == Initial):
            if (token.type in ('NUMBER', 'L_BRACKET', 'R_BRACKET','NeuronalSTATE','COLUMN')):
                parent.init.append(token)

            elif (token.type == 'END'):
                return index, result;
            else:
                raise RuntimeError("Unexpected token '%s' on line %d" % (token.value, token.line))


        elif (type(parent) == int):
            if (token.type == 'NUMBER'):
                result = int(token.value);

        else:
            # process the token generally
            if (token.type == 'ASSIGN'):
                index, result = process_tokens(tokens, SNP_System(), index + 1);

        if (token.type == 'END'):
            return index, result;

        prev_token = token;
        index += 1
    return index, result

#generate the recognizable snp system for computation
def resultTOsystem(result):
    for i in range(1,result.Number+1):
        result.Neural.__dict__['Neural_%d' % i]= Neural()

# creat new distribute
    itera=0
    while (itera < len(result.rule.Neural)):
        if result.rule.Neural[itera].value == '(':
            result.rule.newNeural.append([])
            result.rule.newNeural[-1].append(result.rule.Neural[itera])
        elif result.rule.Neural[itera].value ==')':
            result.rule.newNeural[-1].append(result.rule.Neural[itera])
        elif result.rule.Neural[itera].value ==',' and result.rule.Neural[itera-1].value ==')':
            pass
        else:
            result.rule.newNeural[-1].append(result.rule.Neural[itera])
        itera += 1

#start in initial
    itera = 0
    while (itera < len(result.initial.init)):
        if (((result.initial.init[itera].value =='[') or (result.initial.init[itera].value ==','))and (result.initial.init[itera+1].type =='NUMBER')):
            itera += 1
            temp = ''
            while (result.initial.init[itera].type == 'NUMBER'):
                temp += result.initial.init[itera].value
                itera += 1
            result.initial.impulseNum.append(int(temp))
            itera -= 1

        if ((result.initial.init[itera].value =='/') and (result.initial.init[itera+1].type =='NUMBER')):
            itera += 1
            temp = ''
            while (result.initial.init[itera].type == 'NUMBER'):
                temp += result.initial.init[itera].value
                itera += 1
            result.initial.delayStep.append(int(temp))
            itera -= 1
        itera += 1
# end in initial

# start in synapses
    itera = 0
    while (itera < len(result.synapses.synap)):
        if (((result.synapses.synap[itera].value == '[') or (result.synapses.synap[itera].value == ',')) and (result.synapses.synap[itera + 1].type == 'NUMBER')):
            itera += 1
            temp = ''
            while (result.synapses.synap[itera].type == 'NUMBER'):
                temp += result.synapses.synap[itera].value
                itera += 1
            result.synapses.ejectNeural.append(int(temp))
            itera -= 1

        if ((result.synapses.synap[itera].value == '-')  and (result.synapses.synap[itera + 1].type == 'NUMBER')):
            itera += 1
            temp = ''
            while (result.synapses.synap[itera].type == 'NUMBER'):
                temp += result.synapses.synap[itera].value
                itera += 1
            result.synapses.recieveNeural.append(int(temp))
            itera -= 1
        elif ((result.synapses.synap[itera].value == '-')  and (result.synapses.synap[itera + 1].type == 'ID')):
            result.synapses.recieveNeural.append(result.synapses.synap[itera + 1].value)
        itera += 1
    for i in range(len(result.synapses.recieveNeural)):
        if(result.synapses.recieveNeural[i] == 'env'):
            result.out.append(result.synapses.ejectNeural[i])
# end in synapses

# start in rules
        for i in range(len(result.rule.newNeural)):
            itera = 0
            while (itera < len(result.rule.newNeural[i])):
                if ((result.rule.newNeural[i][itera].value == '(') and (result.rule.newNeural[i][itera + 1].type == 'NUMBER')):
                    itera += 1
                    tempINDEX = ''
                    while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                        tempINDEX += result.rule.newNeural[i][itera].value
                        itera += 1

                if ((result.rule.newNeural[i][itera].value == '-') and (result.rule.newNeural[i][itera + 1].type == 'NUMBER')):
                    itera += 1
                    tempSUBindex = ''
                    while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                        tempSUBindex += result.rule.newNeural[i][itera].value
                        itera += 1
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)] = Neural()
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E = Neural()
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power = []
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject = Neural()
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Recieve = Neural()
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].delay = 0
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].retain = 0
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].NeuralNumber = int(tempSUBindex)
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].state = result.initial.delayStep[int(tempINDEX)-1]

                if ((result.rule.newNeural[i][itera].value == ',') and (result.rule.newNeural[i][itera + 1].type == 'ID')):
                    itera += 1
                    tempSTR = result.rule.newNeural[i][itera].value
                    itera += 1
                    if (result.rule.newNeural[i][itera].value == '/'):
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.a = tempSTR
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power.append(1)

                    if (result.rule.newNeural[i][itera].value == '->'):
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.a = tempSTR
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.power = 1

                if ((result.rule.newNeural[i][itera].value == '^') and (result.rule.newNeural[i][itera + 1].type == 'NUMBER')):
                    itera += 1
                    temp = ''
                    while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                        temp += result.rule.newNeural[i][itera].value
                        itera += 1
                    if (result.rule.newNeural[i][itera].value == '/'):
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.a = tempSTR
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power.append(int(temp))
                    elif (result.rule.newNeural[i][itera].value == '->'):
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.a = tempSTR
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.power = int(temp)
                    else:
                        raise ValueError('Rule format is wrong')

                elif ((result.rule.newNeural[i][itera].value == '^') and (result.rule.newNeural[i][itera + 1].value == '[')):
                    itera += 1
                    Epower = []
                    EpowerFlag = []
                    while(result.rule.newNeural[i][itera ].value != ']'):
                        if result.rule.newNeural[i][itera].type != 'NUMBER':
                            itera += 1
                        if itera >len(result.rule.newNeural[i]):
                            raise ValueError('Rule format is wrong')
                        temp = ''
                        while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                            temp += result.rule.newNeural[i][itera].value
                            itera += 1
                        if result.rule.newNeural[i][itera].value == '*':
                            multi_temp = int(temp)
                            EpowerFlag = []
                            itera += 1
                            if result.rule.newNeural[i][itera].value =='-':
                                temp = ''
                                itera += 1
                                while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                                    temp += result.rule.newNeural[i][itera].value
                                    itera += 1
                                if temp != '':
                                    for multi in range(1, InfiniteLong):
                                        EpowerFlag.extend([multi*multi_temp-int(temp)])
                                else:
                                    raise ValueError('Rule format is wrong')
                            elif result.rule.newNeural[i][itera].value =='+':
                                temp = ''
                                itera += 1
                                while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                                    temp += result.rule.newNeural[i][itera].value
                                    itera += 1
                                if temp != '':
                                    for multi in range(1, InfiniteLong):
                                        EpowerFlag.extend([multi*multi_temp+int(temp)])
                                else:
                                    raise ValueError('Rule format is wrong')
                            elif result.rule.newNeural[i][itera].value ==',' or result.rule.newNeural[i][itera].value ==']':
                                for multi in range(2, InfiniteLong):
                                    EpowerFlag.extend([multi*multi_temp])
                            else:
                                raise ValueError('Rule format is wrong')
                        if temp != '':
                            Epower.append(int(temp))
                            Epower.extend(EpowerFlag)
                    Epower = list(set(Epower))
                    Epower = [Epower_i for Epower_i in Epower if Epower_i > 0]
                    itera += 1
                    if (result.rule.newNeural[i][itera].value == '/'):
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.a = tempSTR
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power.extend(Epower)
                    else:
                        raise ValueError('Rule format is wrong')

                if ((result.rule.newNeural[i][itera].value == '/') and (result.rule.newNeural[i][itera + 1].type == 'ID')):
                    itera += 1
                    tempSTR = result.rule.newNeural[i][itera].value
                    itera += 1
                    temp =''
                    if((result.rule.newNeural[i][itera].value =='^')and(result.rule.newNeural[i][itera + 1].type == 'NUMBER')):
                        itera += 1
                        while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                            temp += result.rule.newNeural[i][itera].value
                            itera += 1
                        if (result.rule.newNeural[i][itera].value == '->'):
                            result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.a = tempSTR
                            result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.power = int(temp)
                    elif ((result.rule.newNeural[i][itera].value =='->')and(result.rule.newNeural[i][itera + 1].type == 'ID')):
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.a = tempSTR
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.power = 1

                if ((result.rule.newNeural[i][itera].value == '->') and (result.rule.newNeural[i][itera + 1].type == 'ID')):
                    itera += 1
                    tempSTR = result.rule.newNeural[i][itera].value
                    itera += 1
                    if (tempSTR == 'lambda'):
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Recieve.a = tempSTR
                        result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Recieve.power = 0
                        if (not hasattr(result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E, 'a')):
                            result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.a = result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.a
                        if (len(result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power)==0):
                            result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power.append(result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.power)

                        break
                if ((result.rule.newNeural[i][itera].value == '^') and (result.rule.newNeural[i][itera + 1].type == 'NUMBER')):
                    itera += 1
                    temp = ''
                    while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                        temp += result.rule.newNeural[i][itera].value
                        itera += 1
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Recieve.a = tempSTR
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Recieve.power = int(temp)
                elif (result.rule.newNeural[i][itera].value == ':'):
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Recieve.a = tempSTR
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Recieve.power = 1

                if ((result.rule.newNeural[i][itera].value == ':') and (result.rule.newNeural[i][itera + 1].type == 'NUMBER')):
                    itera += 1
                    temp = ''
                    while (result.rule.newNeural[i][itera].type == 'NUMBER'):
                        temp += result.rule.newNeural[i][itera].value
                        itera += 1
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].delay = int(temp)
                if (not hasattr(result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E,'a')):
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.a = result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.a
                if (len(result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power)==0):
                    result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].E.power.append(result.Neural.__dict__['Neural_%d' % int(tempINDEX)].__dict__['Index_%d' % int(tempSUBindex)].Eject.power)
                itera += 1
# end in rule

    del result.initial.init
    del result.synapses.synap
    del result.rule

    return result

def readInputFile(filename):
    with open(filename) as file_in:
        lines = "".join(file_in.readlines());

    tokens = [token for token in tokenize(lines)];

    index, system = process_tokens(tokens, None, 0)
    system = resultTOsystem(system)

    return system

if __name__ == "__main__":
    filename = 'ex_1.txt'
    if os.path.exists('output/result_%s.txt'%filename):
        os.remove('output/result_%s.txt'%filename)
    system = readInputFile(filename)
    system.runSimulation(system, 5, filename)