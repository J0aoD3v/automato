# Autômato Finito Determinístico (AFD) - Ferramenta de Processamento 🤖🔌🧠🔧🏭

Esta ferramenta permite a execução de um Autômato Finito Determinístico (AFD) em um conjunto de entradas e geração de resultados no arquivo de saída.

## Uso

### Pré-requisitos

- Python 3.x
- Bibliotecas Python: `tqdm`

> Se você não tiver a biblioteca `tqdm` instalada, siga estas instruções:
>
> Certifique-se de ter o `pip` instalado e configurado corretamente em seu sistema antes de executar o comando de instalação. Se estiver usando um ambiente virtual, lembre-se de ativá-lo antes de executar o comando.
>
> 1. Abra um terminal ou prompt de comando.
> 2. Execute o seguinte comando para instalar a biblioteca tqdm:
> 
>    ```
>    pip install tqdm
>    ```
>    
> 3. Aguarde enquanto o `pip` baixa e instala a biblioteca.
> 
> 4. Uma vez concluída a instalação, você poderá executar a ferramenta sem problemas.


### Arquivos

1. `main.py`: O script principal para executar o processamento do AFD nas entradas e gerar os resultados.
2. `gen.py`: Um script auxiliar para gerar exemplos de arquivo de entrada.
3. Arquivo de Autômato (JSON): Arquivo JSON que define a estrutura do AFD, incluindo estados, transições e estados finais.
4. Arquivo de Entrada: Arquivo CSV contendo as palavras a serem processadas pelo AFD. Cada linha contém uma palavra seguida por um valor esperado.

### Execução

1. Certifique-se de que os pré-requisitos estejam instalados.

2. Execute o script principal com o seguinte comando:

```python
python main.py <arquivo_automato> <arquivo_entrada>
```

Substitua `<arquivo_automato>` pelo caminho para o arquivo JSON que define o autômato e `<arquivo_entrada>` pelo caminho para o arquivo CSV de entrada.

3. Aguarde o processamento das entradas. O progresso será exibido em uma barra de progresso.

4. O arquivo de saída `output.out` será gerado. Cada linha contém uma palavra processada, o valor esperado, o valor obtido e o tempo de processamento.

## Estratégias e Técnicas

- **Leitura Eficiente do Arquivo de Entrada em Lotes:** O arquivo de entrada é lido em lotes para otimizar o desempenho.
- **Uso de Dicionário de Transições:** Um dicionário é utilizado para otimizar a busca de transições no autômato.
- **Processamento Paralelo:** O processamento de lotes é realizado em paralelo para aproveitar melhor os recursos da CPU.
- **Atraso de Processamento:** Um pequeno atraso é introduzido a cada caractere processado para simular o processamento real.

## Problema com a Exibição do Tempo no Arquivo de Saída

Devido a restrições de precisão de tempo em sistemas operacionais e linguagens de programação, pode ser desafiador exibir tempos de processamento extremamente curtos, como na ordem de nanossegundos. No entanto, o tempo de processamento é registrado internamente e pode ser usado para fins de medição relativa.

## Exemplo de Geração de Arquivo de Entrada

Para gerar um arquivo de entrada de exemplo, você pode usar o script `gen.py`. Execute o script com o seguinte comando:

```python
python gen.py <quantidade_de_palavras> > exemplo_entrada.csv
```

Substitua `<quantidade_de_palavras>` pelo número desejado de palavras no arquivo de entrada.

---

Este projeto foi desenvolvido como parte da disciplina de Teoria da Computação na UENP. Sinta-se à vontade para contribuir, reportar problemas ou fornecer sugestões.