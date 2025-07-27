<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Usuário" required />
      <input v-model="password" type="password" placeholder="Senha" required />
      <button type="submit">Entrar</button>
    </form>

    <p v-if="error" style="color: red;">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const error = ref(null)
const router = useRouter()

const login = async () => {
  error.value = null

  try {
    // 1. Faz login e pega tokens
    const response = await axios.post('http://localhost:8000/api/token/', {
      username: username.value,
      password: password.value
    })

    const access = response.data.access
    const refresh = response.data.refresh

    // 2. Salva tokens no localStorage
    localStorage.setItem('access', access)
    localStorage.setItem('refresh', refresh)

    // 3. Busca dados do usuário para saber o tipo
    const userInfo = await axios.get('http://localhost:8000/api/me/', {
      headers: {
        Authorization: `Bearer ${access}`
      }
    })

    // 4. Redireciona conforme tipo
    if (userInfo.data.tipo === 'aluno') {
      router.push('/painel-aluno')
    } else if (userInfo.data.tipo === 'personal') {
      router.push('/painel-personal')
    } else {
      router.push('/') // ou alguma página padrão
    }
  } catch (err) {
    error.value = 'Usuário ou senha inválidos'
  }
}
</script>
