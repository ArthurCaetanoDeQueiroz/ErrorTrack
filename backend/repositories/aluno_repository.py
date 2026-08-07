from database.connection import get_db_connection

class AlunoRepository:
    def buscar_por_nome_procedure(self, nome):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.callproc('sp_buscar_alunos_por_nome', [nome])
        
        resultados = []
        for result in cursor.stored_results():
            resultados.extend(result.fetchall())
            
        cursor.close()
        conn.close()
        return resultados