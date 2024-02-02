import tkinter as tk
from tkinter import messagebox

def calcular_lucro():
    try:
        valor = float(entrada_valor.get())
        porcentagem = float(entrada_porcentagem.get())
        frete = float(entrada_frete.get())
        lucro = valor * (porcentagem / 100)
        total = valor + lucro + frete
        resultado.config(text=f"Total: R$ {total:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores válidos.")

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora de Lucro")

# Criando widgets
etiqueta_valor = tk.Label(janela, text="Valor:")
etiqueta_valor.pack()

entrada_valor = tk.Entry(janela)
entrada_valor.pack()

etiqueta_porcentagem = tk.Label(janela, text="Porcentagem de Lucro:")
etiqueta_porcentagem.pack()

entrada_porcentagem = tk.Entry(janela)
entrada_porcentagem.pack()

etiqueta_frete = tk.Label(janela, text="Frete:")
etiqueta_frete.pack()

entrada_frete = tk.Entry(janela)
entrada_frete.pack()

botao_calcular = tk.Button(janela, text="Calcular", command=calcular_lucro)
botao_calcular.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

# Iniciando a interface gráfica
janela.mainloop()
