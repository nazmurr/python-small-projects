'''
Image editor with tkinter and pillow
features:
- select image
- rotate
- crop
- brightness
- contrast
- filters
- reset image
- save image
'''
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image, ImageEnhance, ImageFilter
import PIL

#image editor class
class ImageEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Editor")
        self.geometry("800x500")
        self.resizable(False, False)

        self.img = None
        self.selected_filter = None

        #image frame (left column)
        self.image_frame = tk.Frame(self)
        self.image_frame.pack(ipadx=10, ipady=10, expand=True, fill='both', side='left')

        #buttons frame (right column)
        self.buttons_frame = tk.Frame(self, width=200)
        self.buttons_frame.pack(ipadx=10, ipady=10, expand=True, fill='both')

        #select image button
        self.select_image_button = ttk.Button(self.buttons_frame, text='Select Image', command=self.select_image)
        self.select_image_button.pack(padx=10, pady=10)

        #rotate image button
        self.rotate_image_button = ttk.Button(self.buttons_frame, text='Rotate', command=self.rotate_image)
        self.rotate_image_button.pack(padx=10, pady=10)
        self.crop_image_button = ttk.Button(self.buttons_frame, text='Crop', command=self.crop_image)
        self.crop_image_button.pack(padx=10, pady=(0,10))

        #brightness label and slider
        self.brightness_label = ttk.Label(self.buttons_frame, text='Brightness')
        self.brightness_label.pack(padx=10, pady=(10,0))
        self.brightness_slider = ttk.Scale(
            self.buttons_frame, 
            from_=0, 
            to=2.0, 
            variable=None, 
            command=self.image_brightness_control
        )
        self.brightness_slider.set(1.0)
        self.brightness_slider.pack(padx=10, pady=(0,10))

        #contrast label and slider
        self.contrast_label = ttk.Label(self.buttons_frame, text='Contrast')
        self.contrast_label.pack(padx=10, pady=(10,0))
        self.contrast_slider = ttk.Scale(
            self.buttons_frame, 
            from_=0, 
            to=2.0, 
            variable=None, 
            command=self.image_contrast_control
        )
        self.contrast_slider.set(1.0)
        self.contrast_slider.pack(padx=10, pady=(0,10))

        #filters label and combobox
        self.filters_label = ttk.Label(self.buttons_frame, text='Filters')
        self.filters_label.pack(padx=10, pady=(10, 0))
        self.filters = ttk.Combobox(self.buttons_frame, width=10)
        self.filters['values'] = ['Blur', 'Contour', 'Emboss', 'Greyscale']
        self.filters['state'] = 'readonly'
        self.filters.pack(padx=10, pady=(0,10))
        self.filters.bind('<<ComboboxSelected>>', self.filters_changed)
        
        #reset image and save image buttons
        self.reset_image_button = ttk.Button(self.buttons_frame, text='Reset', command=self.reset_image)
        self.reset_image_button.pack(padx=10, pady=10)
        self.save_image_button = ttk.Button(self.buttons_frame, text='Save', command=self.save_image)
        self.save_image_button.pack(padx=10, pady=(0,0))

    #select_image function to handle image selection from os
    def select_image(self):
        try:
            filetypes = (
                ('JPG files', '*.jpg'),
                ('JPEG files', '*.jpeg'),
                ('PNG files', '*.png'),
            )
            f = fd.askopenfile(filetypes=filetypes)
            self.img = Image.open(f.name)
            self.img.thumbnail((600,450))
            self.org_img = self.img
            self.show_image(self.img)
            self.image_format = self.img.format
            self.brightness_slider.set(1.0)
            self.contrast_slider.set(1.0)
        except Exception as e:
            print(e)
            print('No image selected')

    #rotate_image function to rotate image by 90 degree on each click
    def rotate_image(self):
        try:
            self.img = self.img.rotate(90, PIL.Image.Resampling.NEAREST, 1)
            self.show_image(self.img)
        except:
            print('No image selected')

    #crop_image function to crop image by 300x300 px from top left of the image
    def crop_image(self):
        try:
            self.img = self.img.crop((0,0,300,300))
            self.show_image(self.img)
        except:
            print('No image selected')

    #show_image function to display image on the ui with brightness, contrast and filters applied
    def show_image(self, img):
        enhanced_img = self.apply_image_brightness(img, self.brightness_level)
        enhanced_img = self.apply_image_contrast(enhanced_img, self.contrast_level)
        enhanced_img = self.apply_filter(enhanced_img, self.selected_filter)
        self.updated_img = ImageTk.PhotoImage(enhanced_img)
        self.image_label = ttk.Label(self.image_frame, image = self.updated_img, borderwidth=0)
        self.image_label.place(relx=.5, rely=.5, anchor=tk.CENTER)

    #save_image function to save the edited image on os
    def save_image(self):
        try:
            filetypes = ()
            if self.image_format == 'PNG':
                filetypes = (
                    ('PNG files', '*.png'),
                )
            else:
                filetypes = (
                    ('JPG files', '*.jpg'),
                    ('JPEG files', '*.jpeg'),
                )

            f = fd.asksaveasfile( 
                defaultextension="." + self.image_format.lower(),
                filetypes=filetypes
            )
            savable_img = self.apply_image_brightness(self.img, self.brightness_level)
            savable_img = self.apply_image_contrast(savable_img, self.contrast_level)
            savable_img = self.apply_filter(savable_img, self.selected_filter)
            savable_img.save(f.name)
        except Exception as e:
            print('No image selected')

    #reset_image function to reset all editing
    def reset_image(self):
        try:
            self.brightness_slider.set(1.0)
            self.contrast_slider.set(1.0)
            self.filters.set('')
            self.selected_filter = None
            self.img = self.org_img
            self.show_image(self.img)
        except:
            print('No image selected')

    #image_brightness_control function save slider value
    def image_brightness_control(self, event):
        try:
            self.brightness_level = float('{: .1f}'.format(self.brightness_slider.get()))
            if self.img != None:
                self.show_image(self.img)
        except:
            print('No image selected')

    #image_contrast_control function save slider value
    def image_contrast_control(self, event):
        try:
            self.contrast_level = float('{: .1f}'.format(self.contrast_slider.get()))
            if self.img != None:
                self.show_image(self.img)
        except:
            print('No image selected')

    #apply_image_brightness function to apply current brightness to image
    def apply_image_brightness(self, img, brightness_level):
        img_enhancer = ImageEnhance.Brightness(img)
        return img_enhancer.enhance(brightness_level)
    
    #apply_image_contrast function to apply current contrast to image
    def apply_image_contrast(self, img, contrast_level):
        img_enhancer = ImageEnhance.Contrast(img)
        return img_enhancer.enhance(contrast_level)

    #filters_changed function to save combobox selected value
    def filters_changed(self, event):
        try:
            self.selected_filter = self.filters.get()
            self.show_image(self.img)
        except:
            print('No image selected')

    #apply_filter function to apply blue, contour, emboss and greyscale filter to the image
    def apply_filter(self, img, filter):
        filtered_img = None
        if filter == 'Blur':
            filtered_img = img.filter(ImageFilter.BLUR)
        elif filter == 'Contour':
            filtered_img = img.filter(ImageFilter.CONTOUR)
        elif filter == 'Emboss':
            filtered_img = img.filter(ImageFilter.EMBOSS)
        elif filter == 'Greyscale':
            filtered_img = img.convert('L')
        else:
            filtered_img = img

        return filtered_img

if __name__ == "__main__":
    image_editor = ImageEditor() #instantiate ImageEditor class
    image_editor.mainloop()