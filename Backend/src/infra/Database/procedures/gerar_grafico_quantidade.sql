select data_entrega, "Pratica_Adotada", count("ID_Documento") as quantidade 
from(
	select distinct
        "CNPJ_Companhia",
        date_trunc('quarter', "Data_Entrega")::date AS data_entrega,
        "ID_Documento",
        "Pratica_Adotada"
		from cgvn_praticas where "Capitulo" = 'Acionistas' and "Pratica_Adotada" = 'Não'
	)
	group by data_entrega,"Pratica_Adotada" order by data_entrega;