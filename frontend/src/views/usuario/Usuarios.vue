<template>
  <div>
    <h1>Usuários</h1>

    <!-- Formulário para criar -->
    <form @submit.prevent="criarUsuario" enctype="multipart/form-data">
      <div>
        <label>Nome de usuário:</label>
        <input type="text" v-model="form.username" required />
      </div>
      <div>
        <label>Email:</label>
        <input type="email" v-model="form.email" required />
      </div>
      <div>
        <label>Telefone:</label>
        <input type="text" v-model="form.telefone" />
      </div>
      <div>
        <label>Foto:</label>
        <input type="file" ref="fileInput" @change="onFileChange" />
      </div>
      <button type="submit">Criar Usuário</button>
    </form>

    <hr />

    <!-- Lista de usuários -->
    <ul>
      <li v-for="usuario in usuarios" :key="usuario.id">
        {{ usuario.username }} - {{ usuario.email }} - {{ usuario.telefone || 'Sem telefone' }}
        <button @click="deletarUsuario(usuario.id)">Deletar</button>
        <button @click="editarUsuarioPrompt(usuario)">Editar</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      usuarios: [],
      form: {
        username: '',
        email: '',
        telefone: '',
        foto: null,
      }
    }
  },
  mounted() {
    this.buscarUsuarios()
  },
  methods: {
    buscarUsuarios() {
      axios.get('http://localhost:8000/api/usuarios/')
        .then(response => {
          this.usuarios = response.data
        })
        .catch(error => {
          console.error('Erro ao buscar usuários:', error)
        })
    },
    onFileChange(event) {
      this.form.foto = event.target.files[0]
    },
    criarUsuario() {
    const formData = new FormData();
    formData.append('username', this.form.username);
    formData.append('email', this.form.email);
    formData.append('telefone', this.form.telefone);
    if (this.form.foto) {
        formData.append('foto', this.form.foto);
    }

    axios.post('http://localhost:8000/api/usuarios/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    })
    .then(() => {
        alert('Usuário criado!');
        this.buscarUsuarios();
    })
    .catch(err => console.error(err));
    }
    ,
    limparFormulario() {
      this.form.username = ''
      this.form.email = ''
      this.form.telefone = ''
      this.form.foto = null
      this.$refs.fileInput.value = null
    },

    // Deleta usuário pelo ID
    deletarUsuario(usuarioId) {
      axios.delete(`http://localhost:8000/api/usuarios/${usuarioId}/`)
        .then(() => {
          alert('Usuário deletado com sucesso!')
          this.buscarUsuarios()
        })
        .catch(err => console.error('Erro ao deletar usuário:', err))
    },

    // Editar usuário (exemplo simples com prompt)
    editarUsuarioPrompt(usuario) {
      const novoEmail = prompt('Novo email:', usuario.email)
      const novoTelefone = prompt('Novo telefone:', usuario.telefone)

      if (novoEmail !== null && novoTelefone !== null) {
        axios.patch(`http://localhost:8000/api/usuarios/${usuario.id}/`, {
          email: novoEmail,
          telefone: novoTelefone
        })
        .then(() => {
          alert('Usuário atualizado!')
          this.buscarUsuarios()
        })
        .catch(err => console.error('Erro ao atualizar usuário:', err))
      }
    }
  }
}
</script>
