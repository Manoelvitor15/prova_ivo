import json

def listar_cursos_em_arapiraca_enxuto():
    """
    Lê o JSON e lista cursos únicos em Arapiraca de forma compacta.
    """
    NOME_ARQUIVO = "instituicoes-AL.json"
    CIDADE = "Arapiraca"
    
    try:
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
            data = json.load(f)
            instituicoes = data.get("instituicoes", [])
            
            # --- Lógica de Programação Enxuta (3 Linhas Chave) ---
            
            # 1. Filtra as instituições pela cidade (List Comprehension)
            instituicoes_filtradas = [
                inst for inst in instituicoes 
                if inst.get("endereco", {}).get("municipio") == CIDADE
            ]
            
            # 2. Extrai todos os nomes de cursos de todas as instituições filtradas
            #    (List Comprehension Aninhada)
            lista_cursos_com_duplicatas = [
                curso.get("nome")
                for inst in instituicoes_filtradas
                for curso in inst.get("cursos", [])
            ]
            
            # 3. Usa um SET para obter apenas os cursos únicos e depois ordena a lista final.
            cursos_unicos_ordenados = sorted(list(set(lista_cursos_com_duplicatas)))
            
            # ----------------------------------------------------
            
            # Exibição do resultado
            print(f"--- Cursos Únicos em {CIDADE} ({len(instituicoes_filtradas)} Instituições) ---")
            
            if cursos_unicos_ordenados:
                for i, curso in enumerate(cursos_unicos_ordenados, 1):
                    print(f"  {i}. {curso}")
            else:
                print("Nenhum curso encontrado com base nos dados fornecidos.")
            
    except FileNotFoundError:
        print(f"\nERRO: O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
    except json.JSONDecodeError:
        print(f"\nERRO: O arquivo '{NOME_ARQUIVO}' possui um formato JSON inválido.")
    except Exception as e:
         print(f"\nOcorreu um erro inesperado: {e}")

# Executa a função
listar_cursos_em_arapiraca_enxuto()