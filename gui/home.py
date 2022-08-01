import customtkinter
import tkinter


class App(customtkinter.CTk):
    def __init__(self, button_event):
        super().__init__()

        self.geometry(f"{600}x{500}")
        self.title("CTk example")
        mic_image = tkinter.PhotoImage(file='images/mic_icon.png')
        mic_image = mic_image.subsample(2)

        button = customtkinter.CTkButton(master=self,
                                         width=60,
                                         height=120,
                                         border_width=0,
                                         corner_radius=120,
                                         fg_color="#222325",
                                         hover_color="#222325",
                                         text="",
                                         image=mic_image,
                                         command=button_event)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
