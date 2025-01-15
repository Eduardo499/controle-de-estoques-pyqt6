<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Controle de Estoques</title>
</head>
<body>
    <h1>Controle de Estoques</h1>
    <p>Este é um projeto de controle de estoques desenvolvido em Python utilizando PyQt6 para a interface gráfica e SQLite para o banco de dados.</p>

    <h2>Requisitos</h2>
    <ul>
        <li>Python 3.10 ou superior</li>
        <li>PyQt6</li>
        <li>python-dotenv</li>
    </ul>

    <h2>Instalação</h2>
    <ol>
        <li>Clone o repositório:
            <pre><code>git clone https://github.com/seu-usuario/controle_estoques.git
cd controle_estoques</code></pre>
        </li>
        <li>Crie um ambiente virtual e ative-o:
            <pre><code>python -m venv venv
source venv/bin/activate  <!-- No Windows, use `venv\Scripts\activate` --></code></pre>
        </li>
        <li>Instale as dependências:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2>Uso</h2>
    <ol>
        <li>Execute o aplicativo:
            <pre><code>python src/main.py</code></pre>
        </li>
        <li>A interface gráfica será aberta, permitindo que você adicione, visualize e gerencie os produtos no estoque.</li>
    </ol>

    <h2>Estrutura do Projeto</h2>
    <ul>
        <li><code>src/</code>: Contém o código-fonte do projeto.
            <ul>
                <li><code>gui/</code>: Contém os arquivos relacionados à interface gráfica.</li>
                <li><code>utils/</code>: Contém utilitários e funções auxiliares, como a conexão com o banco de dados.</li>
            </ul>
        </li>
        <li><code>db/</code>: Contém o banco de dados SQLite e arquivos de log.</li>
        <li><code>requirements.txt</code>: Lista de dependências do projeto.</li>
        <li><code>README.md</code>: Este arquivo.</li>
    </ul>

    <h2>Funcionalidades</h2>
    <ul>
        <li>Adicionar novos produtos ao estoque.</li>
        <li>Visualizar produtos existentes.</li>
        <li>Atualizar a quantidade de produtos no estoque.</li>
        <li>Registrar ações em um arquivo de log.</li>
    </ul>

    <h2>Contribuição</h2>
    <ol>
        <li>Faça um fork do projeto.</li>
        <li>Crie uma nova branch (<code>git checkout -b feature/nova-funcionalidade</code>).</li>
        <li>Faça commit das suas alterações (<code>git commit -am 'Adiciona nova funcionalidade'</code>).</li>
        <li>Faça push para a branch (<code>git push origin feature/nova-funcionalidade</code>).</li>
        <li>Crie um novo Pull Request.</li>
    </ol>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a licença MIT. Veja o arquivo <code>LICENSE</code> para mais detalhes.</p>
</body>
</html>