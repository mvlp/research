CREATE OR REPLACE FUNCTION gerar_grafico_quantidade(
    p_capitulo TEXT
)
RETURNS TABLE (
    data_entrega DATE,
    pratica_adotada TEXT,
    quantidade BIGINT
)
LANGUAGE sql
AS $$
WITH base AS (
    SELECT
        "CNPJ_Companhia",
        date_trunc('month', "Data_Entrega")::date AS data_entrega,
        "ID_Documento",
        "Pratica_Adotada"
    FROM cgvn_praticas
    WHERE "Capitulo" = p_capitulo
    GROUP BY
        "CNPJ_Companhia",
        date_trunc('month', "Data_Entrega"),
        "ID_Documento",
        "Pratica_Adotada"
)
SELECT
    data_entrega,
    "Pratica_Adotada",
    COUNT("ID_Documento") AS quantidade
FROM base
GROUP BY
    data_entrega,
    "Pratica_Adotada"
ORDER BY
    data_entrega;
$$;
