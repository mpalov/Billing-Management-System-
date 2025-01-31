from tkinter import *
import random
from tkinter import messagebox


class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing Software")
        title = Label(self.root, text="Billing System", bd=12, relief=RIDGE, font=("Arial Black", 20), bg="#A569BD",
                      fg="white").pack(fill=X)

        # ===================================Variables===================================================================

        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.coca_cola = IntVar()

        self.eggs = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.flour = IntVar()
        self.beef = IntVar()

        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()

        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()

        # ==========================================Customer Details Label Frame========================================

        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#A569BD", fg="white",
                             relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Customer Name", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=15)

        cust_entry = Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="Contact No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(
            row=0, column=2, padx=10)

        contact_entry = Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="Bill No.", font=("Arial Black", 14), bg="#A569BD", fg="white").grid(row=0,
                                                                                                             column=4,
                                                                                                             padx=10)

        bill_entry = Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        # =======================================Snacks Label Frame=====================================================

        snacks = LabelFrame(self.root, text="Snacks", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483",
                            relief=GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)

        item1 = Label(snacks, text="Nutella Choco Spread", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=0, column=0, pady=11)
        item1_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.nutella).grid(row=0, column=1, padx=10)

        item2 = Label(snacks, text="Noodles(1 Pack)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item2_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.noodles).grid(row=1, column=1, padx=10)

        item3 = Label(snacks, text="Lays", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2,
                                                                                                      column=0,
                                                                                                      pady=11)
        item3_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.lays).grid(row=2, column=1, padx=10)

        item4 = Label(snacks, text="Oreo", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3,
                                                                                                      column=0,
                                                                                                      pady=11)
        item4_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.oreo).grid(row=3, column=1, padx=10)

        item5 = Label(snacks, text="Chocolate Muffin", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  pady=11)
        item5_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.muffin).grid(row=4, column=1, padx=10)

        item6 = Label(snacks, text="Dairy Milk Silk", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=5, column=0, pady=11)
        item6_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.silk).grid(row=5, column=1, padx=10)

        item7 = Label(snacks, text="Coca-Cola", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=6,
                                                                                                           column=0,
                                                                                                           pady=11)

        item7_entry = Entry(snacks, borderwidth=2, width=15, textvariable=self.coca_cola).grid(row=6, column=1, padx=10)

        # ===================================Grocery====================================================================

        grocery = LabelFrame(self.root, text="Grocery", font=("Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3",
                             fg="#6C3483")
        grocery.place(x=340, y=180, height=380, width=325)

        item8 = Label(grocery, text="Eggs(10 Count)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=0, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.eggs).grid(row=0, column=1, padx=10)

        item9 = Label(grocery, text="Pasta(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1,
                                                                                                             column=0,
                                                                                                             pady=11)
        item9_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.pasta).grid(row=1, column=1, padx=10)

        item10 = Label(grocery, text="Rice(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=2, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.rice).grid(row=2, column=1, padx=10)

        item11 = Label(grocery, text="Sunflower Oil(1ltr)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=3, column=0, pady=11)
        item11_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.oil).grid(row=3, column=1, padx=10)

        item12 = Label(grocery, text="Refined Sugar(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=4, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.sugar).grid(row=4, column=1, padx=10)

        item13 = Label(grocery, text="Flour(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=5,
                                                                                                             column=0,
                                                                                                             pady=11)
        item13_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.flour).grid(row=5, column=1, padx=10)

        item14 = Label(grocery, text="Ground Beef(1kg)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=6, column=0, pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15, textvariable=self.beef).grid(row=6, column=1, padx=10)

        # ========================================Beauty and Hygiene=====================================================

        hygiene = LabelFrame(self.root, text="Beauty & Hygiene", font=("Arial Black", 12), relief=GROOVE, bd=10,
                             bg="#E5B4F3", fg="#6C3483")
        hygiene.place(x=677, y=180, height=380, width=325)

        item15 = Label(hygiene, text="Bathing Soap", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0,
                                                                                                                column=0,
                                                                                                                pady=11)
        item15_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.soap).grid(row=0, column=1, padx=10)

        item16 = Label(hygiene, text="Shampoo(1ltr)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 pady=11)
        item16_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.shampoo).grid(row=1, column=1, padx=10)

        item17 = Label(hygiene, text="Body Lotion(1ltr)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=2, column=0, pady=11)
        item17_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.lotion).grid(row=2, column=1, padx=10)

        item18 = Label(hygiene, text="Face Cream", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3,
                                                                                                              column=0,
                                                                                                              pady=11)
        item18_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.cream).grid(row=3, column=1, padx=10)

        item19 = Label(hygiene, text="Shaving Foam", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4,
                                                                                                                column=0,
                                                                                                                pady=11)
        item19_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.foam).grid(row=4, column=1, padx=10)

        item20 = Label(hygiene, text="Face Mask(1 piece)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=5, column=0, pady=11)
        item20_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.mask).grid(row=5, column=1, padx=10)

        item21 = Label(hygiene, text="Hand Sanitizer(50ml)", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(
            row=6, column=0, pady=11)
        item21_entry = Entry(hygiene, borderwidth=2, width=15, textvariable=self.sanitizer).grid(row=6, column=1,
                                                                                                 padx=10)

        # =====================================================Bill Area================================================

        bill_area = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        bill_area.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(bill_area, text="Bill Area", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3",
                           fg="#6C3483").pack(fill=X)

        scroll_y = Scrollbar(bill_area, orient=VERTICAL)
        self.txt_area = Text(bill_area, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt_area.yview)
        self.txt_area.pack(fill=BOTH, expand=1)

        # =================================================Billing Menu=================================================

        billing_menu = LabelFrame(self.root, text="Billing Summery", font=("Arial Black", 12), relief=GROOVE, bd=10,
                                  bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_snacks = Label(billing_menu, text="Total Snacks Price", font=("Arial Black", 11), bg="#A569BD",
                             fg="white").grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_sna).grid(row=0,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=7)

        total_grocery = Label(billing_menu, text="Total Grocery Price", font=("Arial Black", 11), bg="#A569BD",
                              fg="white").grid(row=1, column=0)
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_gro).grid(row=1,
                                                                                                             column=1,
                                                                                                             padx=10,
                                                                                                             pady=7)

        total_hygiene = Label(billing_menu, text="Total Beauty & Hygiene Price", font=("Arial Black", 11), bg="#A569BD",
                             fg="white").grid(row=2, column=0)
        total_hygiene_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_hyg).grid(row=2,
                                                                                                            column=1,
                                                                                                            padx=10,
                                                                                                            pady=7)

        tax_snacks = Label(billing_menu, text="Snacks Tax", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(
            row=0, column=2)
        tax_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a).grid(row=0, column=3,
                                                                                                  padx=10, pady=7)

        tax_grocery = Label(billing_menu, text="Grocery Tax", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(
            row=1, column=2)
        tax_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b).grid(row=1, column=3,
                                                                                                   padx=10, pady=7)

        tax_hygiene = Label(billing_menu, text="Beauty & Hygiene Tax", font=("Arial Black", 11), bg="#A569BD",
                           fg="white").grid(row=2, column=2)
        tax_hygiene_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c).grid(row=2, column=3,
                                                                                                  padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Total Bill", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                              fg="#6C3483", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="Clear Field", font=("Arial Black", 15), pady=10, bg="#E5B4F3",
                              fg="#6C3483", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(button_frame, text="Exit", font=("Arial Black", 15), pady=10, bg="#E5B4F3", fg="#6C3483",
                             width=8, command=lambda: exit1(self)).grid(row=0, column=2, padx=10, pady=6)
        intro(self)


def total(self):
    if self.c_name.get == "" or self.phone.get() == "":
        messagebox.showerror("Error", "Fill the complete customer details!!")
    self.nu = self.nutella.get() * 15
    self.no = self.noodles.get() * 2
    self.la = self.lays.get() * 3
    self.ore = self.oreo.get() * 4.50
    self.mu = self.muffin.get() * 1.50
    self.si = self.silk.get() * 5
    self.co = self.coca_cola.get() * 1
    total_snacks_price = (
            self.nu +
            self.no +
            self.la +
            self.ore +
            self.mu +
            self.si +
            self.co)
    self.total_sna.set(str(total_snacks_price) + " €")
    self.a.set(str(round(total_snacks_price * 0.05, 3)) + " €")

    self.at = self.eggs.get() * 3.50
    self.pa = self.pasta.get() * 2.50
    self.oi = self.oil.get() * 4
    self.ri = self.rice.get() * 2.50
    self.su = self.sugar.get() * 2
    self.te = self.beef.get() * 14
    self.da = self.flour.get() * 3.50
    total_grocery_price = (
            self.at +
            self.pa +
            self.oi +
            self.ri +
            self.su +
            self.te +
            self.da)

    self.total_gro.set(str(total_grocery_price) + " €")
    self.b.set(str(round(total_grocery_price * 0.01, 3)) + " €")

    self.so = self.soap.get() * 1.50
    self.sh = self.shampoo.get() * 5
    self.cr = self.cream.get() * 7
    self.lo = self.lotion.get() * 10
    self.fo = self.foam.get() * 3.50
    self.ma = self.mask.get() * 10
    self.sa = self.sanitizer.get() * 2.50

    total_hygiene_price = (
            self.so +
            self.sh +
            self.cr +
            self.lo +
            self.fo +
            self.ma +
            self.sa)

    self.total_hyg.set(str(total_hygiene_price) + " €")
    self.c.set(str(round(total_hygiene_price * 0.10, 3)) + " €")
    self.total_all_bill = (total_snacks_price +
                           total_grocery_price +
                           total_hygiene_price +
                           (round(total_grocery_price * 0.01, 3)) +
                           (round(total_hygiene_price * 0.10, 3)) +
                           (round(total_snacks_price * 0.05, 3)))
    self.total_all_bil = str(self.total_all_bill) + " €"
    billarea(self)


def intro(self):
    self.txt_area.delete(1.0, END)
    self.txt_area.insert(END, "\tWELCOME TO SUPER MARKET\n\tPhone-No.739275410")
    self.txt_area.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
    self.txt_area.insert(END, f"\nCustomer Name : {self.c_name.get()}")
    self.txt_area.insert(END, f"\nPhone No. : {self.phone.get()}")
    self.txt_area.insert(END, "\n====================================\n")
    self.txt_area.insert(END, "\nProduct\tQuantity\tPrice\n")
    self.txt_area.insert(END, "\n====================================\n")


def billarea(self):
    intro(self)
    if self.nutella.get() != 0:
        self.txt_area.insert(END, f"Nutella\t\t {self.nutella.get()}\t{self.nu}\n")
    if self.noodles.get() != 0:
        self.txt_area.insert(END, f"Noodles\t\t {self.noodles.get()}\t{self.no}\n")
    if self.lays.get() != 0:
        self.txt_area.insert(END, f"Lays\t\t {self.lays.get()}\t{self.la}\n")
    if self.oreo.get() != 0:
        self.txt_area.insert(END, f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
    if self.muffin.get() != 0:
        self.txt_area.insert(END, f"Muffins\t\t {self.muffin.get()}\t{self.mu}\n")
    if self.silk.get() != 0:
        self.txt_area.insert(END, f"Silk\t\t {self.silk.get()}\t{self.si}\n")
    if self.coca_cola.get() != 0:
        self.txt_area.insert(END, f"Coca-Cola\t\t {self.coca_cola.get()}\t{self.co}\n")
    if self.eggs.get() != 0:
        self.txt_area.insert(END, f"Eggs\t\t {self.eggs.get()}\t{self.at}\n")
    if self.pasta.get() != 0:
        self.txt_area.insert(END, f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.rice.get() != 0:
        self.txt_area.insert(END, f"Rice\t\t {self.rice.get()}\t{self.ri}\n")
    if self.oil.get() != 0:
        self.txt_area.insert(END, f"Oil\t\t {self.oil.get()}\t{self.oi}\n")
    if self.sugar.get() != 0:
        self.txt_area.insert(END, f"Sugar\t\t {self.sugar.get()}\t{self.su}\n")
    if self.flour.get() != 0:
        self.txt_area.insert(END, f"Flour\t\t {self.flour.get()}\t{self.da}\n")
    if self.beef.get() != 0:
        self.txt_area.insert(END, f"Ground Beef\t\t {self.beef.get()}\t{self.te}\n")
    if self.soap.get() != 0:
        self.txt_area.insert(END, f"Soap\t\t {self.soap.get()}\t{self.so}\n")
    if self.shampoo.get() != 0:
        self.txt_area.insert(END, f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
    if self.lotion.get() != 0:
        self.txt_area.insert(END, f"Lotion\t\t {self.lotion.get()}\t{self.lo}\n")
    if self.cream.get() != 0:
        self.txt_area.insert(END, f"Cream\t\t {self.cream.get()}\t{self.cr}\n")
    if self.foam.get() != 0:
        self.txt_area.insert(END, f"Foam\t\t {self.foam.get()}\t{self.fo}\n")
    if self.mask.get() != 0:
        self.txt_area.insert(END, f"Mask\t\t {self.mask.get()}\t{self.ma}\n")
    if self.sanitizer.get() != 0:
        self.txt_area.insert(END, f"Sanitizer\t\t {self.sanitizer.get()}\t{self.sa}\n")

    self.txt_area.insert(END, f"------------------------------------\n")
    if self.a.get() != "0.0 €":
        self.txt_area.insert(END, f"Total Snacks Tax : {self.a.get()}\n")
    if self.b.get() != "0.0 €":
        self.txt_area.insert(END, f"Total Grocery Tax : {self.b.get()}\n")
    if self.c.get() != "0.0 €":
        self.txt_area.insert(END, f"Total Beauty&Hygiene Tax : {self.c.get()}\n")
    self.txt_area.insert(END, f"Total Bill Amount : {self.total_all_bil}\n")
    self.txt_area.insert(END, f"------------------------------------\n")


def clear(self):
    self.txt_area.delete(1.0, END)
    self.nutella.set(0)
    self.noodles.set(0)
    self.lays.set(0)
    self.oreo.set(0)
    self.muffin.set(0)
    self.silk.set(0)
    self.coca_cola.set(0)
    self.eggs.set(0)
    self.pasta.set(0)
    self.rice.set(0)
    self.oil.set(0)
    self.sugar.set(0)
    self.flour.set(0)
    self.beef.set(0)
    self.soap.set(0)
    self.shampoo.set(0)
    self.lotion.set(0)
    self.cream.set(0)
    self.foam.set(0)
    self.mask.set(0)
    self.sanitizer.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set(0)
    self.bill_no.set(0)
    self.bill_no.set(0)
    self.phone.set(0)


def exit1(self):
    self.root.destroy()


root = Tk()
obj = BillApp(root)
root.mainloop()
