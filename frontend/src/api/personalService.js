import axios from 'axios'

const URL_BASE = 'http://localhost:8000/api/personal/'

export function listarPersonal() {
  return axios.get(URL_BASE)
}

export async function criarPersonal(dados) {
  const formData = new FormData()

  // Campos do usuário (com nomes esperados pelo serializer)
  formData.append('user.email', dados.user.email)
  formData.append('user.username', dados.user.name)      // nome = username
  formData.append('user.telefone', dados.user.phone)     // telefone = phone
  formData.append('user.password', dados.user.password)

  if (dados.user.foto) {
    formData.append('user.foto', dados.user.foto)
  }

  // Campos do modelo Personal
  formData.append('descricao', dados.descricao)

  return axios.post(URL_BASE, formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  })
}

export function atualizarPersonal(id, data) {
  return axios.put(`${URL_BASE}${id}/`, data)
}

export function deletarPersonal(id) {
  return axios.delete(`${URL_BASE}${id}/`)
}
