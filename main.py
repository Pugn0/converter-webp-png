from PIL import Image
import os

def converter_webp_para_png(arquivo_webp, pasta_destino):
    # Verifica se o arquivo de entrada é .webp
    if not arquivo_webp.lower().endswith('.webp'):
        print(f'O arquivo {arquivo_webp} não é um arquivo .webp válido.')
        return
    
    # Cria o nome do arquivo de saída .png
    nome_arquivo_png = os.path.splitext(os.path.basename(arquivo_webp))[0] + '.png'
    
    # Caminho completo para o arquivo de saída .png
    caminho_arquivo_png = os.path.join(pasta_destino, nome_arquivo_png)
    
    # Abre o arquivo .webp
    imagem_webp = Image.open(arquivo_webp)
    
    # Converte e salva a imagem como .png
    imagem_webp.save(caminho_arquivo_png, 'PNG')
    
    print(f'A imagem {arquivo_webp} foi convertida para {caminho_arquivo_png}.')

if __name__ == "__main__":
    # Pasta onde estão os arquivos .webp (diretório atual)
    pasta_origem = os.getcwd()
    
    # Criar pasta 'png' dentro do diretório atual
    pasta_destino = os.path.join(pasta_origem, 'png')
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Listar todos os arquivos .webp no diretório atual
    arquivos_webp = [arquivo for arquivo in os.listdir(pasta_origem) if arquivo.lower().endswith('.webp')]
    
    # Converter cada arquivo .webp para .png
    for arquivo_webp in arquivos_webp:
        converter_webp_para_png(arquivo_webp, pasta_destino)
