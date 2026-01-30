import customtkinter as ctk
import os
from tkinter import filedialog
from colorama import Fore, Back, Style


# Настройка внешнего вида
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Заголовок окна
        self.title("Not‑a‑Virus")
        self.geometry("1000x600")
        self.resizable(True, True)

        # Сетка: 1 колонка для сайдбара, 3 — для контента
        self.grid_columnconfigure(0, weight=1, minsize=200)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # Левый сайдбар
        self.sidebar = ctk.CTkFrame(self, corner_radius=10)
        self.sidebar.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")
        self.sidebar.grid_rowconfigure(4, weight=1)

        # Заголовок в сайдбаре
        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="Not‑a‑Virus",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(pady=(20, 10))

        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="Антивирусное ПО",
            font=ctk.CTkFont(size=15, weight="bold")
        )
        self.title_label.pack(pady=(20, 10))

        # Кнопки разделов
        self.btn_scan = ctk.CTkButton(
            self.sidebar,
            text="Проверка на вирусы",
            command=self.show_scan,
            corner_radius=8,
            fg_color="#1f538d",
            hover_color="#143d6d"
        )
        self.btn_scan.pack(pady=10, padx=15, fill="x")

        self.btn_settings = ctk.CTkButton(
            self.sidebar,
            text="Настройки",
            command=self.show_settings,
            corner_radius=8,
            fg_color="#1f538d",
            hover_color="#143d6d"
        )
        self.btn_settings.pack(pady=10, padx=15, fill="x")

        self.btn_theme = ctk.CTkButton(
            self.sidebar,
            text="Инфо",
            command=self.show_info,
            corner_radius=8,
            fg_color="#1f538d",
            hover_color="#143d6d"
        )
        self.btn_theme.pack(pady=10, padx=15, fill="x")

        # Центральная область контента
        self.content_frame = ctk.CTkFrame(self, corner_radius=10)
        self.content_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nswe")
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        # Изначально показываем «Проверку на вирусы»
        self.show_scan()

    def clear_content(self):
        """Удаляет все виджеты из центральной области"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_scan(self):
        self.clear_content()
        label = ctk.CTkLabel(
            self.content_frame,
            text="ПРОВЕРКА НА ВИРУСЫ",
            font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, pady=0, padx=20, sticky="n")

        label = ctk.CTkLabel(
            self.content_frame,
            text="Проверка находится в версии альфа",
            font=ctk.CTkFont(size=12, weight="normal")
        ).grid(row=1, column=0, pady=0, padx=20, sticky="n")

        label = ctk.CTkLabel(
            self.content_frame,
            text="Есть ошибки.",
            font=ctk.CTkFont(size=12, weight="normal")
        ).grid(row=2, column=0, pady=0, padx=20, sticky="n")

        label = ctk.CTkLabel(
            self.content_frame,
            text="---------------------------",
            font=ctk.CTkFont(size=12, weight="normal")
        ).grid(row=3, column=0, pady=0, padx=20, sticky="n")
            
        def virus_check():

            def bat():
                alert_words = [['shutdown', ''], ['echo', '>'],
                [':', 'goto'], ['del', '/s', '/q', 'C:\\', '*.*'],
                ['rmdir', '/s', '/q', 'C:\\'], ['net', 'user'],
                ['net', 'localgroup', '/add'],]

                def print_list(list_):
                    return ', '.join(list_)


                def check_file(filename, encoding='utf-8'):
                    if os.path.exists(filename):
                        with open(filename, 'r', encoding=encoding) as f:
                            contents = f.read()
                            contents_list = contents.split('\n')
                            for line in contents_list:
                                for words in alert_words:
                                    x = True
                                    true_words = []
                                    c = 0
                                    for word in words:
                                        true_words.append(word)
                                        c += 1
                                        if word not in line:
                                            x = False
                                            break
                                    if x:
                                        os.system('cls')
                                        os.system('color e')
                                        print(f'{Fore.LIGHTYELLOW_EX}Найдено: {Fore.LIGHTRED_EX}{print_list(true_words)}{Style.RESET_ALL}')
                                        print()
                                    
                    else:
                        print("File not found")

                file = filedialog.askopenfile(title="Select file",

                filetypes=(("bat", "*.bat"), ("all files", "*.*")))

                check_file(file.name)

                app.destroy()

                a = input('Press Enter to close >>> ')
                os.system('cls')
                

                      
            # Настройка внешнего вида (можно изменить по желанию)
            ctk.set_appearance_mode("dark")      # Тёмный режим
            ctk.set_default_color_theme("blue")  # Синяя тема

            # Создание главного окна
            app = ctk.CTk()
            app.title("Not-a-Virus")
            app.geometry("400x300")

            # Центрирование окна на экране
            app.update_idletasks()
            x = (app.winfo_screenwidth() // 2) - (app.winfo_width() // 2)
            y = (app.winfo_screenheight() // 2) - (app.winfo_height() // 2)
            app.geometry(f"+{x}+{y}")

            # Заголовок по центру
            title_label = ctk.CTkLabel(
                app,
                text="Not-a-Virus",
                font=ctk.CTkFont(size=24, weight="bold")
            )
            title_label.pack(pady=(20, 10))

            # Текст "Выбор" под заголовком
            choice_label = ctk.CTkLabel(
                app,
                text="Выбор",
                font=ctk.CTkFont(size=16)
            )
            choice_label.pack(pady=(0, 20))

            # Функция-заглушка для кнопок (можно заменить на нужную логику)
            def on_button_click(button_name):
                print(f"Нажата кнопка: {button_name}")

##            # Кнопка "Пайтон"
##            python_button = ctk.CTkButton(
##                app,
##                text=".py",
##                command=lambda: on_button_click("Пайтон")
##            )
##            python_button.pack(pady=10)

            # Кнопка "Батник"
            batch_button = ctk.CTkButton(
                app,
                text=".bat",
                command=bat
            )
            batch_button.pack(pady=10)

##            # Кнопка ".exe"
##            exe_button = ctk.CTkButton(
##                app,
##                text="Exe",
##                command=lambda: on_button_click("Exe")
##            )
##            exe_button.pack(pady=10)

            choice_label = ctk.CTkLabel(
                app,
                text="Результат будет в консоли",
                font=ctk.CTkFont(size=16)
            )
            choice_label.pack(pady=(0, 40))

            choice_label = ctk.CTkLabel(
                app,
                text="Скоро добавим еще расширений",
                font=ctk.CTkFont(size=16)
            )
            choice_label.pack(pady=(0, 60))

            app.mainloop()

        btn_run = ctk.CTkButton(
            self.content_frame,
            text="Запустить проверку",
            fg_color="#1f538d",
            hover_color="#143d6d",
            command=virus_check
        )
        btn_run.grid(row=4, column=0, pady=10, padx=20, sticky="n")

    def show_settings(self):
        self.clear_content()
        label = ctk.CTkLabel(
            self.content_frame,
            text="НАСТРОЙКИ",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        label.grid(row=0, column=0, pady=0, padx=20, sticky="n")

        ctk.CTkLabel(
            self.content_frame,
            text="Выберите параметры работы программы:"
        ).grid(row=1, column=0, pady=5, padx=20, sticky="n")

        switch1 = ctk.CTkSwitch(self.content_frame, text="В разработке")
        switch1.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        switch2 = ctk.CTkSwitch(self.content_frame, text="В разработке")
        switch2.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        btn_save = ctk.CTkButton(
            self.content_frame,
            text="Сохранить настройки",
            fg_color="#1f538d",
            hover_color="#143d6d"
        )
        btn_save.grid(row=4, column=0, pady=20, padx=20, sticky="w")

    def show_info(self):
        self.clear_content()
        label = ctk.CTkLabel(
            self.content_frame,
            text="ИНФО",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        label.grid(row=0, column=0, pady=20, padx=20, sticky="n")

        ctk.CTkLabel(
            self.content_frame,
            text="Разработчик: @KotyaDev"
        ).grid(row=2, column=0, pady=3, padx=20, sticky="w")

        ctk.CTkLabel(
            self.content_frame,
            text="Издатель: @KotyashkaRU"
        ).grid(row=1, column=0, pady=4, padx=20, sticky="w")

        ctk.CTkLabel(
            self.content_frame,
            text="Версия: Alpha v0.1.0"
        ).grid(row=3, column=0, pady=4, padx=20, sticky="w")

        ctk.CTkLabel(
            self.content_frame,
            text="Вся программа сделана командой KotyaDev. Все права защищены. KotyaDev 2025"
        ).grid(row=4, column=1, pady=4, padx=20, sticky="w")


def main():
    app = App()
    app.mainloop()
# Запуск приложения
#Вся программа сделана командой KotyaDev. Все права защищены. KotyaDev 2025
