import axios from 'axios'

const URL_BASE = 'http://localhost:8000/api/alunos/'

export function listarAlunos() {
  return axios.get(URL_BASE)
}

export function criarAluno(data) {
  return axios.post(URL_BASE, data)
}

export function atualizarAluno(id, data) {
  return axios.put(`${URL_BASE}${id}/`, data)
}

export function deletarAluno(id) {
  return axios.delete(`${URL_BASE}${id}/`)
}
