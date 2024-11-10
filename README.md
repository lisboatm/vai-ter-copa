## Desafio H - **"Vai ter Copa?"**

### Descrição
O Brasil está prestes a sediar a Copa do Mundo e, apesar disso, há muitos protestos em curso. Em diversas redes sociais, circulam rumores de que a Copa não ocorrerá por conta dessas manifestações.

No entanto, a presidente da época assegurou que a Copa acontecerá, e que, caso haja mais reclamações, até duas copas seriam realizadas!

Este desafio consiste em determinar a resposta correta baseada no número de reclamações recebidas.

---

### **Entrada**
O programa deve processar vários casos de teste até o fim do arquivo (EOF). Cada linha da entrada contém um número inteiro `N` que representa a quantidade de reclamações enviadas para a presidente:

- `0 ≤ N ≤ 100`

### **Saída**
Para cada número `N` lido, o programa deve imprimir:

- `"vai ter copa!"` se `N` for igual a 0 (ou seja, não houve reclamações).
- `"vai ter duas!"` se `N` for maior que 0 (ou seja, houve uma ou mais reclamações).

---

### **Exemplos**
#### Entrada
```
0
2
1
100
```

#### Saída
```
vai ter copa!
vai ter duas!
vai ter duas!
vai ter duas!
```

---

### **Explicação**
- Quando `N = 0`, não há reclamações, então a saída é `"vai ter copa!"`.
- Quando `N > 0`, há reclamações, então a saída é `"vai ter duas!"`.

---

### **Implementação em Python**

```python
import sys

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")
```

### **Como o código funciona:**
1. **Leitura da Entrada**: Usamos `sys.stdin` para ler a entrada até o fim do arquivo (EOF).
2. **Processamento**: Para cada linha lida:
   - Convertendo o valor para um número inteiro `n`.
   - Se `n == 0`, imprime `"vai ter copa!"`.
   - Caso contrário, imprime `"vai ter duas!"`.

---

### **Como executar o código**
Para rodar o código em um ambiente que suporte Python (como a plataforma Beecrowd), você pode copiar e colar o código em um arquivo `.py` e executá-lo da seguinte maneira:

```bash
python3 vai_ter_copa.py < input.txt
```

Onde `input.txt` é um arquivo com os dados de entrada.

---

### **Notas Adicionais**
- O uso de `sys.stdin` é essencial para leitura contínua até o fim do arquivo (EOF), o que é necessário em ambientes de competição como o Beecrowd.
- O código é otimizado para funcionar de forma eficiente mesmo para o maior valor permitido (`N = 100`).

Esperamos que esse README ajude a compreender o problema e a solução implementada!
