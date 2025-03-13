import openpyxl
import pyperclip
import pyautogui
from time import sleep

#Entrar na planilha
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

#Copiar informações de um campo e colar no seu camnpo correspondente
for linha in sheet_produtos.iter_rows(min_row=2, max_row=101):
    
    #NOME DO PRODUTO
    sleep(5)
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1230,305, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #DESCRIÇÃO
    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1228,403, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #CATEGORIA
    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1226,570, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #CÓDIGO DO PRODUTO
    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(1230,670, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #PESO
    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(1225,784, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #DIMENSÕES
    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(1229,892, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #BOTÃO PRÓXIMO
    pyautogui.click(1245,966, duration=1)
    sleep(3)
    
    #PREÇO
    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(1222,326, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #QUANTIDADE EM ESTOQUE
    quantidade_em_estoque = linha[7].value
    pyperclip.copy(quantidade_em_estoque)
    pyautogui.click(1223,443, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #DATA DE VALIDADE
    data_de_validade = linha[8].value
    pyperclip.copy(data_de_validade)
    pyautogui.click(1228,538, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #COR
    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(1232,651, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #TAMANHO
    tamanho = linha[10].value
    
    pyautogui.click(1260,756, duration=1)

    if tamanho == 'Pequenho':
        pyautogui.click(1277,793, duration=1)

    elif tamanho == 'Médio':
        pyautogui.click(1251,835, duration=1)

    elif tamanho == 'Grande':
        pyautogui.click(1238,867, duration=1)
    
    #MATERIAL
    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(1241,860, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #BOTÃO PRÓXIMO
    pyautogui.click(1243,932, duration=1)
    sleep(3)
    
    #FABRICANTE
    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(1249,352, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #PAÍS DE ORIGEM
    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(1232,451, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #OBSERVAÇÕES
    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(1237,564, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #CÓDIGO DE BARRAS
    codigo_de_barras = linha[15].value
    pyperclip.copy(codigo_de_barras)
    pyautogui.click(1234,737, duration=1)
    pyautogui.hotkey('ctrl','v')
    
    #LOCALIZAÇÃO DO ARMAZEM
    localizacao_armazem = linha[16].value
    pyperclip.copy(localizacao_armazem)
    pyautogui.click(1247,838, duration=1)
    pyautogui.hotkey('ctrl','v')
        
    #BOTÃO CONCLUIR
    pyautogui.click(1245,913, duration=1)
    sleep(3)
    #BOTÃO CONFIRMAR INCLUSÃO
    pyautogui.click(1749,218, duration=1)
    sleep(3)
    #INICIAL CADASTRO DE PRODUTO NOVAMENTE
    pyautogui.click(1533,622, duration=1)
    sleep(3)
#Repetir esse processo para outros campos até preencher os campos daquela página 
#Clicar em próxima
#Repetir os mesmos processos e ir para a página seguinte
#Repetir os mesmos processos e finalizar o cadastro daquele prouto e clicar em concluir
#Clicar em "ok", para finalizar o processo
#Clicar no "ok" mais uma vez na mensagem de confirmação de salvamento no banco de dados
#Clicar em "Adicionar mais um e repetir o processo até finalizar a planilha"