import axios from 'axios'

const BASE_URL = 'http://localhost:8000/api/treinos/'

export function criarTreino(dados) {
  return axios.post(BASE_URL, dados)
}

export function listarExercicios() {
  return axios.get('http://localhost:8000/api/exercicios/')
}

export function listarAlunos() {
  return axios.get('http://localhost:8000/api/alunos/')
}

export function atualizarTreino(id, data) {
  return axios.put(`${URL_BASE}${id}/`, data)
}

export function deletarTreino(id) {
  return axios.delete(`${URL_BASE}${id}/`)
}

