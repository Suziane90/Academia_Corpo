<template>
  <div>
    <h1>Exercícios</h1>
    <ul v-if="exercicios.length">
      <li v-for="exercicio in exercicios" :key="exercicio.id">
        {{ exercicio.nome_exercicio }}
      </li>
    </ul>
    <p v-else>Nenhum exercício cadastrado.</p>
    <div v-if="erro" style="color:red">{{ erro }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { listarExercicio } from '@/api/exercicioService.js'

const exercicios = ref([])
const erro = ref(null)

async function carregarExercicios() {
  try {
    const resposta = await listarExercicio()
    exercicios.value = resposta.data
  } catch (e) {
    erro.value = 'Erro ao carregar exercícios'
    console.error(e)
  }
}

onMounted(() => {
  carregarExercicios()
})
</script>
