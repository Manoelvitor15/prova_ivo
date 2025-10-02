import json

with open('instituicoes-AL.json', 'r', encoding='utf-8') as f:
    info = json.load(f)
    instituicoes = info.get("instituicoes", [])
    total_cursos = 0
    presencial_count = 0
    ead_count = 0

    for instituicao in instituicoes:
        cursos = instituicao.get("cursos", [])
        for curso in cursos:
            total_cursos += 1
            modalidade = str(curso.get("modalidade", "")).strip().upper()

            if "PRESENCIAL" in modalidade:
                presencial_count += 1
            elif "EAD" in modalidade or "A DISTÂNCIA" in modalidade:
                ead_count += 1

    if total_cursos > 0:
        percentual_presencial = (presencial_count / total_cursos) * 100
        percentual_ead = (ead_count / total_cursos) * 100

        print(f"Total de cursos: {total_cursos}")
        print(f"Cursos presenciais: {presencial_count} ({percentual_presencial:.2f}%)")
        print(f"Cursos EAD: {ead_count} ({percentual_ead:.2f}%)")
    else:
        print("Não há cursos para calcular percentuais.")
