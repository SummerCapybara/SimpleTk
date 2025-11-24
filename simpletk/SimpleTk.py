import tkinter as tk
from tkinter import ttk
from PIL import Image
from os import remove

class SimpleTk:
    
    def __init__(self, input_name):
        """Initialize window and set title."""
        self.Name = input_name
        self.window = tk.Tk()
        self.window.title(self.Name)
    
    # ============================
    # Window management
    # ============================


    def change_res(self, WIDTH=800, HEIGHT=600):
        """Change window resolution."""
        self.window.geometry(f"{WIDTH}x{HEIGHT}")

    def run(self):
        """Start Tkinter event loop."""
        self.window.mainloop()
    
    def title(self, text: str):
        """Set window title."""
        self.window.title(text)

    def resizable(self, width = True, height = True):
        self.window.resizable(width=width, height=height)

    def set_icon(self, file_path: str):
        try:
            img = tk.PhotoImage(file=file_path)
            self.window.iconphoto(False, img)
        except Exception as e:
            raise ValueError(f"Failed to set icon: {e}")
    
    # ============================
    # Style
    # ============================

    def CreateStyle(
        self,
        Name: str,
        Widget: str,
        foreground=None,
        background=None,
        font=None,
        borderwidth=None,
        relief=None,
        padding=None,
        width=None,
        anchor=None,
        justify=None,
        wraplength=None,
        focuscolor=None,
        lightcolor=None,
        darkcolor=None,
        troughcolor=None,
        sliderlength=None,
        sliderrelief=None,
        arrowsize=None,
        indicatormargin=None,
        indicatorcolor=None,
        indicatorsize=None,
        insertcolor=None,
        selectbackground=None,
        selectforeground=None
        ):
        style = ttk.Style(self.window)
        style_name = f"{Name}.T{Widget}"

        # Collect all kwargs
        kwargs = {
            "foreground": foreground,
            "background": background,
            "font": font,
            "borderwidth": borderwidth,
            "relief": relief,
            "padding": padding,
            "width": width,
            "anchor": anchor,
            "justify": justify,
            "wraplength": wraplength,
            "focuscolor": focuscolor,
            "lightcolor": lightcolor,
            "darkcolor": darkcolor,
            "troughcolor": troughcolor,
            "sliderlength": sliderlength,
            "sliderrelief": sliderrelief,
            "arrowsize": arrowsize,
            "indicatormargin": indicatormargin,
            "indicatorcolor": indicatorcolor,
            "indicatorsize": indicatorsize,
            "insertcolor": insertcolor,
            "selectbackground": selectbackground,
            "selectforeground": selectforeground
        }

        # Try to configure each option individually
        for k, v in kwargs.items():
            if v is not None:
                try:
                    style.configure(style_name, **{k: v})
                except tk.TclError:
                    pass  # silently ignore invalid options

        return style, style_name

    # ============================
    # Widgets
    # ============================


    def CreateButton(
                    self,
                    toolkit = "tk",
                    activebackground=None,
                    activeforeground=None,
                    anchor=None,
                    background=None, bg=None,
                    bd=None, borderwidth=None,
                    bitmap=None,
                    command=None,
                    compound=None,
                    cursor=None,
                    default=None,
                    disabledforeground=None,
                    font=None,
                    foreground=None, fg=None,
                    height=None,
                    highlightbackground=None,
                    highlightcolor=None,
                    highlightthickness=None,
                    image=None,
                    justify=None,
                    overrelief=None,
                    padx=None,
                    pady=None,
                    relief=None,
                    repeatdelay=None,
                    repeatinterval=None,
                    state=None,
                    takefocus=None,
                    text=None,
                    textvariable=None,
                    underline=None,
                    width=None,
                    wraplength=None,
                    style=None,
                    x=0, y=0,):
        """
        Create a button using tk or ttk.
        tk → supports fg/bg directly
        ttk → requires style for colors
        """
        if toolkit == "tk":
            Button = tk.Button(
                    self.window,
                    activebackground=activebackground,
                    activeforeground=activeforeground,
                    anchor=anchor,
                    background=background if background else bg,
                    bd=bd if bd else borderwidth,
                    bitmap=bitmap,
                    command=command,
                    compound=compound,
                    cursor=cursor,
                    default=default,
                    disabledforeground=disabledforeground,
                    font=font,
                    foreground=foreground if foreground else fg,
                    height=height,
                    highlightbackground=highlightbackground,
                    highlightcolor=highlightcolor,
                    highlightthickness=highlightthickness,
                    image=image,
                    justify=justify,
                    overrelief=overrelief,
                    padx=padx,
                    pady=pady,
                    relief=relief,
                    repeatdelay=repeatdelay,
                    repeatinterval=repeatinterval,
                    state=state,
                    takefocus=takefocus,
                    text=text,
                    textvariable=textvariable,
                    underline=underline,
                    width=width,
                    wraplength=wraplength)
            
        elif toolkit == "ttk":

            Button = ttk.Button(
                self.window,
                text=text,
                image=image,
                command=command,
                style=style,
                width=width,
                takefocus=takefocus,
                textvariable=textvariable,
                underline=underline,
            )

        else:
            raise ValueError('toolkit must be "tk" or "ttk".')


        Button.place(x=x, y=y)
        return Button

    def CreateLabel(
        self,
        toolkit="tk",
        anchor=None,
        background=None, bg=None,
        bd=None, borderwidth=None,
        bitmap=None,
        cursor=None,
        font=None,
        foreground=None, fg=None,
        height=None,
        highlightbackground=None,
        highlightcolor=None,
        highlightthickness=None,
        image=None,
        justify=None,
        padx=None,
        pady=None,
        relief=None,
        state=None,
        takefocus=None,
        text=None,
        textvariable=None,
        underline=None,
        width=None,
        wraplength=None,
        style=None,
        x=None, y=None,
    ):

        # tk-only options
        tk_only = {
            "background": background,
            "bg": bg,
            "foreground": foreground,
            "fg": fg,
            "highlightbackground": highlightbackground,
            "highlightcolor": highlightcolor,
            "highlightthickness": highlightthickness,
            "bitmap": bitmap,
        }

        # ttk-only arguments
        if toolkit == "tk" and style is not None:
            raise ValueError("tk.Label does not support 'style'. Use toolkit='ttk'.")

        if toolkit == "ttk":
            for name, value in tk_only.items():
                if value is not None:
                    raise ValueError(f"'{name}' is not supported by ttk.Label.")

        if toolkit == "tk":
            Label = tk.Label(
                self.window,
                anchor=anchor,
                background=background if background else bg,
                bd=bd if bd else borderwidth,
                bitmap=bitmap,
                cursor=cursor,
                font=font,
                foreground=foreground if foreground else fg,
                height=height,
                highlightbackground=highlightbackground,
                highlightcolor=highlightcolor,
                highlightthickness=highlightthickness,
                image=image,
                justify=justify,
                padx=padx,
                pady=pady,
                relief=relief,
                state=state,
                takefocus=takefocus,
                text=text,
                textvariable=textvariable,
                underline=underline,
                width=width,
                wraplength=wraplength,
            )

        elif toolkit == "ttk":
            Label = ttk.Label(
                self.window,
                text=text,
                image=image,
                justify=justify,
                padding=(padx, pady) if padx or pady else None,
                style=style,
                width=width,
                textvariable=textvariable,
                underline=underline,
            )

        else:
            raise ValueError('toolkit must be "tk" or "ttk".')

        Label.place(x=x, y=y)
        return Label

    def CreateEntry(self,
        toolkit="tk",
        background=None, bg=None,
        bd=None, borderwidth=None,
        cursor=None,
        disabledbackground=None,
        disabledforeground=None,
        exportselection=None,
        font=None,
        foreground=None, fg=None,
        highlightbackground=None,
        highlightcolor=None,
        highlightthickness=None,
        insertbackground=None,
        insertborderwidth=None,
        insertofftime=None,
        insertontime=None,
        insertwidth=None,
        justify=None,
        relief=None,
        selectbackground=None,
        selectborderwidth=None,
        selectforeground=None,
        show=None,
        state=None,
        takefocus=None,
        text=None,
        width=None,
        xscrollcommand=None,
        validate=None,
        validatecommand=None,
        invalidcommand=None,
        style=None,
        x=None, y=None,
    ):

        tk_only = {
            "background": background,
            "bg": bg,
            "foreground": foreground,
            "fg": fg,
            "highlightbackground": highlightbackground,
            "highlightcolor": highlightcolor,
            "highlightthickness": highlightthickness,
            "selectbackground": selectbackground,
            "selectforeground": selectforeground,
        }

        if toolkit == "tk" and style is not None:
            raise ValueError("tk.Entry does not support 'style'. Use ttk.")

        if toolkit == "ttk":
            for name, value in tk_only.items():
                if value is not None:
                    raise ValueError(f"'{name}' is not supported by ttk.Entry.")

        if toolkit == "tk":
            Entry = tk.Entry(
                self.window,
                background=background if background else bg,
                bd=bd if bd else borderwidth,
                cursor=cursor,
                disabledbackground=disabledbackground,
                disabledforeground=disabledforeground,
                exportselection=exportselection,
                font=font,
                foreground=foreground if foreground else fg,
                highlightbackground=highlightbackground,
                highlightcolor=highlightcolor,
                highlightthickness=highlightthickness,
                insertbackground=insertbackground,
                insertborderwidth=insertborderwidth,
                insertofftime=insertofftime,
                insertontime=insertontime,
                insertwidth=insertwidth,
                justify=justify,
                relief=relief,
                selectbackground=selectbackground,
                selectborderwidth=selectborderwidth,
                selectforeground=selectforeground,
                show=show,
                state=state,
                takefocus=takefocus,
                textvariable=text,
                width=width,
                xscrollcommand=xscrollcommand,
            )

        elif toolkit == "ttk":
            Entry = ttk.Entry(
                self.window,
                font=font,
                justify=justify,
                show=show,
                state=state,
                takefocus=takefocus,
                textvariable=text,
                validate=validate,
                validatecommand=validatecommand,
                invalidcommand=invalidcommand,
                width=width,
                xscrollcommand=xscrollcommand,
                style=style)

        else:
            raise ValueError('toolkit must be "tk" or "ttk".')

        Entry.place(x=x, y=y)
        return Entry
            
    def CreateText(self,
        text=None,
        background=None, bg=None,
        bd=None, borderwidth=None,
        blockcursor=None,
        cursor=None,
        exportselection=None,
        font=None,
        foreground=None, fg=None,
        height=None,
        highlightbackground=None,
        highlightcolor=None,
        highlightthickness=None,
        insertbackground=None,
        insertborderwidth=None,
        insertofftime=None,
        insertontime=None,
        insertwidth=None,
        maxundo=None,
        padx=None,
        pady=None,
        relief=None,
        selectbackground=None,
        selectborderwidth=None,
        selectforeground=None,
        setgrid=None,
        spacing1=None,
        spacing2=None,
        spacing3=None,
        state=None,
        tabstyle=None,
        takefocus=None,
        undo=None,
        width=None,
        wrap=None,
        xscrollcommand=None,
        yscrollcommand=None,
        x=None, y=None,
    ):

        Text = tk.Text(
            self.window,
            background=background if background else bg,
            bd=bd if bd else borderwidth,
            blockcursor=blockcursor,
            cursor=cursor,
            exportselection=exportselection,
            font=font,
            foreground=foreground if foreground else fg,
            height=height,
            highlightbackground=highlightbackground,
            highlightcolor=highlightcolor,
            highlightthickness=highlightthickness,
            insertbackground=insertbackground,
            insertborderwidth=insertborderwidth,
            insertofftime=insertofftime,
            insertontime=insertontime,
            insertwidth=insertwidth,
            maxundo=maxundo,
            padx=padx,
            pady=pady,
            relief=relief,
            selectbackground=selectbackground,
            selectborderwidth=selectborderwidth,
            selectforeground=selectforeground,
            setgrid=setgrid,
            spacing1=spacing1,
            spacing2=spacing2,
            spacing3=spacing3,
            state=state,
            tabstyle=tabstyle,
            takefocus=takefocus,
            undo=undo,
            width=width,
            wrap=wrap,
            xscrollcommand=xscrollcommand,
            yscrollcommand=yscrollcommand,
        )

        Text.place(x=x, y=y)

        if text is not None:
            Text.insert("1.0", text)

        return Text

    def CreateCheckbutton(
        self,
        toolkit="tk",
        text=None,
        variable=None,
        onvalue=1,
        offvalue=0,
        command=None,
        state=None,
        anchor=None,
        justify=None,
        background=None, bg=None,
        foreground=None, fg=None,
        font=None,
        padx=None,
        pady=None,
        width=None,
        height=None,
        selectcolor=None,
        x=None, y=None
    ):
        """Create a Checkbutton (tk or ttk)."""
        if toolkit == "tk":
            cb = tk.Checkbutton(
                self.window,
                text=text,
                variable=variable,
                onvalue=onvalue,
                offvalue=offvalue,
                command=command,
                state=state,
                anchor=anchor,
                justify=justify,
                background=background or bg,
                foreground=foreground or fg,
                font=font,
                padx=padx,
                pady=pady,
                width=width,
                height=height,
                selectcolor=selectcolor
            )
        elif toolkit == "ttk":
            if background or bg or foreground or fg or selectcolor:
                raise ValueError("ttk.Checkbutton uses Styles, not direct fg/bg/selectcolor.")
            cb = ttk.Checkbutton(
                self.window,
                text=text,
                variable=variable,
                onvalue=onvalue,
                offvalue=offvalue,
                command=command,
                state=state
            )
        else:
            raise ValueError('Toolkit must be "tk" or "ttk".')
        cb.place(x=x, y=y)
        return cb

    def CreateRadiobutton(
        self,
        toolkit="tk",
        text=None,
        variable=None,
        value=None,
        command=None,
        state=None,
        anchor=None,
        justify=None,
        background=None, bg=None,
        foreground=None, fg=None,
        font=None,
        padx=None,
        pady=None,
        width=None,
        height=None,
        indicatoron=True,
        x=None, y=None
    ):
        """Create a Radiobutton (tk or ttk)."""
        if toolkit == "tk":
            rb = tk.Radiobutton(
                self.window,
                text=text,
                variable=variable,
                value=value,
                command=command,
                state=state,
                anchor=anchor,
                justify=justify,
                background=background or bg,
                foreground=foreground or fg,
                font=font,
                padx=padx,
                pady=pady,
                width=width,
                height=height,
                indicatoron=indicatoron
            )
        elif toolkit == "ttk":
            if background or bg or foreground or fg:
                raise ValueError("ttk.Radiobutton uses Styles, not direct fg/bg.")
            rb = ttk.Radiobutton(
                self.window,
                text=text,
                variable=variable,
                value=value,
                command=command,
                state=state
            )
        else:
            raise ValueError('Toolkit must be "tk" or "ttk".')
        rb.place(x=x, y=y)
        return rb

    def CreateScale(
        self,
        toolkit="tk",
        from_=0,
        to=100,
        orient="horizontal",
        length=None,
        resolution=1,
        tickinterval=0,
        variable=None,
        command=None,
        state=None,
        showvalue=True,
        sliderlength=None,
        troughcolor=None,
        background=None, bg=None,
        foreground=None, fg=None,
        font=None,
        x=None, y=None
    ):
        """Create a Scale (slider) widget."""
        if toolkit == "tk":
            sc = tk.Scale(
                self.window,
                from_=from_,
                to=to,
                orient=orient,
                length=length,
                resolution=resolution,
                tickinterval=tickinterval,
                variable=variable,
                command=command,
                state=state,
                showvalue=showvalue,
                sliderlength=sliderlength,
                troughcolor=troughcolor,
                background=background or bg,
                foreground=foreground or fg,
                font=font
            )
        elif toolkit == "ttk":
            if background or bg or foreground or fg or troughcolor or sliderlength:
                raise ValueError("ttk.Scale uses Styles, not direct fg/bg/troughcolor.")
            sc = ttk.Scale(
                self.window,
                from_=from_,
                to=to,
                orient=orient,
                length=length,
                command=command,
                variable=variable
            )
        else:
            raise ValueError('Toolkit must be "tk" or "ttk".')
        sc.place(x=x, y=y)
        return sc


    def CreateListbox(
        self,
        selectmode="browse",
        height=None,
        width=None,
        background=None, bg=None,
        foreground=None, fg=None,
        font=None,
        x=None, y=None
    ):
        """Create a Listbox widget (tk only)."""
        lb = tk.Listbox(
            self.window,
            selectmode=selectmode,
            height=height,
            width=width,
            background=background or bg,
            foreground=foreground or fg,
            font=font
        )
        lb.place(x=x, y=y)
        return lb


    def CreateCombobox(
        self,
        values=None,
        state="normal",
        width=None,
        font=None,
        x=None, y=None
    ):
        """Create a ttk Combobox (dropdown list)."""
        cb = ttk.Combobox(
            self.window,
            values=values,
            state=state,
            width=width,
            font=font
        )
        cb.place(x=x, y=y)
        return cb


    def CreateProgressbar(
        self,
        orient="horizontal",
        length=None,
        mode="determinate",
        maximum=100,
        value=0,
        variable=None,
        x=None, y=None
    ):
        """Create a ttk Progressbar."""
        pb = ttk.Progressbar(
            self.window,
            orient=orient,
            length=length,
            mode=mode,
            maximum=maximum,
            value=value,
            variable=variable
        )
        pb.place(x=x, y=y)
        return pb


    def destroy(self):
        """Destroy the window."""
        self.window.destroy()