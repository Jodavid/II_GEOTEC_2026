# Padrões Espaciais das Denúncias do Disque 100 no Nordeste Brasileiro em 2024

[![Event: II GEOTEC 2026](https://img.shields.io/badge/II_GEOTEC-2026_IFPB_Jo%C3%A3o_Pessoa-05437a?style=flat-square)](https://www.even3.com.br/ii-geotec-encontro-de-geotecnologias-776649/)
[![Made with Quarto](https://img.shields.io/badge/Made%20with-Quarto-447099?style=flat-square&logo=quarto&logoColor=white)](https://quarto.org/)
[![Format: Reveal.js](https://img.shields.io/badge/Format-Reveal.js-e74c3c?style=flat-square)](https://revealjs.com/)
[![Slides: 61 Slides](https://img.shields.io/badge/Slides-61_Slides-27ae60?style=flat-square)](#)

Apresentação oral / palestra de 50 minutos preparada para o **II GEOTEC — Encontro de Geotecnologias**, realizado no Instituto Federal da Paraíba (**IFPB — Campus João Pessoa**) de 10 a 12 de novembro de 2026.

---

## 👥 Autor e Apresentador

- **Prof. Dr. Jodavid de Araújo Ferreira**  
  Departamento de Estatística — Universidade Federal de Pernambuco (UFPE)  
  📧 [jodavid.ferreira@ufpe.br](mailto:jodavid.ferreira@ufpe.br) | 🌐 [jodavid.github.io](https://jodavid.github.io) | 🐙 [github.com/jodavid](https://github.com/jodavid)

---

## 📌 Histórico da Pesquisa

Esta pesquisa consolida investigações em Estatística Espacial e Direitos Humanos que tiveram versões preliminares e metodológicas apresentadas e debatidas em fóruns especializados:
1. **III WDCD** (*III Workshop de Divulgação Científica e Didáticas*): Discussão sobre a democratização, transparência e divulgação de dados públicos de violência.
2. **XIX EMR | V EPE** (*XIX Escola de Modelos de Regressão & V Encontro Paraibano de Estatística*): Aprofundamento da modelagem estocástica, formulação do Estimador Bayesiano Empírico e testes de varredura espacial.
3. **II GEOTEC (2026)**: Apresentação da esteira integrada de **Geotecnologias, Análise Espacial de Áreas e Tomada de Decisão em Políticas Públicas**.

---

## 🛰️ Visão Geral do Trabalho

As violações de direitos humanos constituem uma grave crise social e de saúde pública no Brasil. Segundo o 18º Anuário Brasileiro de Segurança Pública (2024), a Região Nordeste abriga 2 dos 3 estados com maiores taxas de Mortes Violentas Intencionais (Bahia e Pernambuco) e 7 dos 10 municípios mais violentos do país.

Este trabalho investiga a distribuição territorial das **110.278 denúncias registradas pelo Disque 100 (Disque Direitos Humanos / MDHC)** ao longo do ano de 2024 nos **1.793 municípios da Região Nordeste**, integrando dados demográficos do IBGE (SIDRA 2024) através de quatro abordagens estatístico-espaciais complementares:

1. **Razão de Incidência Espacial (RIE):** Mapeamento empírico do risco relativo local frente à média macroeconômica regional.
2. **Autocorrelação Espacial Global e Local (Moran & LISA):** Diagnóstico de dependência espacial com matriz de contiguidade Rainha (*Queen*), identificando 51 hotspots (Alto-Alto), 9 coldspots (Baixo-Baixo) e 219 outliers espaciais.
3. **Estimador Bayesiano Empírico Local (EBEL - Marshall, 1991):** Suavização de taxas sob modelo Poisson-Gama com fator de encolhimento (*shrinkage*) para neutralizar a instabilidade estatística do problema de pequenas áreas.
4. **Estatística de Varredura Scan Espacial (Kulldorff & Nagarwalla, 1995):** Identificação de conglomerados com excesso de risco via janelas circulares flexíveis e simulações de Monte Carlo ($p < 0,05$).

---

## 📊 Principais Resultados

- **Perfil dos Atores:**
  - **85,22%** das denúncias são efetuadas por **terceiros** (apenas ~15% pela própria vítima).
  - **90,86%** das notificações chegam via **ligação telefônica tradicional**.
  - **Vulnerabilidade Extrema:** Crianças e adolescentes (0 a 17 anos) somam **46,74%** das vítimas; idosos (60+ anos) somam **33,80%** (juntos superam **80% do total**).
  - **O Lar como Epicentro:** Quase **80%** das agressões ocorrem no ambiente domiciliar (48,90% em casa compartilhada e 30,43% na casa da vítima).
- **Diagnóstico Espacial:**
  - Autocorrelação global positiva confirmada: **$I = 0,12$ ($p < 0,01$)**.
  - O caso de **Salgadinho (PB)** ilustra o desafio das pequenas populações: RIE empírica de 12,9 e taxa bayesiana suavizada de 24,27 por mil habitantes.
- **Triangulação e Convergência Multi-Método:**
  - A interseção tríplice ($\text{RIE} > 2$ $\cap$ $\text{Bayes} > 2$ $\cap$ $\text{Scan Sig.}$) identificou **49 municípios críticos prioritários**.
  - Desses, **6 grandes centros metropolitanos** possuem população superior ao teto do Scan (57.112 hab.), apresentando risco crítico autônomo: **Recife (PE), Natal (RN), Parnaíba (PI), Casa Nova (BA), Ceará-Mirim (RN) e Extremoz (RN)**.

---

## 📁 Estrutura do Diretório

```text
Slide/
├── index.qmd                      # Código-fonte da apresentação em Quarto (Reveal.js)
├── index.html                     # Apresentação interativa compilada (61 slides)
├── Apresentacao_GEOTEC_2026.pdf   # Versão completa em PDF (impressão/distribuição)
├── css/
│   ├── geotec.css                 # Estilos customizados para o II GEOTEC 2026
│   ├── sinape.css                 # Estilo base da identidade visual
│   └── jodavid.css                # Classes utilitárias auxiliares
├── images/
│   ├── banner_geotec.jpeg         # Banner oficial do II GEOTEC (IFPB)
│   ├── mapa_nordeste_estudo.png   # Mapa regional com os 9 estados e polos críticos
│   ├── metodologia_fluxograma.png # Fluxograma da esteira analítica integrada
│   ├── disque100_temporal.png     # Curvas horárias e semanais de atendimento
│   ├── disque100_perfil_social.png# Painel demográfico de vítimas, agressores e canais
│   ├── moran_scatterplot_diagram.png # Diagrama explicativo do Moran Scatterplot
│   ├── bayes_shrinkage_diagram.png# Efeito de encolhimento bayesiano (shrinkage)
│   ├── scan_statistic_diagram.png # Esquema da janela circular de Kulldorff
│   ├── triangulacao_convergencia.png # Diagrama de Venn da convergência dos métodos
│   ├── mapa_moran_lisa_nordeste.png # Cartografia dos clusters LISA
│   ├── mapa_rie_bayes_comparativo.png # Comparação cartográfica RIE vs. Bayes
│   ├── mapa_scan_clusters_nordeste.png # Cartografia dos clusters da varredura Scan
│   └── logo_ufpe_facepe.png       # Logomarcas institucionais de apoio
└── README.md                      # Esta documentação
```

---

## 🖥️ Como Executar e Visualizar

### 1. Visualização Direta
Abra o arquivo `Slide/index.html` em qualquer navegador web moderno:
```bash
xdg-open Slide/index.html
```

### 2. Teclas de Navegação (Reveal.js)
- `Espaço` ou `Seta Direita`: Avançar slide.
- `Seta Esquerda`: Voltar slide.
- `F`: Modo tela cheia (*full screen*).
- `O`: Visão geral de todos os slides (*overview/slides matrix*).
- `S`: Modo de visualização do apresentador (*speaker notes* e cronômetro).
- `?`: Ajuda de atalhos.

### 3. Recompilação com Quarto
Caso queira modificar o conteúdo ou os estilos:
```bash
quarto render Slide/index.qmd
```
