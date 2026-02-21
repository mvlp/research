export function formatHttpParams<T = any>(params: { [ key: string ]: any }): T {
  Object.entries(params).forEach((entry) => {
    let key = entry[0];
    let value = entry[1];
    // verifica se o valor do item é um array
    if(Array.isArray(value)) {
      // se o array não tiver nenhum item, ele é removido dos parametros
      if(!value.length) {
        delete params[key];
        return;
      }
      // se o array possuir itens, ele é convertido para uma string no formato "item,item,item"
      params[key] = value.toString();
    };
    // se o valor item for nulo, ele é removido dos parametros
    if(value === null) delete params[key];
  });
  return params as any;
}