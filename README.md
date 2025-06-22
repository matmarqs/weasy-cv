# WeasyCV - Gerador de Currículo em PDF

Gerador minimalista de currículos em PDF a partir de arquivos JSON, utilizando Jinja2 para templates e WeasyPrint para renderização.

## 📦 Instalação

```bash
git clone https://github.com/matmarqs/weasy-cv  # Clonar repositório
python -m venv .venv  # Criar ambiente virtual
source .venv/bin/activate  # Ativar ambiente virtual (Linux/Mac)
# .venv\Scripts\activate  # Para Windows
pip install -r requirements.txt
```

## ▶️ Como Usar

```bash
python main.py -j <arquivo_json> [-o <output.pdf>]
```

Exemplo:
```bash
python main.py -j data/curriculo.json -o meu_curriculo.pdf
```

## ✨ Funcionalidades

- **Modular**: Estrutura do currículo definida em JSON
- **Templates**: Utiliza Jinja2 para renderização HTML
- **PDF de Qualidade**: WeasyPrint gera PDFs profissionais
- **Live Preview**: Watchdog monitora e regenera automaticamente
- **Ícones**: Integração com Font Awesome (créditos abaixo)

## 🛠️ Tecnologias

- **WeasyPrint**: Conversão de HTML para PDF
- **Jinja2**: Engine de templates
- **Watchdog**: Monitoramento de arquivos em tempo real
- **Font Awesome**: Ícones profissionais (Free v6.4.0)

## 📝 Créditos

Ícones por [Font Awesome](https://fontawesome.com/) (Free v6.4.0) - Licença CC BY 4.0

## 📄 Licença

MIT License - Consulte o arquivo LICENSE para mais detalhes
