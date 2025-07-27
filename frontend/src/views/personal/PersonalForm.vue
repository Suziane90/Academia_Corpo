<script setup>
import { ref } from 'vue'
import { criarPersonal } from '@/api/personalService'

const emit = defineEmits(['personal-criado'])

const form = ref({
  user: {
    email: '',
    name: '',
    phone: '',
    password: '',
    foto: null
  },
  descricao: ''
})

function salvar() {
  criarPersonal(form.value)
    .then(() => {
      emit('personal-criado')
      alert('Personal criado com sucesso!')
      form.value = {
        user: {
          email: '',
          name: '',
          phone: '',
          password: '',
          foto: null
        },
        descricao: ''
      }
    })
    .catch(err => {
      console.error(err)
      alert('Erro ao criar personal.')
    })
}

function handleFoto(e) {
  const file = e.target.files[0]
  form.value.user.foto = file
}
</script>

<template>
  <form @submit.prevent="salvar">
    <h2>Cadastrar Personal</h2>

    <div>
      <label>Foto:</label>
      <input type="file" @change="handleFoto" accept="image/*" required />
    </div>

    <div>
      <label>Email:</label>
      <input v-model="form.user.email" type="email" required />
    </div>

    <div>
      <label>Nome:</label>
      <input v-model="form.user.name" type="text" required />
    </div>

    <div>
      <label>Telefone:</label>
      <input v-model="form.user.phone" type="text" required />
    </div>

    <div>
      <label>Senha:</label>
      <input v-model="form.user.password" type="password" required />
    </div>

    <div>
      <label>Descrição:</label>
      <textarea v-model="form.descricao" required></textarea>
    </div>

    <button type="submit">Salvar</button>
  </form>
</template>
