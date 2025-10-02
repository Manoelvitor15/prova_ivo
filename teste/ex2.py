import json
import csv

with open('instituicoes-AL.json', 'r', encoding='utf-8') as f:
    info = json.load(f)
    instituicoes = info.get("instituicoes", [])

# cria/abre arquivo CSV
with open('cursos_instituicoes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    
    # cabeçalho
    writer.writerow(["CNPJ", "Código Escola", "Nome Curso", "Modalidade", "Cidade"])
    
    for instituicao in instituicoes:
        cnpj = instituicao.get("cnpj", "")
        cod_escola = instituicao.get("codEscola", "")
        cidade = instituicao.get("municipio", "")
        
        cursos = instituicao.get("cursos", [])
        for curso in cursos:
            nome_curso = curso.get("nome", "")
            modalidade = curso.get("modalidade", "")
            writer.writerow([cnpj, cod_escola, nome_curso, modalidade, cidade])

print("Arquivo 'cursos_instituicoes.csv' gerado com sucesso!")
