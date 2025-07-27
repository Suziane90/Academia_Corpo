import axios from 'axios'

const URL_BASE = 'http://localhost:8000/api/alunos/'

export function listarAlunos() {
  return axios.get(URL_BASE)
}

export async function criarAluno(dados) {
  const formData = new FormData();

  formData.append('user.username', dados.user.username);
  formData.append('user.email', dados.user.email);
  formData.append('user.telefone', dados.user.telefone || '');
  formData.append('user.password', dados.user.password);
  if (dados.user.foto) {
    formData.append('user.foto', dados.user.foto);
  }
  formData.append('objetivo', dados.objetivo);

  return axios.post(URL_BASE, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
}

export function atualizarAluno(id, dados) {
  const formData = new FormData();

  formData.append('user.username', dados.user.username);
  formData.append('user.email', dados.user.email);
  formData.append('user.telefone', dados.user.telefone || '');
  if (dados.user.password) {
    formData.append('user.password', dados.user.password);
  }
  if (dados.user.foto) {
    formData.append('user.foto', dados.user.foto);
  }
  formData.append('objetivo', dados.objetivo);

  return axios.put(`${URL_BASE}${id}/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
}

export function deletarAluno(id) {
  return axios.delete(`${URL_BASE}${id}/`)
}
