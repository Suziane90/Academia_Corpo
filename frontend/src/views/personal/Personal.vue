<template>
  <div>
    <h1>Criar Personal com Usuário</h1>

    <form @submit.prevent="criarPersonal">
      <h2>Dados do Usuário</h2>
      <input v-model="form.user.username" placeholder="Nome de usuário" required />
      <input v-model="form.user.email" type="email" placeholder="Email" required />
      <input v-model="form.user.telefone" placeholder="Telefone" />
      <input type="file" @change="onFileChange" />
      <input v-model="form.user.password" type="password" placeholder="Senha" required />

      <h2>Dados do Personal</h2>
      <textarea v-model="form.descricao" placeholder="Descrição" required></textarea>

      <button type="submit">Criar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        user: {
          username: '',
          email: '',
          telefone: '',
          foto: null,
          password: ''
        },
        descricao: ''
      }
    }
  },
  methods: {
    onFileChange(e) {
      this.form.user.foto = e.target.files[0]
    },
    criarPersonal() {
      const formData = new FormData()
      formData.append('descricao', this.form.descricao)
      formData.append('user.username', this.form.user.username)
      formData.append('user.email', this.form.user.email)
      formData.append('user.telefone', this.form.user.telefone)
      formData.append('user.password', this.form.user.password)
      if (this.form.user.foto) {
        formData.append('user.foto', this.form.user.foto)
      }

      axios.post('http://localhost:8000/api/personals/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      .then(() => {
        alert('Personal criado com usuário!')
        // Limpar formulário
        this.form = {
          user: { username: '', email: '', telefone: '', foto: null, password: '' },
          descricao: ''
        }
      })
      .catch(err => {
        console.error('Erro:', err)
      })
    }
  }
}
</script>
