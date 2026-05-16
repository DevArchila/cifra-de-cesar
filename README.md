# 🔐 Cifra de César — Criptografia Clássica

Implementação em Python da Cifra de César, uma das técnicas de criptografia mais antigas da história, que consiste em deslocar cada letra do texto por um número fixo de posições no alfabeto.

---

# Descrição

O programa recebe uma string e uma chave numérica, e retorna o texto cifrado com cada letra deslocada pela quantidade de posições definida pela chave. Caracteres especiais, espaços e números são mantidos sem alteração.

---

# Funcionalidades

- Cifração de texto com chave definida pelo usuário
- Suporte a letras maiúsculas e minúsculas
- Preservação de espaços, números e caracteres especiais
- Mapeamento de letras por dicionários para deslocamento preciso
- Tratamento de borda: chaves que ultrapassam o limite do alfabeto são tratadas com módulo

---

# Como executar

**Pré-requisito:** Python 3.x instalado.

```bash
python cifra_de_cesar.py
```

---

# Exemplo de uso

```
---CIFRA DE CESAR---

digite a string: Samuel
digite a chave: 3

String: vdpxho
Chave: 3
```

> A letra **S** deslocada 3 posições → **V**, a letra **a** → **d**, e assim por diante.

---

# Como funciona

A cifra mapeia cada letra para um valor numérico (a=1, b=2, ..., z=26), soma a chave e converte de volta para letra usando módulo 26 para garantir que o alfabeto seja "circular" — ou seja, após o **z** volta para o **a**.

```
letra → valor numérico → valor + chave → % 26 → nova letra
```

---

# Conceitos praticados

- Funções com parâmetros
- Dicionários (`dict`) e `zip()` para mapeamento bidirecional
- Iteração com `enumerate()`
- Operador módulo (`%`) para lógica circular
- List comprehension implícita com `append()`
- Manipulação de strings

---

# Contexto histórico

A Cifra de César foi utilizada pelo imperador romano Júlio César para proteger comunicações militares, geralmente com deslocamento de 3 posições. É considerada um dos primeiros exemplos documentados de criptografia na história.

---

# 👤 Autor

**Samuel Archila**  
Estudante de Data Science | Python | SQL | Power BI  
[LinkedIn](https://www.linkedin.com/in/samuelarchila)
