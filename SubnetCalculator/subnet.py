import tkinter as tk
from tkinter import scrolledtext
#import ImageTk as img

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
tk_lbl_subnet_count = tk.Label(text="Subnet Divisions:")

#Entry's:
tk_ent_ip_block_A = tk.Entry(width=3)
tk_ent_ip_block_B = tk.Entry(width=3)
tk_ent_ip_block_C = tk.Entry(width=3)
tk_ent_ip_block_D = tk.Entry(width=3,font=("Arial",14,"bold"),fg="red")

#Spin:
tk_spin_subnet_count = tk.Spinbox(from_=1, to=6, increment=1, width=3, state="readonly", command=lambda:selected_spin)

#Buttons:
tk_btn_calculate = tk.Button(text="Calculate", font=("Arial",14,"bold"), command=lambda:result_print())
tk_btn_reset_form = tk.Button(text="Reset", font=("Arial",14,""), command=lambda:reset_form())
tk_btn_print = tk.Button(text="Print", font=("Arial",14,""), command=lambda:print_form())
#Scrolled Text:
tk_text_result = scrolledtext.ScrolledText(width=70,height=30, font=("Courier",14))

def reset_form():
    tk_ent_ip_block_A.delete(0,tk.END)
    tk_ent_ip_block_B.delete(0,tk.END)
    tk_ent_ip_block_C.delete(0,tk.END)
    tk_text_result.delete(1.0, tk.END)
    tk_spin_subnet_count.delete(0,"end")
    tk_ent_ip_block_A.focus()
   
def print_form():
    pass

def selected_spin():
    subnet_count = tk_spin_subnet_count.get()
    return subnet_count

def result_print():
    #FORM-VARIABLES:
    
    try:
        ip_A = int(tk_ent_ip_block_A.get())
        ip_B = int(tk_ent_ip_block_B.get())
        ip_C = int(tk_ent_ip_block_C.get())
        #ip_D = int(tk_ent_ip_block_D.get())

        i=1; a=1
        count = int(selected_spin())
        subnet = int(pow(2,count))
        increase = int(pow(2,(8-count)))
        subnet_mask = 256-increase

        result = ""
        tk_text_result.delete(1.0, tk.END)
        tk_text_result.config(font=("Arial",14,""),fg="black")

        firstIP = a
        lastIP = increase-2
        broadcastIP = lastIP + 1
        result+= f"{i}.Network({ip_A}.{ip_B}.{ip_C}.{firstIP-1}/255.255.255.{subnet_mask}):\n"
        result+= f"First IP: {ip_A}.{ip_B}.{ip_C}.{firstIP}\n"
        result+= f"Last IP: {ip_A}.{ip_B}.{ip_C}.{lastIP}\n"
        result+= f"Broadcast IP: {ip_A}.{ip_B}.{ip_C}.{broadcastIP}\n\n"


        while(True):
            firstIP = firstIP+increase
            lastIP = lastIP+increase
            broadcastIP = lastIP + 1
            result+= f"{i+1}.Network({ip_A}.{ip_B}.{ip_C}.{firstIP-1}/255.255.255.{subnet_mask}):\n"
            result+= f"First IP: {ip_A}.{ip_B}.{ip_C}.{firstIP}\n"
            result+= f"Last IP: {ip_A}.{ip_B}.{ip_C}.{lastIP}\n"
            result+= f"Broadcast IP: {ip_A}.{ip_B}.{ip_C}.{broadcastIP}\n\n"
            i+= 1

            if i == int(pow(2,count)):
                break

        result+=f"\n\nTotal Subnet Count: {subnet}"
        result+=f"\nTotal IP Count by Subnet: {increase-2}"       
        tk_text_result.insert(tk.INSERT, chars = result)
    except:
        tk_text_result.delete(1.0, tk.END)
        tk_text_result.config(font=("Arial",14,"bold"),fg="red")
        tk_text_result.insert(tk.INSERT, chars = "Please Enter Your IP Address Completely")

dx=0; dy=0
tk_lbl_ip.place(x=dx+10, y=dy+10)
tk_ent_ip_block_A.place(x=dx+85, y=dy+10); tk_ent_ip_block_A.focus()
tk_lbl_point_1.place(x=dx+120,y=dy+10)
tk_ent_ip_block_B.place(x=dx+125, y=dy+10)
tk_lbl_point_2.place(x=dx+160,y=dy+10)
tk_ent_ip_block_C.place(x=dx+165, y=dy+10)
tk_lbl_point_3.place(x=dx+200,y=dy+10)
tk_ent_ip_block_D.place(x=dx+205, y=dy+10)
tk_ent_ip_block_D.insert(0," X")
tk_ent_ip_block_D.config(state="readonly")

tk_lbl_subnet_count.place(x=dx+10,y=dy+50)
tk_spin_subnet_count.place(x=dx+123, y=dy+45)

tk_btn_calculate.place(x=dx+175,y=dy+45)
tk_btn_print.place(x=dx+270, y=dy+45)
tk_btn_reset_form.place(x=dx+330, y=dy+45)

tk_text_result.place(x=dx+10,y=dy+90)

window.mainloop()