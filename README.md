ErrorTrack

Arthur Caetano de Queiroz, Arthur Fernandes Costa Martins, Ian Fideles dos Reis Silva, Ulisses Greg dos Santos Bragança & Samuel Costa Motta.

Front-end:
HTML, CSS e JavaScript.
Back-end:
Python
Banco de dados:
MySQL

Descrição.

Instruções básicas para executar o projeto, quando aplicável.

Funcionalidades

Alunos: Cadastro, listagem e busca por ID ou nome.

Questões: Cadastro, consulta e listagem por simulado.

Relatório de Erros: Mapeamento do desempenho do aluno.

Classes: Aluno, Aula, Simulado, Questao, MapaErro e MotorIa.

Estrutura do Projeto

Controller: Gerencia as rotas e requisições HTTP.

Service: Aplica as regras de negócio.

Model: Representa as tabelas do banco de dados.

Repository: Executa as Stored Procedures e buscas avançadas.

Stored Procedures (MySQL)

sp_buscar_alunos_por_nome: Busca alunos por nome com ordenação.

sp_buscar_questoes_por_simulado: Retorna as questões de um simulado específico (JOIN).

sp_gerar_relatorio_erros: Filtra os erros do aluno combinando as tabelas necessárias (JOIN).

Principais Rotas

GET /alunos -> Lista os alunos (aceita ?nome=exemplo).

POST /alunos -> Cadastra um aluno.

GET /questoes -> Lista as questões (aceita ?simulado_id=1).

POST /questoes -> Cadastra uma questão.

GET /questoes/relatorio-erros/<aluno_id> -> Gera relatório de erros.


Cadastrar Aluno (Tela -> API -> AlunoController -> CadastrarAlunoService -> Aluno Model -> MySQL)
Listar Todos os Alunos (Tela -> API -> AlunoController -> ListarAlunosService -> Aluno Model -> MySQL)
Buscar Aluno por ID (Tela -> API -> AlunoController -> BuscarAlunoPorIdService -> Aluno Model -> MySQL)
Atualizar Aluno (Tela -> API -> AlunoController -> AtualizarAlunoService -> Aluno Model -> MySQL)
Excluir Aluno (Tela -> API -> AlunoController -> ExcluirAlunoService -> Aluno Model -> MySQL)
Buscar Alunos por Nome (Tela -> API -> AlunoController -> BuscarAlunosPorNomeService -> AlunoRepository -> Stored Procedure)
Cadastrar Questão (Tela -> API -> QuestaoController -> CadastrarQuestaoService -> Questao Model -> MySQL)
Listar Todas as Questões (Tela -> API -> QuestaoController -> ListarQuestoesService -> Questao Model -> MySQL)
Buscar Questões por Simulado (Tela -> API -> QuestaoController -> BuscarQuestoesPorSimuladoService -> QuestaoRepository -> Stored Procedure)
Gerar Relatório de Erros por Aluno (Tela -> API -> QuestaoController -> RelatorioErrosService -> QuestaoRepository -> Stored Procedure)