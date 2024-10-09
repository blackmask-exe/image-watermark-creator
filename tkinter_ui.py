import customtkinter as tk
from sqlalchemy import column
from PIL import Image
from tkinter import filedialog


class App(tk.CTk):
    def __init__(self):
        super().__init__()

        # WINDOW LAYOUT SETUP
        self.title("Watermark Adder")
        self.geometry("510x510")

        # Allow the frames to expand and fill the available space
        self.grid_rowconfigure(0, weight=1)  # Row for the upload image frame
        self.grid_rowconfigure(1, weight=0)  # Row for the watermark frame
        self.grid_columnconfigure(0, weight=1)

        # COMPONENT SETUP

        # 1. Upload Photo box, and it goes away once the photo has been uploaded
        #    and in place of it, the preview of the photo takes its place
        self.upload_img_frame = UploadImageFrame(self)
        self.upload_img_frame.configure(width=550, height=400)
        self.upload_img_frame.grid(row=0, column=0)

        # 2. Frame with "Add Watermark" on the bottom
        self.watermark_frame = AddWatermarkFrame(self)
        self.watermark_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)


class AddWatermarkFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Text box saying what watermark you want to put in
        self.watermark_entry = tk.CTkEntry(self, placeholder_text="Enter Watermark Here", width=300, justify="center", )
        self.watermark_entry.grid(column=0, row=0, sticky="ew", padx=(10, 0))

        # Button saying "add watermark"
        self.button_add_watermark = tk.CTkButton(master=self, text="Add Watermark")
        self.button_add_watermark.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
        self.grid_columnconfigure(0, weight=1)


def get_photo_file_path():
    return filedialog.askopenfilename()


class UploadImageFrame(tk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.preview_img = None
        self.preview_img_element = None
        self.photo_filepath = None
        self.button_upload_image = tk.CTkButton(master=self, text="Upload Image", command=self.display_preview_img)
        self.button_upload_image.grid(row=0, column=0, sticky="ew")

    def display_preview_img(self):
        self.preview_img = Image.open(get_photo_file_path())
        # self.preview_img = self.preview_img.resize((150, 150))

        desired_width = 500

        # Calculate the height maintaining aspect ratio
        aspect_ratio = self.preview_img.height / self.preview_img.width
        desired_height = int(desired_width * aspect_ratio)
        self.preview_img_element = tk.CTkImage(dark_image=self.preview_img, size=(desired_width, desired_height))
        # self.button_upload_image.configure(image=self.preview_img_element, text="")
        # self.button_upload_image.grid(row=0, column=0, sticky="ew")
        # creating a new label in order to display the image preview
        self.img_preview_label = tk.CTkLabel(self, text="", image=self.preview_img_element)
        self.img_preview_label.grid(row=1, column=0)



if __name__ == "__main__":
    app = App()
    app.focus_force()
    app.mainloop()
