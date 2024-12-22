---
title: "Título del Informe"
author: |
  Román \ \
  \
  \ 
  \
  \
  \ 
  \ 
  \ 
  \ \ \ \ \ \ \
date: |
  Fecha de entrega: \today \
  \
  \
  \
  Cliente: Nombre del cliente o entidad
  \
  \
  \
  \
  \
  \
  Número de Informe: \
  \
  \
  Ubicación: Dirección o localización del proyecto

papersize: a4
fontsize: 10pt
geometry: top=2cm, bottom=2cm, left=2cm, right=2cm, asymmetric
lang: es-ES
# documentclass: book
# classoption: twoside, twocolumn
header-includes:
  - \usepackage{graphicx}
  - \usepackage{float}
  - \usepackage[none]{hyphenat}
  - \usepackage{fancyhdr}
  - \usepackage{caption}
  - \usepackage{subcaption}
  - \usepackage{csquotes}
  - \usepackage{hyperref}
  - \usepackage{pdfcomment}  # Usar pdfcomment en lugar de eforms
  - \hypersetup{pdfborder={0 0 0}, colorlinks=false}
  - \usepackage{amsmath}    # Cargar el paquete amsmath para fórmulas matemáticas
  - \usepackage{hyperref}   # Cargar el paquete para enlaces
  - \hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=blue}  # Configuración de enlaces
toc: true
toc-depth: 4 # Opcional: Profundidad del índice
output: pdf_document
---
# Cálculo de la Transmitancia Térmica (U)

La transmitancia térmica de una fachada típica (también conocida como coeficiente de transferencia de calor o valor U) se puede calcular utilizando la siguiente fórmula general:


$$
U = \frac{1}{R_\text{total}}
$$

Donde $R_\text{total}$ es la resistencia térmica total de la fachada, obtenida como la suma de las resistencias térmicas de todas las capas:

$$
R_\text{total} = R_1 + R_2 + \dots + R_n
$$

Cada resistencia térmica $R$ para una capa se calcula con la fórmula:

$$
R = \frac{e}{\lambda}
$$

Donde:
- $e$: Espesor de la capa (en metros).

- $\lambda$: Conductividad térmica de la capa (en $W/m\cdot K$).

Para las capas donde se proporciona directamente $R$, simplemente se utiliza ese valor.

---

## Capas de la fachada

| Capa                      | $e$ (mm) | $\lambda$ (W/m·K) | $R$ ($m^2\cdot K/W$) |
|---------------------------|------------|----------------------|--------------------------|
| Ladrillo Obra Vista       | 140        | 0.87                | $R = \frac{0.14}{0.87} = 0.161$ |
| Cámara de aire            | 10         | -                   | $R = 0.15$            |
| Poliestireno extruido     | 30         | 0.033               | $R = \frac{0.03}{0.033} = 0.909$ |
| Barrera de vapor          | 10         | 0.19                | $R = \frac{0.01}{0.19} = 0.053$ |
| Ladrillo Perforado        | 40         | 0.87                | $R = \frac{0.04}{0.87} = 0.046$ |
| Mortero                   | 10         | 1.4                 | $R = \frac{0.01}{1.4} = 0.007$  |
| Cerámica                  | 10         | 0.8                 | $R = \frac{0.01}{0.8} = 0.013$  |

---

## Resultado Final

Sumamos todas las resistencias térmicas:

$$
R_\text{total} = 0.161 + 0.15 + 0.909 + 0.053 + 0.046 + 0.007 + 0.013 = 1.338 \, m^2 \cdot K/W
$$

Finalmente, calculamos la transmitancia térmica:

$$
U = \frac{1}{R_\text{total}} = \frac{1}{1.338} = 0.747 \, W/m^2\cdot K
$$

Por lo tanto, la transmitancia térmica de la fachada es:

$$
U = 0.747 \, W/m^2\cdot K
$$
