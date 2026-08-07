DELIMITER //
CREATE PROCEDURE sp_buscar_alunos_por_nome(IN p_nome VARCHAR(100))
BEGIN
    SELECT id, nome, matricula 
    FROM alunos 
    WHERE nome LIKE CONCAT('%', p_nome, '%')
    ORDER BY nome ASC;
END //
DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_buscar_questoes_por_simulado(IN p_simulado_id INT)
BEGIN
    SELECT q.id, q.enunciado, q.alternativa_correta
    FROM questao q
    INNER JOIN simulado_questao sq ON q.id = sq.questao_id
    WHERE sq.simulado_id = p_simulado_id
    ORDER BY q.id ASC;
END //

CREATE PROCEDURE sp_gerar_relatorio_erros(IN p_aluno_id INT)
BEGIN
    SELECT q.id, q.enunciado, q.alternativa_correta, q.alternativa_marcada
    FROM questao q
    INNER JOIN mapa_erro_questao meq ON q.id = meq.questao_id
    INNER JOIN mapa_erro me ON me.id = meq.mapa_erro_id
    WHERE me.aluno_id = p_aluno_id AND q.alternativa_correta <> q.alternativa_marcada;
END //

DELIMITER ;