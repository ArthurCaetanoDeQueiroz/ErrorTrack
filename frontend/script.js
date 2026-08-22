// --- CÓDIGO ORIGINAL QUE JÁ ESTAVA NO SEU ARQUIVO (NÃO APAGAR) ---
const barra = document.querySelector('.barra');
const mudar = document.querySelector('.barramudar');
const alunoForm = document.getElementById('alunoForm');
const alunoIdInput = document.getElementById('alunoId');
const nomeInput = document.getElementById('nome');
const materiaInput = document.getElementById('materia');
const formButton = document.getElementById('formButton');
const cancelarAtualizacao = document.getElementById('cancelarAtualizacao');
const buscarForm = document.getElementById('buscarForm');
const buscarIdInput = document.getElementById('buscarId');
const mensagem = document.getElementById('mensagem');
const listaAlunos = document.getElementById('listaAlunos');

mudar.addEventListener('click', () => {
  barra.classList.toggle('expandir');
  document.body.classList.toggle('barraexpandir');
  const expandido = document.body.classList.contains('barraexpandir');
  mudar.textContent = expandido ? '‹' : '›';
  mudar.setAttribute('aria-label', expandido ? 'Recolher barra' : 'Expandir barra');
});

alunoForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const id = alunoIdInput.value;
  const nome = nomeInput.value.trim();
  const materia = materiaInput.value.trim();

  if (!nome || !materia) {
    mostrarMensagem('Preencha nome e matéria.', 'erro');
    return;
  }

  if (id) {
    await atualizarAluno(id, { name: nome, materia });
  } else {
    await criarAluno({ name: nome, materia });
  }

  limparFormulario();
  listarAlunos();
});

cancelarAtualizacao.addEventListener('click', () => {
  limparFormulario();
});

buscarForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const id = buscarIdInput.value.trim();

  if (!id) {
    listarAlunos();
    return;
  }

  await buscarAluno(id);
});

async function criarAluno(dados) {
  const response = await fetch('/alunos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dados),
  });

  if (!response.ok) {
    const erro = await response.json();
    mostrarMensagem(erro.erro || 'Erro ao criar aluno.', 'erro');
    return;
  }

  const aluno = await response.json();
  mostrarMensagem(`Aluno ${aluno.name} criado com sucesso.`, 'sucesso');
}

async function listarAlunos() {
  const response = await fetch('/alunos');
  if (!response.ok) {
    mostrarMensagem('Erro ao listar alunos.', 'erro');
    return;
  }
  const alunos = await response.json();
  renderizarLista(alunos);
}

async function buscarAluno(id) {
  const response = await fetch(`/alunos/${id}`);
  if (!response.ok) {
    if (response.status === 404) {
      mostrarMensagem('Aluno não encontrado.', 'erro');
      return;
    }
    mostrarMensagem('Erro ao buscar aluno.', 'erro');
    return;
  }
  const aluno = await response.json();
  renderizarLista([aluno]);
}

async function atualizarAluno(id, dados) {
  const response = await fetch(`/alunos/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dados),
  });

  if (!response.ok) {
    const erro = await response.json();
    mostrarMensagem(erro.erro || 'Erro ao atualizar aluno.', 'erro');
    return;
  }

  const aluno = await response.json();
  mostrarMensagem(`Aluno ${aluno.name} atualizado com sucesso.`, 'sucesso');
}

async function deletarAluno(id) {
  const response = await fetch(`/alunos/${id}`, {
    method: 'DELETE',
  });

  if (!response.ok) {
    mostrarMensagem('Erro ao deletar aluno.', 'erro');
    return;
  }

  mostrarMensagem(`Aluno ${id} removido com sucesso.`, 'sucesso');
  listarAlunos();
}

function prepararEdicao(aluno) {
  alunoIdInput.value = aluno.id;
  nomeInput.value = aluno.name;
  materiaInput.value = aluno.materia;
  formButton.textContent = 'Atualizar';
  cancelarAtualizacao.classList.remove('hidden');
}

function limparFormulario() {
  alunoIdInput.value = '';
  nomeInput.value = '';
  materiaInput.value = '';
  formButton.textContent = 'Criar';
  cancelarAtualizacao.classList.add('hidden');
}

function mostrarMensagem(texto, tipo) {
  mensagem.textContent = texto;
  mensagem.className = `mensagem ${tipo}`;
}

function renderizarLista(alunos) {
  listaAlunos.innerHTML = '';
  if (!alunos.length) {
    listaAlunos.innerHTML = '<p>Nenhum aluno encontrado.</p>';
    return;
  }

  alunos.forEach((aluno) => {
    const item = document.createElement('div');
    item.className = 'aluno-item';
    item.innerHTML = `
      <div>
        <strong>ID:</strong> ${aluno.id}<br>
        <strong>Nome:</strong> ${aluno.name}<br>
        <strong>Matéria:</strong> ${aluno.materia}
      </div>
      <div class="aluno-acoes">
        <button class="botao" data-id="${aluno.id}" data-action="editar">Editar</button>
        <button class="botao secundario" data-id="${aluno.id}" data-action="deletar">Deletar</button>
      </div>
    `;

    const editar = item.querySelector('[data-action="editar"]');
    const deletar = item.querySelector('[data-action="deletar"]');

    editar.addEventListener('click', () => prepararEdicao(aluno));
    deletar.addEventListener('click', () => deletarAluno(aluno.id));

    listaAlunos.appendChild(item);
  });
}

listarAlunos();

// Buscar Aluno por Nome (Stored Procedure)
const buscarNomeForm = document.getElementById('buscarNomeForm');
if (buscarNomeForm) {
  buscarNomeForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const nome = document.getElementById('buscarNome').value.trim();
    if (!nome) {
      listarAlunos();
      return;
    }
    const response = await fetch(`/alunos?nome=${encodeURIComponent(nome)}`);
    if (response.ok) {
      const alunos = await response.json();
      renderizarLista(alunos);
    }
  });
}

// Questões e Relatórios
const questaoForm = document.getElementById('questaoForm');
const buscarSimuladoForm = document.getElementById('buscarSimuladoForm');
const btnListarQuestoes = document.getElementById('btnListarQuestoes');
const listaQuestoes = document.getElementById('listaQuestoes');

if (questaoForm) {
  questaoForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const enunciado = document.getElementById('enunciado').value;
    const materia = document.getElementById('materia') ? document.getElementById('materia').value : '';
    const alternativa_correta = document.getElementById('alternativaCorreta').value;

    const res = await fetch('/questoes', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ enunciado, materia, alternativa_correta })
    });

    if (res.ok) {
      mostrarMensagem('Questão criada com sucesso!', 'sucesso');
      questaoForm.reset();
      carregarQuestoes();
    } else {
      mostrarMensagem('Erro ao criar questão.', 'erro');
    }
  });
}

async function carregarQuestoes(termo = '') {
  let url = '/questoes';
  if (termo) {
    url += `?busca=${encodeURIComponent(termo)}`;
  }
  const res = await fetch(url);
  const dados = await res.json();
  
  if (listaQuestoes) {
    if (Array.isArray(dados)) {
      listaQuestoes.innerHTML = dados.map(q => `
        <div class="questao-item" style="border: 1px solid #ccc; padding: 10px; margin-bottom: 5px;">
          <strong>ID:</strong> ${q.id}<br>
          <strong>Matéria:</strong> ${q.materia || 'Não informada'}<br>
          <strong>Enunciado:</strong> ${q.enunciado}<br>
          <strong>Correta:</strong> ${q.alternativa_correta}
        </div>
      `).join('') || '<p>Nenhuma questão encontrada.</p>';
    } else {
      listaQuestoes.innerHTML = `<pre>${JSON.stringify(dados, null, 2)}</pre>`;
    }
  }
}

if (btnListarQuestoes) {
  btnListarQuestoes.addEventListener('click', () => {
    carregarQuestoes();
  });
}

if (buscarSimuladoForm) {
  buscarSimuladoForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('buscarSimuladoId').value.trim();
    
    if (!id) {
      carregarQuestoes();
      return;
    }

    const res = await fetch(`/questoes/${id}`);
    if (res.ok) {
      const q = await res.json();
      listaQuestoes.innerHTML = `
        <div class="questao-item" style="border: 1px solid #ccc; padding: 10px; margin-bottom: 5px;">
          <strong>ID:</strong> ${q.id}<br>
          <strong>Matéria:</strong> ${q.materia || 'Não informada'}<br>
          <strong>Enunciado:</strong> ${q.enunciado}<br>
          <strong>Correta:</strong> ${q.alternativa_correta}
        </div>
      `;
    } else {
      listaQuestoes.innerHTML = '<p>Questão não encontrada com esse ID.</p>';
    }
  });
}

const relatorioForm = document.getElementById('relatorioForm');
const listaRelatorio = document.getElementById('listaRelatorio');

if (relatorioForm) {
  relatorioForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = document.getElementById('relatorioAlunoId').value.trim();
    
    if (!id) {
      listaRelatorio.innerHTML = '<p>Digite o ID do aluno.</p>';
      return;
    }

    try {
      const res = await fetch(`/questoes/relatorio-erros/${id}`);
      const dados = await res.json();
      
      if (res.ok) {
        listaRelatorio.innerHTML = `<pre>${JSON.stringify(dados, null, 2)}</pre>`;
      } else {
        listaRelatorio.innerHTML = `<p>Erro: ${dados.error || 'Não foi possível gerar o relatório.'}</p>`;
      }
    } catch (err) {
      listaRelatorio.innerHTML = '<p>Erro de conexão com o servidor.</p>';
    }
  });
}