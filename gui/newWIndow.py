import customtkinter
import tkinter


class NewWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{600}x{100}")
        self.title("Inputs and Output")

    def createAndFillLabel(self, text):
        # self.button.destroy()
        label = customtkinter.CTkLabel(master=self,
                                       fg_color=("white", "gray75"),
                                       text=text,
                                       corner_radius=8)
        label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
