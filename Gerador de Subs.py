# Projetos-Públicos

import docxtpl

def gerar_documento(modelo_arquivo, dados, nome_saída):
    doc = docxtpl.DocxTemplate(modelo_arquivo)
    doc.render(dados)  
    doc.save(nome_saída)

dados = {
    "Escritorio": "Exemplo de Escritório",
    "Endereco_Escritorio": "Exemplo de Endereço",
    "adv_nome_1": "Advogado 1",
    "adv_oab_1": "OAB do Advogado 1",
    "CPF_1": "CPF do Advogado 1",

    #CASO TENHA MAIS DE UM ADVOGADO, PREENCHA OS CAMPOS ABAIXO
    
    "Texto_Padrao_1": "", #utilizar esse para caso tenha mais de um "brasileiro, casado, advogado, inscrito no CPF/MF sob o nº"
    "Texto_Padrao_2": "", #utilizar esse para caso tenha mais de um "e na OAB/SP sob o nº"  
    
    "adv_nome_2": "",
    "adv_oab_2": "",
    "CPF_2": "",

    "adv_nome_3": "",
    "adv_oab_3": "",
    "CPF_3": "",
    
    "adv_nome_4": "",
    "adv_oab_4": "",
    "CPF_4": "",
    
    "adv_nome_5": "",
    "adv_oab_5": "",
    "CPF_5": "",
    
    "adv_nome_6": "",
    "adv_oab_6": "",
    "CPF_6": "",
    
    "adv_nome_7": "",
    "adv_oab_7": "",
    "CPF_7": "",
    
    "adv_nome_8": "",
    "adv_oab_8": "",
    "CPF_8": "",
    
    "adv_nome_9": "",
    "adv_oab_9": "",
    "CPF_9": "",
    
    "adv_nome_10": "",
    "adv_oab_10": "",
    "CPF_10": "",
    
    #CASO TENHA MAIS DE UM ADVOGADO, PREENCHA OS CAMPOS ACIMA
    #Também pode adicionar campos para caso tenha mais advogados, porém tem que fazer a mesma coisa no modelo da pasta

    "cidade_1": "São Paulo",
    "processo": "1234567-89.2023.8.26.0100",
    "Contra_Parte_Processo": "ARTESP",
    "Unidade": "Ecovias dos Imigrantes",
    "Vara_Comarca": "9ª Vara Cível do Foro de São Bernardo do Campo/SP",
    "Cidade": "São Bernardo do Campo",
    "Data": "21 de agosto de 2025"
}
modelo = "substabelecimento_modelo.docx"
saída = "substabelecimento_gerado.docx"

gerar_documento(modelo, dados, saída)
