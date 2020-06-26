SELECT json_agg(lis) FROM (SELECT par.nome, par.curso1_id AS curso_id, cur.nome, par.data_inscricao_c1 AS data_inscricao
FROM sisins_participante AS par JOIN sisins_curso AS cur ON par.curso1_id = cur.id 
WHERE (par.curso1_id = 1 AND par.resultado_c1 = 1)
UNION
SELECT par.nome, par.curso2_id AS curso_id, cur.nome, par.data_inscricao_c2 AS data_inscricao
FROM sisins_participante AS par JOIN sisins_curso AS cur ON par.curso2_id = cur.id 
WHERE (par.curso2_id = 1 AND par.resultado_c2 = 1)) AS lis

SELECT par.nome, par.curso1_id AS curso_id, cur.nome, par.data_inscricao_c1 AS data_inscricao, CURRENT_TIMESTAMP AS data_cert FROM sisins_participante AS par JOIN sisins_curso AS cur ON par.curso1_id = cur.id  WHERE (par.curso1_id = 1 AND par.resultado_c1 = 1) UNION SELECT par.nome, par.curso2_id AS curso_id, cur.nome, par.data_inscricao_c2 AS data_inscricao, CURRENT_TIMESTAMP AS data_cert FROM sisins_participante AS par JOIN sisins_curso AS cur ON par.curso2_id = cur.id  WHERE (par.curso2_id = 1 AND par.resultado_c2 = 1)