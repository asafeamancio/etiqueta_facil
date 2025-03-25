import os
import fitz

def dividir_pdf_em_4(input_path, output_file):
    pdf = fitz.open(input_path)
    novo_pdf = fitz.open()

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)
        rect = page.rect

        largura_metade = rect.width / 2
        altura_metade = rect.height / 2

        quadrantes = [
            fitz.Rect(0, 0, largura_metade, altura_metade),
            fitz.Rect(largura_metade, 0, rect.width, altura_metade),
            fitz.Rect(0, altura_metade, largura_metade, rect.height),
            fitz.Rect(largura_metade, altura_metade, rect.width, rect.height)
        ]

        for quad in quadrantes:
            nova_pagina = novo_pdf.new_page(width=quad.width, height=quad.height)
            nova_pagina.show_pdf_page(nova_pagina.rect, pdf, page_num, clip=quad)

    novo_pdf.save(output_file)
    novo_pdf.close()
    pdf.close()


# Diretórios
input_folder = './pasta1'
output_folder = './pasta2'
os.makedirs(output_folder, exist_ok=True)

output_file_path = os.path.join(output_folder, 'pdf_unificado.pdf')
novo_pdf_unificado = fitz.open()

for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        input_file_path = os.path.join(input_folder, filename)
        dividir_pdf_em_4(input_file_path, output_file_path)

print('Processo concluído.')
