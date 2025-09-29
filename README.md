# Academic Personal Website

Este repositório contém um template completo para criação de uma página pessoal acadêmica, ideal para docentes e pesquisadores que desejam divulgar suas pesquisas, publicações, participações em eventos e repositórios do GitHub.

## 🌟 Características

- **Design Responsivo**: Otimizado para desktop, tablet e dispositivos móveis
- **Seções Organizadas**: 
  - Perfil pessoal e apresentação
  - Pesquisas em andamento
  - Publicações acadêmicas
  - Eventos e participações
  - Repositórios GitHub
  - Informações de contato
- **Carregamento Dinâmico**: Conteúdo carregado a partir de arquivos JSON
- **Animações Suaves**: Transições e efeitos visuais elegantes
- **SEO Otimizado**: Estrutura HTML semântica

## 🚀 Como Usar

### 1. Personalização Básica

Edite o arquivo `index.html` para personalizar:
- Nome do docente
- Título/posição
- Descrição pessoal
- Links de contato

### 2. Adicionando Sua Foto

Substitua o arquivo `images/profile.jpg` pela sua foto pessoal (recomendado: 400x400px).

### 3. Configurando o Conteúdo

Edite os arquivos JSON na pasta `data/` para adicionar seu conteúdo:

#### `data/research.json`
```json
[
  {
    "title": "Título da Pesquisa",
    "description": "Descrição detalhada da pesquisa...",
    "tags": ["tag1", "tag2", "tag3"]
  }
]
```

#### `data/publications.json`
```json
[
  {
    "title": "Título do Artigo",
    "authors": "Autores",
    "venue": "Revista/Conferência",
    "year": "2024",
    "links": [
      { "text": "PDF", "url": "link", "icon": "fas fa-file-pdf" }
    ]
  }
]
```

#### `data/events.json`
```json
[
  {
    "date": "Data do Evento",
    "title": "Nome do Evento",
    "location": "Local",
    "description": "Descrição da participação..."
  }
]
```

#### `data/repositories.json`
```json
[
  {
    "name": "nome-do-repositorio",
    "description": "Descrição do projeto",
    "url": "https://github.com/username/repo",
    "language": "Python",
    "stars": "10",
    "forks": "2"
  }
]
```

### 4. Integração com GitHub

Para carregar automaticamente seus repositórios do GitHub, edite o arquivo `js/main.js` e adicione seu username:

```javascript
// Substitua 'seu-username' pelo seu username do GitHub
loadGitHubRepositories('seu-username');
```

## 🎨 Personalização Avançada

### Cores e Estilo

Edite o arquivo `css/style.css` para personalizar:
- Cores primárias e secundárias
- Fontes
- Espaçamentos
- Animações

### Adicionando Novas Seções

1. Adicione a seção no HTML
2. Crie o CSS correspondente
3. Implemente a lógica JavaScript se necessário

## 📱 Responsividade

O template é totalmente responsivo e funciona bem em:
- Desktop (1200px+)
- Tablets (768px - 1199px)
- Smartphones (até 767px)

## 🌐 Deployment

### GitHub Pages

1. Faça commit de todas as alterações
2. Vá em Settings > Pages
3. Selecione a branch `main` como source
4. Sua página estará disponível em `https://username.github.io/repository-name`

### Netlify

1. Conecte seu repositório ao Netlify
2. Configure o build (não necessário para este projeto)
3. Sua página será deployada automaticamente

### Outros Provedores

Este é um site estático simples que pode ser hospedado em qualquer provedor que suporte HTML/CSS/JS.

## 🔧 Desenvolvimento Local

Para testar localmente:

```bash
# Servir os arquivos localmente (Python)
python -m http.server 8000

# Ou usando Node.js
npx serve .

# Ou usando PHP
php -S localhost:8000
```

Acesse `http://localhost:8000` no seu navegador.

## 📚 Tecnologias Utilizadas

- **HTML5**: Estrutura semântica
- **CSS3**: Estilos e animações
- **JavaScript (ES6+)**: Funcionalidades dinâmicas
- **Font Awesome**: Ícones
- **Google Fonts**: Tipografia (opcional)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ✨ Exemplos

Confira alguns exemplos de sites criados com este template:
- [Exemplo 1](#) - Professor de Ciência da Computação
- [Exemplo 2](#) - Pesquisadora em IA
- [Exemplo 3](#) - Docente de Engenharia

## 📞 Suporte

Se precisar de ajuda:
1. Consulte a documentação acima
2. Verifique as [Issues do GitHub](../../issues)
3. Crie uma nova issue se necessário

---

Desenvolvido com ❤️ para a comunidade acadêmica brasileira.