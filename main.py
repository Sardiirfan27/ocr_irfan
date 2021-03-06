#import principal
import streamlit as st
#imports relacionados
from PIL import Image
import pytesseract
#metodos internos
import functions.functions as fc

class OCR:

    def __init__(self):
        #altera titulo da pagina
        st.set_page_config(page_title="Python OCR")
        #inicializa variveis
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        #conteudo inicial da pagina
        st.title("OCR JOMBLO EXPERT")
        st.write("Optical Character Recognition (OCR) Coba-coba aja")
        imagem = st.file_uploader("Masukan Image JOMBLO EXPERT", type=["png","jpg"])
        #se selecionar alguma imagem...
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=350)
            st.info("Hasil Ekstraksi JOMBLO EXPERT")
            self.texto = self.extrair_texto(img)
            st.write("{}".format(self.texto))
            
            #Opcao de analisar texto
            self.analisar_texto = st.sidebar.checkbox("Analisar texto")
            if self.analisar_texto==True:
                self.mostrar_analise()
    
    def extrair_texto(self, img):
        #O comando que extrai o texto da imagem
        texto = pytesseract.image_to_string(img, lang="por")
        return texto
    
    def mostrar_analise(self):
        #busca CPF, datas e palavras boas e mas na extracao
        cpf = fc.buscar_cpf(self.texto)
        datas = fc.buscar_data(self.texto)
        p_boas, percentual_bom = fc.buscar_palavras_boas(self.texto)
        p_mas, percentual_mau = fc.buscar_palavras_mas(self.texto)
        
        if cpf==None:
            st.warning("Nenhum CPF encontrado.")
        else:
            cpf = fc.sumarizar_cpf(cpf)
            st.success("CPF encontrado:")
            st.write(cpf)

        if datas==None:
            st.warning("Nenhuma data encontrada.")
        else:
            datas = fc.sumarizar_datas(datas)
            st.success("Datas encontradas:")
            st.write(datas)
        
        if p_boas==0:
            st.warning("N??o identificado palavras de bem.")
        else:
            st.success("Palavras de bem:")
            st.write("{} palavra(s). Representam das palavras do texto: {:.2f}%".format(p_boas, percentual_bom))
        
        if p_mas==0:
            st.warning("N??o identificado palavras m??s.")
        else:
            st.success("Palavras m??s:")
            st.write("{} palavra(s). Representam das palavras do texto: {:.2f}%".format(p_mas, percentual_mau))

ocr = OCR()
ocr.inicial()
