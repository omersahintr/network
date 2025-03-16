import tkinter as tk
from tkinter import scrolledtext


ip_address=[0,0,0,0]
subnet_mask=0
subnet_count=0
result=""

window = tk.Tk()
window.title("Subnet Calculator")
window.minsize(width=600, height=600)

#label:
tk_lbl_ip = tk.Label(text="Ip Address:")
tk_lbl_point_1 = tk.Label(text=".")
tk_lbl_point_2 = tk.Label(text=".")
tk_lbl_point_3 = tk.Label(text=".")
tk_lbl_subnet_count = tk.Label(text="Subnet Count:")

#Entry's:
tk_ent_ip_block_A = tk.Entry(width=3)
tk_ent_ip_block_B = tk.Entry(width=3)
tk_ent_ip_block_C = tk.Entry(width=3)
tk_ent_ip_block_D = tk.Entry(width=3)

#Spin:
tk_spin_subnet_count = tk.Spinbox(from_=2, to=16, increment=2, width=3, command=lambda:selected_spin)

#Buttons:
tk_btn_calculate = tk.Button(text="Calculate", font=("Arial",14,"bold"), command=lambda:subnet_calculate())

#Scrolled Text:
tk_text_result = scrolledtext.ScrolledText(width=70,height=30, font=("Courier",14))

def selected_spin():
    subnet_count = tk_spin_subnet_count.get()
    return subnet_count

def result_print(param):
    #FORM-VARIABLES:
    ip_A = int(tk_ent_ip_block_A.get())
    ip_B = int(tk_ent_ip_block_B.get())
    ip_C = int(tk_ent_ip_block_C.get())
    ip_D = int(tk_ent_ip_block_D.get())

    i=1
    count = int(selected_spin())
    pows = int(pow(2,count)-2)
    increase = int(pows/count)
    result = ""

    while(True):
        firstIP = i
        lastIP = increase
        broadcastIP = lastIP + 1
        result+= f"{i}.Network:\n"
        result+= f"First IP: {ip_A}.{ip_B}.{ip_C}.{firstIP}\n"
        result+= f"Last IP: {ip_A}.{ip_B}.{ip_C}.{lastIP}\n"
        result+= f"Broadcast IP: {ip_A}.{ip_B}.{ip_C}.{broadcastIP}\n\n"
        
        if i == count:
            break
        else:
            i+= 1
    return result

def subnet_calculate(): 
    match int(selected_spin()):
        case 1:
            result = result_print(1)
        case 2:
            result = result_print(2)   
        case 4:
            result = result_print(4) 

    tk_text_result.insert(tk.INSERT, chars = result)

    

"""    tk_text_result.insert(tk.INSERT, chars=(f"{ip_A}\n"))
    tk_text_result.insert(tk.INSERT, chars=(f"{subnet}\n"))"""






dx=0; dy=0
tk_lbl_ip.place(x=dx+10, y=dy+10)
tk_ent_ip_block_A.place(x=dx+85, y=dy+10); tk_ent_ip_block_A.focus()
tk_lbl_point_1.place(x=dx+120,y=dy+10)
tk_ent_ip_block_B.place(x=dx+125, y=dy+10)
tk_lbl_point_2.place(x=dx+160,y=dy+10)
tk_ent_ip_block_C.place(x=dx+165, y=dy+10)
tk_lbl_point_3.place(x=dx+200,y=dy+10)
tk_ent_ip_block_D.place(x=dx+205, y=dy+10)

tk_lbl_subnet_count.place(x=dx+10,y=dy+50)
tk_spin_subnet_count.place(x=dx+103, y=dy+45)

tk_btn_calculate.place(x=dx+155,y=dx+45)

tk_text_result.place(x=dx+10,y=dx+90)

window.mainloop()