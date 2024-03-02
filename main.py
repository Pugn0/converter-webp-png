from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

def converter_webp_para_png(pasta_origem):
    # Pasta de destino para os arquivos .png
    pasta_destino = os.path.join(pasta_origem, 'png')
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Listar todos os arquivos .webp na pasta de origem
    arquivos_webp = [arquivo for arquivo in os.listdir(pasta_origem) if arquivo.lower().endswith('.webp')]
    
    # Converter cada arquivo .webp para .png
    for arquivo_webp in arquivos_webp:
        # Caminho completo para o arquivo .webp
        caminho_arquivo_webp = os.path.join(pasta_origem, arquivo_webp)
        
        # Verifica se o arquivo de entrada é .webp
        if not arquivo_webp.lower().endswith('.webp'):
            print(f'O arquivo {arquivo_webp} não é um arquivo .webp válido.')
            continue
        
        # Cria o nome do arquivo de saída .png
        nome_arquivo_png = os.path.splitext(arquivo_webp)[0] + '.png'
        
        # Caminho completo para o arquivo de saída .png
        caminho_arquivo_png = os.path.join(pasta_destino, nome_arquivo_png)
        
        # Abre o arquivo .webp
        imagem_webp = Image.open(caminho_arquivo_webp)
        
        # Converte e salva a imagem como .png
        imagem_webp.save(caminho_arquivo_png, 'PNG')
        
        print(f'A imagem {arquivo_webp} foi convertida para {caminho_arquivo_png}.')

def selecionar_pasta():
    # Abrir diálogo para selecionar pasta
    pasta_origem = filedialog.askdirectory(title="Selecione a pasta onde estão as imagens")
    if pasta_origem:
        converter_webp_para_png(pasta_origem)

if __name__ == "__main__":
    # Interface gráfica para seleção de pasta
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal

    # Chamar a função para selecionar a pasta
    selecionar_pasta()
