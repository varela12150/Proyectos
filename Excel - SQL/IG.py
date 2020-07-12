import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from io import open
from numpy import nan

ruta = "" # Almacenar la ruta del fichero
campos_break = "insert into admfca.cltb_account_comp_bal_breakup (ACCOUNT_NUMBER, BRANCH_CODE, COMPONENT, GL_CODE, GL_TYPE, BALANCE, LCY_BALANCE, CREATION_DATE, STATUS_CODE, SEVERITY_LEVEL, CONT_OFFSET_GL, BALANCE_FLAG, GAAP_INDICATOR)"
campos_shedules = "insert into admfca.cltb_account_schedules (ACCOUNT_NUMBER, BRANCH_CODE, COMPONENT_NAME, FORMULA_NAME, SCHEDULE_TYPE, SCHEDULE_ST_DATE, SCHEDULE_DUE_DATE, GRACE_DAYS, ORIG_AMOUNT_DUE, AMOUNT_DUE, ADJ_AMOUNT, AMOUNT_SETTLED, AMOUNT_OVERDUE, ACCRUED_AMOUNT, SETTLEMENT_CCY, LCY_EQUIVALENT, DLY_AVG_AMT, EMI_AMOUNT, SCHEDULE_FLAG, WAIVER_FLAG, EVENT_SEQ_NO, SCHEDULE_LINKAGE, CAPITALIZED, PROCESS_NO, AMOUNT_READJUSTED, ADJ_SETTLED, SCH_STATUS, ACCOUNT_GL, LAST_PMNT_VALUE_DATE, RETRY_START_DATE, MORA_INT, SCHEDULE_NO, WRITEOFF_AMT, READJ_SETTLED, LAST_READJ_XRATE, SUSP_AMT_DUE, SUSP_AMT_SETTLED, SUSP_AMT_LCY, SUSP_READ_AMT, SUSP_READ_SETTLED, LAST_SUSP_XRATE, AMOUNT_WAIVED, IRR_APPLICABLE, LIST_DAYS, LIST_AVG_AMT, PAY_BY_DATE)"
campos_comcal = "insert into admfca.cltb_account_comp_calc (BRANCH_CODE, ACCOUNT_NUMBER, COMPONENT_NAME, FORMULA_NAME, SCH_DUE_DATE, START_DATE, END_DATE, NO_OF_DAYS, PRODUCT, CURRENCY, EXPR_LINE, ACCR_TILL_DATE, DLY_AVG_AMT, IS_DUE_TO_SUB_COMP, SCH_START_DATE, FORMULA_GROUP)"
campos_sch = "insert into admfca.cltb_account_comp_sch (ACCOUNT_NUMBER, BRANCH_CODE, COMPONENT_NAME, SCHEDULE_TYPE, SCHEDULE_FLAG, FORMULA_NAME, SCH_START_DATE, NO_OF_SCHEDULES, FREQUENCY, UNIT, SCH_END_DATE, AMOUNT, PAYMENT_MODE, PMNT_PROD_AC, PAYMENT_DETAILS, BEN_ACCOUNT, BEN_BANK, BEN_NAME, CAPITALIZED, FIRST_DUE_DATE, WAIVER_FLAG, COMPOUND_DAYS, COMPOUND_MONTHS, COMPOUND_YEARS, EMI_AMOUNT, DUE_DATES_ON, DAYS_MTH, DAYS_YEAR, DP_AMOUNT, PAY_MODE, PAYABLE_ACC, EXCH_RATE, PAYABLE_ACC_CCY, EMI_AS_PERCENTAGE_SALARY)"
campos_daily = "insert into admfca.CLTB_ACCNT_DAILY_COMPOUND (ACCOUNT_NUMBER, BRANCH_CODE, COMPONENT_NAME, COMPOUNDING_DATE, SCHEDULE_ST_DATE, AMOUNT)"
campos_balance = "insert into admfca.cltb_account_comp_balances (BRANCH_CODE, ACCOUNT_NUMBER, COMPONENT_NAME, VAL_DATE, BALANCE)"
    

def seleccionar():
        global ruta
        ruta = filedialog.askopenfilename(
        initialdir = '.',
        filetypes=(("Fichero general","*.*"),("Fichero de Excel","*.xlsx"),("Fichero sql","*.txt"),),
        title="Abrri un fichero")

def generar():
    global ruta

    if (CLTB_ACCOUNT_SCHEDULES.get()):
        path_file = ruta
        hoja_1 = "CLTB_ACCOUNT_SCHEDULES"
        df1 = pd.read_excel(path_file,sheet_name=hoja_1)
        with open("prueba_1.txt","w") as file:
            delete = "delete from admfca.cltb_account_schedules where account_number = "+'\''+str(df1.ACCOUNT_NUMBER[0])+'\''+";)"
            file.write(delete+"\n")
            for a,b in enumerate(df1.iterrows()):
                contenido = campos_shedules +"\n"+'values (\''+str(df1.ACCOUNT_NUMBER[a])+'\''+', \''+str(df1.BRANCH_CODE[a])+'\''+', \''+str(df1.COMPONENT_NAME[a])+'\''+', '+("null" if str(df1.FORMULA_NAME[a]) == str(nan) else '\''+str(df1.FORMULA_NAME[a])+'\'')+', '+("null" if str(df1.SCHEDULE_TYPE[a]) == str(nan) else '\''+str(df1.SCHEDULE_TYPE[a])+'\'')+ ', '+'to_date(\''+str("{:02d}".format(int(df1.SCHEDULE_ST_DATE[a].day)))+'-'+str("{:02d}".format(int(df1.SCHEDULE_ST_DATE[a].month)))+'-'+str("{:04d}".format(int(df1.SCHEDULE_ST_DATE[a].year)))+'\', \'dd-mm-yyyy\')'+', '+'to_date(\''+str("{:02d}".format(int(df1.SCHEDULE_DUE_DATE[a].day)))+'-'+str("{:02d}".format(int(df1.SCHEDULE_DUE_DATE[a].month)))+'-'+str("{:04d}".format(int(df1.SCHEDULE_DUE_DATE[a].year)))+'\', \'dd-mm-yyyy\')'+', '+("null" if str(df1.GRACE_DAYS[a]) == str(nan) else str(df1.GRACE_DAYS[a]))+', '+("null" if str(df1.ORIG_AMOUNT_DUE[a]) == str(nan) else str(df1.ORIG_AMOUNT_DUE[a]))+', '+("null" if str(df1.AMOUNT_DUE[a]) == str(nan) else str(df1.AMOUNT_DUE[a]))+', '+("null" if str(df1.ADJ_AMOUNT[a]) == str(nan) else str(df1.ADJ_AMOUNT[a]))+', '+("null" if str(df1.AMOUNT_SETTLED[a]) == str(nan) else str(df1.AMOUNT_SETTLED[a]))+', '+("null" if str(df1.AMOUNT_OVERDUE[a]) == str(nan) else str(df1.AMOUNT_OVERDUE[a]))+', '+("null" if str(df1.ACCRUED_AMOUNT[a]) == str(nan) else str(df1.ACCRUED_AMOUNT[a]))+', '+'\''+str(df1.SETTLEMENT_CCY[a])+'\''+', '+("null" if str(df1.LCY_EQUIVALENT[a]) == str(nan) else str(df1.LCY_EQUIVALENT[a]))+', '+("null" if str(df1.DLY_AVG_AMT[a]) == str(nan) else str(df1.DLY_AVG_AMT[a]))+', '+("null" if str(df1.EMI_AMOUNT[a]) == str(nan) else str(df1.EMI_AMOUNT[a]))+', '+("null" if str(df1.SCHEDULE_FLAG[a]) == str(nan) else '\''+str(df1.SCHEDULE_FLAG[a])+'\'')+', '+("null" if str(df1.WAIVER_FLAG[a]) == str(nan) else '\''+str(df1.WAIVER_FLAG[a])+'\'')+', '+("null" if str(df1.EVENT_SEQ_NO[a]) == str(nan) else str(df1.EVENT_SEQ_NO[a]))+', '+("null" if str(df1.SCHEDULE_LINKAGE[a]) == 'NaT' else 'to_date(\''+str("{:02d}".format(int(df1.SCHEDULE_LINKAGE[a].day)))+'-'+str("{:02d}".format(int(df1.SCHEDULE_LINKAGE[a].month)))+'-'+str("{:04d}".format(int(df1.SCHEDULE_LINKAGE[a].year)))+'\', \'dd-mm-yyyy\')')+', '+("null" if str(df1.CAPITALIZED[a]) == str(nan) else '\''+str(df1.CAPITALIZED[a])+'\'')+', '+("null" if str(df1.PROCESS_NO[a]) == str(nan) else str(df1.PROCESS_NO[a]))+', '+("null" if str(df1.AMOUNT_READJUSTED[a]) == str(nan) else str(df1.AMOUNT_READJUSTED[a]))+', '+("null" if str(df1.ADJ_SETTLED[a]) == str(nan) else '\''+str(df1.ADJ_SETTLED[a])+'\'')+', '+("null" if str(df1.SCH_STATUS[a]) == str(nan) else str(df1.SCH_STATUS[a]))+', '+("null" if str(df1.ACCOUNT_GL[a]) == str(nan) else '\''+str(df1.ACCOUNT_GL[a])+'\'')+', '+("null" if str(df1.LAST_PMNT_VALUE_DATE[a]) == 'NaT' else 'to_date(\''+str("{:02d}".format(int(df1.LAST_PMNT_VALUE_DATE[a].day)))+'-'+str("{:02d}".format(int(df1.LAST_PMNT_VALUE_DATE[a].month)))+'-'+str("{:04d}".format(int(df1.LAST_PMNT_VALUE_DATE[a].year)))+'\', \'dd-mm-yyyy\')')+', '+("null" if str(df1.RETRY_START_DATE[a]) == 'NaT' else 'to_date(\''+str("{:02d}".format(int(df1.RETRY_START_DATE[a].day)))+'-'+str("{:02d}".format(int(df1.RETRY_START_DATE[a].month)))+'-'+str("{:04d}".format(int(df1.RETRY_START_DATE[a].year)))+'\', \'dd-mm-yyyy\')')+', '+("null" if str(df1.MORA_INT[a]) == str(nan) else str(df1.MORA_INT[a]))+', '+("null" if str(df1.SCHEDULE_NO[a]) == str(nan) else str(df1.SCHEDULE_NO[a]))+', '+("null" if str(df1.WRITEOFF_AMT[a]) == str(nan) else str(df1.WRITEOFF_AMT[a]))+', '+("null" if str(df1.READJ_SETTLED[a]) == str(nan) else str(df1.READJ_SETTLED[a]))+', '+("null" if str(df1.LAST_READJ_XRATE[a]) == str(nan) else str(df1.LAST_READJ_XRATE[a]))+', '+("null" if str(df1.SUSP_AMT_DUE[a]) == str(nan) else str(df1.SUSP_AMT_DUE[a]))+', '+("null" if str(df1.SUSP_AMT_SETTLED[a]) == str(nan) else str(df1.SUSP_AMT_SETTLED[a]))+', '+("null" if str(df1.SUSP_AMT_LCY[a]) == str(nan) else str(df1.SUSP_AMT_LCY[a]))+', '+("null" if str(df1.SUSP_READ_AMT[a]) == str(nan) else str(df1.SUSP_READ_AMT[a]))+', '+("null" if str(df1.SUSP_READ_SETTLED[a]) == str(nan) else str(df1.SUSP_READ_SETTLED[a]))+', '+("null" if str(df1.LAST_SUSP_XRATE[a]) == str(nan) else str(df1.LAST_SUSP_XRATE[a]))+', '+("null" if str(df1.AMOUNT_WAIVED[a]) == str(nan) else str(df1.AMOUNT_WAIVED[a]))+', '+("null" if str(df1.IRR_APPLICABLE[a]) == str(nan) else '\''+str(df1.IRR_APPLICABLE[a])+'\'')+', '+("null" if str(df1.LIST_DAYS[a]) == str(nan) else str(df1.LIST_DAYS[a]))+', '+("null" if str(df1.LIST_AVG_AMT[a]) == str(nan) else str(df1.LIST_AVG_AMT[a]))+', '+("null" if str(df1.PAY_BY_DATE[a]) == str(nan) else str(df1.PAY_BY_DATE[a]))+');'
                file.write (contenido + "\n")

    if (CLTB_ACCOUNT_COMP_BAL_BREAKUP.get()):
        path_file = ruta
        hoja_2 = "CLTB_ACCOUNT_COMP_BAL_BREAKUP"
        df2 = pd.read_excel(path_file,sheet_name=hoja_2)
        with open("prueba_2.txt","w") as file:
            delete = "delete from admfca.cltb_account_comp_bal_breakup where account_number = "+'\''+str(df2.ACCOUNT_NUMBER[0])+'\''+";)"
            file.write(delete+"\n")
            for c,d in enumerate(df2.iterrows()):
                contenido = campos_break +"\n"+'values (\''+str(df2.ACCOUNT_NUMBER[c])+'\''+', '+'\''+str(df2.BRANCH_CODE[c])+'\''+', '+'\''+str(df2.COMPONENT[c])+'\''+', '+'\''+str(df2.GL_CODE[c])+'\''+', '+'\''+str(df2.GL_TYPE[c])+'\''+', '+("null" if str(df2.BALANCE[c]) == str(nan) else str(df2.BALANCE[c]))+', '+("null" if str(df2.LCY_BALANCE[c]) == str(nan) else str(df2.LCY_BALANCE[c]))+', '+'to_date(\''+str("{:02d}".format(int(df2.CREATION_DATE[c].day)))+'-'+str("{:02d}".format(int(df2.CREATION_DATE[c].month)))+'-'+str("{:04d}".format(int(df2.CREATION_DATE[c].year)))+'\', \'dd-mm-yyyy\')'+ ', '+'\''+str(df2.STATUS_CODE[c])+'\''+', '+("null" if str(df2.SEVERITY_LEVEL[c]) == str(nan) else str(df2.SEVERITY_LEVEL[c]))+', '+("null" if str(df2.CONT_OFFSET_GL[c]) == str(nan) else str(df2.CONT_OFFSET_GL[c]))+', '+'\''+str(df2.BALANCE_FLAG[c])+'\''+', '+'\''+str(df2.GAAP_INDICATOR[c])+'\''+');'
                file.write (contenido + "\n")
                
    if (CLTB_ACCOUNT_COMP_CALC.get()):
        path_file = ruta
        hoja_3 = "CLTB_ACCOUNT_COMP_CALC"
        df3 = pd.read_excel(path_file,sheet_name=hoja_3)
        with open("prueba_3.txt","w") as file:
            delete = "delete from admfca.cltb_account_comp_calc where account_number = "+'\''+str(df3.ACCOUNT_NUMBER[0])+'\''+";)"
            file.write(delete+"\n")
            for e,f in enumerate(df3.iterrows()):
                contenido = campos_comcal +"\n"+'values (\''+str(df3.BRANCH_CODE[e])+'\''+', '+'\''+str(df3.ACCOUNT_NUMBER[e])+'\''+', '+'\''+str(df3.COMPONENT_NAME[e])+'\''+', '+'\''+str(df3.FORMULA_NAME[e])+'\''+', '+'to_date(\''+str("{:02d}".format(int(df3.SCH_DUE_DATE[e].day)))+'-'+str("{:02d}".format(int(df3.SCH_DUE_DATE[e].month)))+'-'+str("{:04d}".format(int(df3.SCH_DUE_DATE[e].year)))+'\', \'dd-mm-yyyy\')'+', '+'to_date(\''+str("{:02d}".format(int(df3.START_DATE[e].day)))+'-'+str("{:02d}".format(int(df3.START_DATE[e].month)))+'-'+str("{:04d}".format(int(df3.START_DATE[e].year)))+'\', \'dd-mm-yyyy\')'+', '+'to_date(\''+str("{:02d}".format(int(df3.END_DATE[e].day)))+'-'+str("{:02d}".format(int(df3.END_DATE[e].month)))+'-'+str("{:04d}".format(int(df3.END_DATE[e].year)))+'\', \'dd-mm-yyyy\')'+', '+("null" if str(df3.NO_OF_DAYS[e]) == str(nan) else str(df3.NO_OF_DAYS[e]))+', '+'\''+str(df3.PRODUCT[e])+'\''+', '+'\''+str(df3.CURRENCY[e])+'\''+', '+'\''+str(df3.EXPR_LINE[e])+'\''+', '+("null" if str(df3.ACCR_TILL_DATE[e]) == str(nan) else str(df3.ACCR_TILL_DATE[e]))+', '+("null" if str(df3.DLY_AVG_AMT[e]) == str(nan) else str(df3.DLY_AVG_AMT[e]))+', '+'\''+str(df3.IS_DUE_TO_SUB_COMP[e])+'\''+', '+'to_date(\''+str("{:02d}".format(int(df3.SCH_START_DATE[e].day)))+'-'+str("{:02d}".format(int(df3.SCH_START_DATE[e].month)))+'-'+str("{:04d}".format(int(df3.SCH_START_DATE[e].year)))+'\', \'dd-mm-yyyy\')'+', '+'\''+str(df3.FORMULA_GROUP[e])+'\''+');'
                file.write (contenido + "\n")

    if (CLTB_ACCOUNT_COMP_SCH.get()):
        path_file = ruta
        hoja_4 = "CLTB_ACCOUNT_COMP_SCH"
        df4 = pd.read_excel(path_file,sheet_name=hoja_4)
        with open("prueba_4.txt","w") as file:
            delete = "delete from admfca.cltb_account_comp_sch where account_number = "+'\''+str(df4.ACCOUNT_NUMBER[0])+'\''+";)"
            file.write(delete+"\n")
            for g,h in enumerate(df4.iterrows()):
                contenido = campos_sch +"\n"+'values (\''+str(df4.ACCOUNT_NUMBER[g])+'\''+', '+'\''+str(df4.BRANCH_CODE[g])+'\''+', '+'\''+str(df4.COMPONENT_NAME[g])+'\''+', '+'\''+str(df4.SCHEDULE_TYPE[g])+'\''+', '+'\''+str(df4.SCHEDULE_FLAG[g])+'\''+', '+("null" if str(df4.FORMULA_NAME[g]) == str(nan) else '\''+str(df4.FORMULA_NAME[g])+'\'')+', '+'to_date(\''+str("{:02d}".format(int(df4.SCH_START_DATE[g].day)))+'-'+str("{:02d}".format(int(df4.SCH_START_DATE[g].month)))+'-'+str("{:04d}".format(int(df4.SCH_START_DATE[g].year)))+'\', \'dd-mm-yyyy\')'+', '+("null" if str(df4.NO_OF_SCHEDULES[g]) == str(nan) else str(df4.NO_OF_SCHEDULES[g]))+', '+("null" if str(df4.FREQUENCY[g]) == str(nan) else str(df4.FREQUENCY[g]))+', '+("null" if str(df4.UNIT[g]) == str(nan) else '\''+str(df4.UNIT[g])+'\'')+', '+'to_date(\''+str("{:02d}".format(int(df4.SCH_START_DATE[g].day)))+'-'+str("{:02d}".format(int(df4.SCH_END_DATE[g].month)))+'-'+str("{:04d}".format(int(df4.SCH_END_DATE[g].year)))+'\', \'dd-mm-yyyy\')'+', '+("null" if str(df4.AMOUNT[g]) == str(nan) else str(df4.AMOUNT[g]))+', '+("null" if str(df4.PAYMENT_MODE[g]) == str(nan) else str(df4.PAYMENT_MODE[g]))+', '+("null" if str(df4.PMNT_PROD_AC[g]) == str(nan) else str(df4.PMNT_PROD_AC[g]))+', '+("null" if str(df4.PAYMENT_DETAILS[g]) == str(nan) else str(df4.PAYMENT_DETAILS[g]))+', '+("null" if str(df4.BEN_ACCOUNT[g]) == str(nan) else str(df4.BEN_ACCOUNT[g]))+', '+("null" if str(df4.BEN_BANK[g]) == str(nan) else str(df4.BEN_BANK[g]))+', '+("null" if str(df4.BEN_NAME[g]) == str(nan) else str(df4.BEN_NAME[g]))+', '+("null" if str(df4.CAPITALIZED[g]) == str(nan) else '\''+str(df4.CAPITALIZED[g])+'\'')+', '+'to_date(\''+str("{:02d}".format(int(df4.FIRST_DUE_DATE[g].day)))+'-'+str("{:02d}".format(int(df4.FIRST_DUE_DATE[g].month)))+'-'+str("{:04d}".format(int(df4.FIRST_DUE_DATE[g].year)))+'\', \'dd-mm-yyyy\')'+', '+("null" if str(df4.WAIVER_FLAG[g]) == str(nan) else '\''+str(df4.WAIVER_FLAG[g])+'\'')+', '+("null" if str(df4.COMPOUND_DAYS[g]) == str(nan) else str(df4.COMPOUND_DAYS[g]))+', '+("null" if str(df4.COMPOUND_MONTHS[g]) == str(nan) else str(df4.COMPOUND_MONTHS[g]))+', '+("null" if str(df4.COMPOUND_YEARS[g]) == str(nan) else str(df4.COMPOUND_YEARS[g]))+', '+("null" if str(df4.EMI_AMOUNT[g]) == str(nan) else str(df4.EMI_AMOUNT[g]))+', '+("null" if str(df4.DUE_DATES_ON[g]) == str(nan) else str(df4.DUE_DATES_ON[g]))+', '+("null" if str(df4.DAYS_MTH[g]) == str(nan) else str(df4.DAYS_MTH[g]))+', '+("null" if str(df4.DAYS_YEAR[g]) == str(nan) else str(df4.DAYS_YEAR[g]))+', '+("null" if str(df4.DP_AMOUNT[g]) == str(nan) else str(df4.DP_AMOUNT[g]))+', '+("null" if str(df4.PAY_MODE[g]) == str(nan) else str(df4.PAY_MODE[g]))+', '+("null" if str(df4.PAYABLE_ACC[g]) == str(nan) else str(df4.PAYABLE_ACC[g]))+', '+("null" if str(df4.EXCH_RATE[g]) == str(nan) else str(df4.EXCH_RATE[g]))+', '+("null" if str(df4.PAYABLE_ACC_CCY[g]) == str(nan) else str(df4.PAYABLE_ACC_CCY[g]))+', '+("null" if str(df4.EMI_AS_PERCENTAGE_SALARY[g]) == str(nan) else str(df4.EMI_AS_PERCENTAGE_SALARY[g]))+');'
                file.write (contenido + "\n")

    if (CLTB_ACCOUNT_COMP_BALANCES.get()):
        path_file = ruta
        hoja_5 = "CLTB_ACCOUNT_COMP_BALANCES"
        df5 = pd.read_excel(path_file,sheet_name=hoja_5)
        with open("prueba_5.txt","w") as file:
            delete = "delete from admfca.cltb_account_comp_balances where account_number = "+'\''+str(df5.ACCOUNT_NUMBER[0])+'\''+";)"
            file.write(delete+"\n")
            for i,j in enumerate(df5.iterrows()):
                contenido = campos_balance +"\n"+'values (\''+str(df5.BRANCH_CODE[i])+'\''+', '+'\''+str(df5.ACCOUNT_NUMBER[i])+'\''+', '+'\''+str(df5.COMPONENT_NAME[i])+'\''+', '+'to_date(\''+str("{:02d}".format(int(df5.VAL_DATE[i].day)))+'-'+str("{:02d}".format(int(df5.VAL_DATE[i].month)))+'-'+str("{:04d}".format(int(df5.VAL_DATE[i].year)))+'\', \'dd-mm-yyyy\')'+', '+("null" if str(df5.BALANCE[i]) == str(nan) else str(df5.BALANCE[i]))+');'
                file.write (contenido + "\n")

    if (CLTB_ACCNT_DAILY_COMPOUND.get()):
        path_file = ruta
        hoja_6 = "CLTB_ACCNT_DAILY_COMPOUND"
        df6 = pd.read_excel(path_file,sheet_name=hoja_6)
        with open("prueba_6.txt","w") as file:
            delete = "delete from admfca.cltb_accnt_daily_compound where account_number = "+'\''+str(df6.ACCOUNT_NUMBER[0])+'\''+";)"
            file.write(delete+"\n")
            for k,l in enumerate(df6.iterrows()):
                contenido = campos_daily +"\n"+'values (\''+str(df6.ACCOUNT_NUMBER[k])+'\''+', '+'\''+str(df6.BRANCH_CODE[k])+'\''+', '+'\''+str(df6.COMPONENT_NAME[k])+'\''+', '+'to_date(\''+str("{:02d}".format(int(df6.COMPOUNDING_DATE[k].day)))+'-'+str("{:02d}".format(int(df6.COMPOUNDING_DATE[k].month)))+'-'+str("{:04d}".format(int(df6.COMPOUNDING_DATE[k].year)))+'\', \'dd-mm-yyyy\')'+', '+'to_date(\''+str("{:02d}".format(int(df6.SCHEDULE_ST_DATE[k].day)))+'-'+str("{:02d}".format(int(df6.SCHEDULE_ST_DATE[k].month)))+'-'+str("{:04d}".format(int(df6.SCHEDULE_ST_DATE[k].year)))+'\', \'dd-mm-yyyy\')'+', '+("null" if str(df6.AMOUNT[k]) == str(nan) else str(df6.AMOUNT[k]))+');'
                file.write (contenido + "\n")
                
    else:
        pass

# Configuración de la raíz
root = Tk()
root.title("generador sql")
root.config(bd=15)
root.resizable(0,0)


CLTB_ACCOUNT_SCHEDULES = IntVar()    # 1 si, 0 no
CLTB_ACCOUNT_COMP_BAL_BREAKUP = IntVar() 
CLTB_ACCOUNT_COMP_CALC = IntVar() # 1 si, 0 
CLTB_ACCOUNT_COMP_SCH = IntVar() # 1 si, 0 
CLTB_ACCOUNT_COMP_BALANCES = IntVar() # 1 si, 0 
CLTB_ACCNT_DAILY_COMPOUND = IntVar() # 1 si, 0 


frame = Frame(root)
frame.grid()

Label(frame, text="Que tablas necesitas modificar ?").grid(row = 0, column = 0, sticky = "w")
Checkbutton(frame, text="CLTB_ACCOUNT_SCHEDULES", variable=CLTB_ACCOUNT_SCHEDULES, onvalue=1, 
            offvalue=0).grid(row = 1, column = 0, sticky = "w")
Checkbutton(frame, text="CLTB_ACCOUNT_COMP_BAL_BREAKUP", variable=CLTB_ACCOUNT_COMP_BAL_BREAKUP, onvalue=1, 
            offvalue=0).grid(row = 2, column = 0, sticky = "w")
Checkbutton(frame, text="CLTB_ACCOUNT_COMP_CALC", variable=CLTB_ACCOUNT_COMP_CALC, onvalue=1, 
            offvalue=0).grid(row = 3, column = 0, sticky = "w")
Checkbutton(frame, text="CLTB_ACCOUNT_COMP_SCH", variable=CLTB_ACCOUNT_COMP_SCH, onvalue=1, 
            offvalue=0).grid(row = 4, column = 0, sticky = "w")
Checkbutton(frame, text="CLTB_ACCOUNT_COMP_BALANCES", variable=CLTB_ACCOUNT_COMP_BALANCES, onvalue=1, 
            offvalue=0).grid(row = 5, column = 0, sticky = "w")
Checkbutton(frame, text="CLTB_ACCNT_DAILY_COMPOUND", variable=CLTB_ACCNT_DAILY_COMPOUND, onvalue=1, 
            offvalue=0).grid(row = 6, column = 0, sticky = "w")

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen).grid(row = 0, column = 1)


Button(root, text="generar", command=generar).grid(sticky = "s")
Button(root, text="Seleccionar Excel", command=seleccionar).grid(sticky = "s")
            

# Finalmente bucle de la aplicación
root.mainloop()