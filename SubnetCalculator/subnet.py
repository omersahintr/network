import tkinter as tk


ip_address=[0,0,0,0]
subnet_mask=0
subnet_count=0

window = tk.Tk()
window.title("Subnet Calculator")
window.minsize(width=600, height=600)

#label:
lbl_ip = tk.Label(text="Ip Address:")
lbl_point_1 = tk.Label(text=".")
lbl_point_2 = tk.Label(text=".")
lbl_point_3 = tk.Label(text=".")

#Entry's:
ent_ip_block_A = tk.Entry(width=3)
ent_ip_block_B = tk.Entry(width=3)
ent_ip_block_C = tk.Entry(width=3)
ent_ip_block_D = tk.Entry(width=3)

#Buttons:
btn_calculate = tk.Button(text="Calculate")




def subnet_calculate(num):
    pass



dx=0; dy=0
lbl_ip.place(x=dx+10, y=dy+10)
ent_ip_block_A.place(x=dx+85, y=dy+10); ent_ip_block_A.focus()
lbl_point_1.place(x=dx+120,y=dy+10)
ent_ip_block_B.place(x=dx+125, y=dy+10)
lbl_point_2.place(x=dx+160,y=dy+10)
ent_ip_block_C.place(x=dx+165, y=dy+10)
lbl_point_3.place(x=dx+160,y=dy+10)
ent_ip_block_D.place(x=dx+165, y=dy+10)
window.mainloop()