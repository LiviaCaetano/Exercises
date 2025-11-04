import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Cálculo do IMC - Índice de Massa Corporal')
app.geometry('700x400')
app.resizable(False, False) #Não permite maximizar/minimizar

fonte_label = ("Arial", 15)
fonte_entry = ("Arial", 13)

def calculate_imc():
    try:
        name = campo_name.get()
        height = float(campo_height.get()) / 100  
        weight = float(campo_weight.get())

        imc = weight / (height * height)  

        if imc < 17:
            classificacao = "Muito abaixo do peso"
        elif imc <= 18.49:
            classificacao = "Abaixo do peso"
        elif imc <= 24.99:
            classificacao = "Peso normal"
        elif imc <= 29.99:
            classificacao = "Acima do peso"
        elif imc <= 34.99:
            classificacao = "Obesidade grau I"
        elif imc <= 39.99:
            classificacao = "Obesidade grau II (severa)"
        else:
            classificacao = "Obesidade grau III"

        resultado_texto = (
            f"{name} tem {height:.2f} m de altura.\n"
            f"Seu peso é de {weight:.1f} kg\n"
            f"Seu IMC é de {imc:.2f}\n\n"
            f"Classificação: {classificacao}"
        )
        label_result.configure(text=resultado_texto)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")  # messagebox.showerror- caixa de diálogo

def reiniciar():
    campo_name.delete(0, 'end')
    campo_addres.delete(0, 'end')  
    campo_height.delete(0, 'end')
    campo_weight.delete(0, 'end')
    label_result.configure(text="Resultado")

def sair():
    app.destroy()

frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack(side="bottom", fill="x", pady=10)

btn_calculate = ctk.CTkButton(frame_buttons, text='Calcular', width=120, command=calculate_imc)
btn_calculate.pack(side="left", padx=20, pady=10)

btn_restart = ctk.CTkButton(frame_buttons, text='Reiniciar', width=120, command=reiniciar)
btn_restart.pack(side="left", padx=20, pady=10)

btn_exit = ctk.CTkButton(frame_buttons, text='Sair', width=120, command=sair)
btn_exit.pack(side="right", padx=20, pady=10)

frame_main = ctk.CTkFrame(app)
frame_main.pack(fill="both", expand=True, padx=10, pady=(0, 5))

frame_fields = ctk.CTkFrame(frame_main)
frame_fields.pack(side="left", fill="both", expand=True, padx=20, pady=20)

frame_result = ctk.CTkFrame(frame_main)
frame_result.pack(side="right", fill="both", expand=True, padx=20, pady=20)

label_name = ctk.CTkLabel(frame_fields, text='Nome do Paciente:', font=fonte_label)
label_name.pack(anchor="w")
campo_name = ctk.CTkEntry(frame_fields, placeholder_text='Digite seu nome', width=350, font=fonte_entry)
campo_name.pack(pady=(5, 10), anchor='w')

label_addres = ctk.CTkLabel(frame_fields, text='Endereço Completo:', font=fonte_label)
label_addres.pack(anchor="w")
campo_addres = ctk.CTkEntry(frame_fields, placeholder_text='Digite seu endereço', width=350, font=fonte_entry)
campo_addres.pack(pady=(5, 10), anchor='w')

label_height = ctk.CTkLabel(frame_fields, text='Altura (cm):', font=fonte_label)
label_height.pack(anchor="w")
campo_height = ctk.CTkEntry(frame_fields, placeholder_text='Digite sua altura em cm', width=200, font=fonte_entry)
campo_height.pack(pady=(5, 10), anchor='w')

label_peso = ctk.CTkLabel(frame_fields, text='Peso (Kg):', font=fonte_label)
label_peso.pack(anchor="w")
campo_weight = ctk.CTkEntry(frame_fields, placeholder_text='Digite seu peso em Kg', width=200, font=fonte_entry)
campo_weight.pack(pady=(5, 10), anchor='w')

label_result = ctk.CTkLabel(
    frame_result,
    text='Resultado',
    width=250,
    height=150,
    font=("Arial", 15),
    fg_color=("gray20", "gray30"),
    corner_radius=10,
    justify="center"
)
label_result.pack(pady=30, padx=20, fill="both", expand=True)

app.mainloop()
