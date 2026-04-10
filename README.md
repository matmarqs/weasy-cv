# WeasyCV - Gerador de Currículo em PDF

Gerador minimalista de currículos em PDF a partir de arquivos JSON, utilizando Jinja2 para templates HTML e WeasyPrint para renderização.

## Instalação

```bash
git clone https://github.com/matmarqs/weasy-cv  # Clonar repositório
python -m venv .venv                            # Criar ambiente virtual
source .venv/bin/activate                       # Ativar ambiente virtual (Linux/Mac)
# .venv\Scripts\activate                        # Para Windows
pip install -r requirements.txt                 # Instalar dependências
```

## Como Usar

```bash
python weasy-cv.py -j <arquivo_json> [-o <output.pdf>]
```

Exemplo:
```bash
python weasy-cv.py -j data/cyber_br.json
```

## Funcionalidades

- **JSON**: Estrutura do currículo definida em JSON
- **Templates**: Utiliza Jinja2 para renderização HTML
- **PDF de Qualidade**: WeasyPrint gera PDFs profissionais
- **Live Preview**: Watchdog monitora e regenera automaticamente
- **Ícones**: Integração com Font Awesome.

## Créditos

Ícones por [Font Awesome](https://fontawesome.com/) (Free v6.4.0) - Licença CC BY 4.0

## Licença

GPL-3.0 LICENSE - Consulte o arquivo LICENSE para mais detalhes
