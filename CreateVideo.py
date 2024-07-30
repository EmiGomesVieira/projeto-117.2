import os
import cv2

# Defina o caminho para a pasta de imagens
path = "Images"

# Crie uma lista para armazenar os nomes dos arquivos de imagem
images = []

# Verifique cada arquivo na pasta
for file in os.listdir(path):
    # Separe o nome do arquivo e a extensão
    name, ext = os.path.splitext(file)
    # Verifique se a extensão do arquivo corresponde à extensão da imagem (por exemplo, .jpg, .jpeg, .png)
    if ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        # Crie o nome completo do arquivo
        file_name = os.path.join(path, file)
        print(f"Arquivo adicionado: {file_name}")  # Certifique-se de que os nomes dos arquivos sejam formados corretamente
        # Adicione o arquivo à lista de imagens
        images.append(file_name)

# Contador de imagens
count = len(images)
print(f"Total de imagens encontradas: {count}")

# Verifique se há imagens na lista
if count == 0:
    print("Nenhuma imagem encontrada na pasta.")
else:
    # Leia a primeira imagem para capturar suas dimensões
    frame = cv2.imread(images[0])
    if frame is None:
        print(f"Erro ao ler a imagem: {images[0]}")
    height, width, channels = frame.shape
    size = (width, height)
    print(f"Dimensões da imagem: {size}")  # Verifique o resultado das dimensões

    # Crie o objeto VideoWriter
    out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

    # Adicione as imagens ao VideoWriter
    for i in range(count):
        frame = cv2.imread(images[i])
        if frame is None:
            print(f"Erro ao ler a imagem: {images[i]}")
            continue
        # Redimensione a imagem para o tamanho da primeira imagem, se necessário
        if (frame.shape[1], frame.shape[0]) != size:
            frame = cv2.resize(frame, size)
        out.write(frame)
        print(f"Imagem {i+1} adicionada ao vídeo: {images[i]}")

    # Libere o objeto VideoWriter
    out.release()
    print("Vídeo concluído")



