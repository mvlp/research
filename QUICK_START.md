# Guia de Início Rápido - Website Acadêmico

Este guia irá ajudá-lo a configurar rapidamente sua página pessoal acadêmica.

## ⚡ Primeiros Passos (5 minutos)

### 1. Personalize suas informações básicas

Edite o arquivo `index.html` e substitua:
- `Dr. Nome do Docente` pelo seu nome
- `Professor(a) e Pesquisador(a)` pelo seu título
- A descrição na seção hero
- Links de contato na seção de contato

### 2. Adicione sua foto

- Coloque sua foto em `images/profile.jpg`
- Recomendado: 400x400px, formato JPG ou PNG

### 3. Configure seu conteúdo

Edite os arquivos na pasta `data/`:

**Pesquisas** (`data/research.json`):
```json
{
  "title": "Sua Pesquisa",
  "description": "Descrição da pesquisa...",
  "tags": ["tag1", "tag2"]
}
```

**Publicações** (`data/publications.json`):
```json
{
  "title": "Título do Artigo",
  "authors": "Seus Autores",
  "venue": "Revista/Conferência",
  "year": "2024",
  "links": [{"text": "PDF", "url": "seu-link", "icon": "fas fa-file-pdf"}]
}
```

### 4. Deploy no GitHub Pages

1. Vá em **Settings** > **Pages**
2. Selecione **Deploy from branch**
3. Escolha **main** branch
4. Clique **Save**
5. Sua página estará em: `https://seu-usuario.github.io/research`

## 🎨 Personalização Avançada

### Cores e Tema

Edite `css/style.css` nas variáveis CSS:
```css
:root {
  --primary-color: #3498db;
  --secondary-color: #2c3e50;
  --accent-color: #667eea;
}
```

### Configuração Completa

Use o arquivo `config.json` para configurações avançadas:
- Informações pessoais
- Links de redes sociais
- Cores do tema
- Integração com GitHub

### Integração Automática com GitHub

No arquivo `js/main.js`, substitua:
```javascript
// Linha aproximada 280
loadGitHubRepositories('seu-username-github');
```

## 📱 Testando Localmente

```bash
# Python
python -m http.server 8000

# Node.js
npx serve .

# Acesse: http://localhost:8000
```

## ❓ Problemas Comuns

**Foto não aparece?**
- Verifique se o arquivo está em `images/profile.jpg`
- Confirme que o nome do arquivo está correto

**JSON não carrega?**
- Verifique a sintaxe dos arquivos JSON
- Use um validador JSON online se necessário

**Site não funciona no GitHub Pages?**
- Aguarde alguns minutos para propagação
- Verifique se a branch está correta nas configurações

## 🆘 Suporte

- Consulte o [README completo](README.md)
- Abra uma [issue no GitHub](../../issues)
- Verifique os [exemplos de configuração](data/)

---

✨ **Dica**: Comece com pequenas alterações e teste localmente antes de fazer o deploy!