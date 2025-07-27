import axios from 'axios'

const URL_BASE = 'http://localhost:8000/api/exercicio/'

export function listarExercicio() {
  return axios.get(URL_BASE)
}

export function criarExercicio(data) {
  return axios.post(URL_BASE, data)
}

export function atualizarExercicio(id, data) {
  return axios.put(`${URL_BASE}${id}/`, data)
}

export function deletarExercicio(id) {
  return axios.delete(`${URL_BASE}${id}/`)
}
