CREATE OR REPLACE FUNCTION gerar_grafico_percentual(
    p_capitulo TEXT
)
RETURNS TABLE (
    data_entrega TIMESTAMP,
    pratica_adotada TEXT,
    media NUMERIC,
    limite_inferior NUMERIC,
    limite_superior NUMERIC
)
LANGUAGE sql
AS $$
WITH cnt AS (
    SELECT
        "CNPJ_Companhia",
        date_trunc('quarter', "Data_Entrega") AS data_entrega,
        "ID_Documento",
        "Pratica_Adotada",
        COUNT(*) AS cnt
    FROM cgvn_praticas
    WHERE "Capitulo" = p_capitulo
    GROUP BY
        "CNPJ_Companhia",
        date_trunc('quarter', "Data_Entrega"),
        "ID_Documento",
        "Pratica_Adotada"
),
totais AS (
    SELECT
        data_entrega,
        "ID_Documento",
        SUM(cnt) AS total
    FROM cnt
    GROUP BY
        data_entrega,
        "ID_Documento"
),
freq AS (
    SELECT
        c.data_entrega,
        c."Pratica_Adotada" AS pratica_adotada,
        c.cnt::NUMERIC / t.total AS freq
    FROM cnt c
    JOIN totais t
      ON c.data_entrega = t.data_entrega
     AND c."ID_Documento" = t."ID_Documento"
)
SELECT
    data_entrega,
    pratica_adotada,

    AVG(freq) * 100 AS media,
    percentile_cont(0.05) WITHIN GROUP (ORDER BY freq) * 100 AS limite_inferior,
    percentile_cont(0.95) WITHIN GROUP (ORDER BY freq) * 100 AS limite_superior
FROM freq
GROUP BY
    data_entrega,
    pratica_adotada
ORDER BY
    data_entrega;
$$;
