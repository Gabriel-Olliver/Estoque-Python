# Sistema de estoque

Sistema de controle de estoque simples, feito em Python e executado direto no terminal. O usuário cadastra um produto com a quantidade inicial e depois adiciona, retira ou consulta o estoque por meio de um menu interativo.

# Funcionalidades

- Cadastro de um produto com quantidade inicial
- Adicionar produtos ao estoque
- Retirar produtos do estoque, com bloqueio quando a quantidade pedida é maior que a disponível
- Consultar a quantidade atual em estoque
- Validação das entradas:
  - impede texto no lugar de números
  - impede quantidades negativas ou iguais a zero nas movimentações
- Menu em loop, que só encerra quando o usuário escolhe sair

# Tecnologias

- Python 3.8 ou superior (nenhuma biblioteca externa)

# Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
   cd NOME-DO-REPOSITORIO
   

2. Execute o programa:

   ```bash
   python estoque.py
   

   > Dependendo do sistema, o comando pode ser `python3 estoque.py`.

# Exemplo de uso

------ Estoque Olliver ------
Digite o nome do produto: Arroz
Digite a quantidade do produto: 10

------ Menu do Estoque ------
(1) Adicionar produtos
(2) Retirar produtos
(3) Consultar estoque
(4) Sair do programa

Digite uma opção: 1
Digite a quantidade: 5

Estoque atualizado de Arroz: 15

Digite uma opção: 2
Digite a quantidade: 20

Estoque insuficiente!

Digite uma opção: 3

Estoque atual de Arroz: 15

Digite uma opção: 4
Saindo do estoque...


# Menu

| Opção | Ação                | Descrição                                           |
|-------|---------------------|-----------------------------------------------------|
| 1     | Adicionar produtos  | Soma a quantidade informada ao estoque              |
| 2     | Retirar produtos    | Subtrai a quantidade, se houver estoque suficiente  |
| 3     | Consultar estoque   | Mostra a quantidade atual do produto                |
| 4     | Sair do programa    | Encerra a execução                                  |

# O que pratiquei neste projeto

- Entrada e saída de dados com `input()` e `print()`
- Conversão de tipos (`int`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while True`, `break`, `continue`)
- Tratamento de erros com `try/except`
- Formatação de texto com f-strings

# Próximos passos

- Suporte a vários produtos usando dicionário
- Listar todos os produtos do estoque
- Salvar os dados em arquivo (CSV ou JSON)
- Versão em Java com classes `Produto` e `Estoque`

# Autor

**Gabriel Oliveira**
Estudante de Análise e Desenvolvimento de Sistemas, em busca de uma carreira como desenvolvedor back-end.

- GitHub: [@SEU-USUARIO](https://github.com/SEU-USUARIO)
