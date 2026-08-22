from extensions import db

class QuestaoRepository:
    def buscar_questoes_por_simulado_procedure(self, simulado_id):
        conn = db()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('sp_buscar_questoes_por_simulado', [simulado_id])
        resultados = []
        for result in cursor.stored_results():
            resultados.extend(result.fetchall())
        cursor.close()
        conn.close()
        return resultados

    def gerar_relatorio_erros_procedure(self, aluno_id):
        conn = db()
        cursor = conn.cursor(dictionary=True)
        cursor.callproc('sp_gerar_relatorio_erros', [aluno_id])
        resultados = []
        for result in cursor.stored_results():
            resultados.extend(result.fetchall())
        cursor.close()
        conn.close()
        return resultados