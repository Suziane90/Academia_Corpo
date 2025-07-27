<script setup>
import { ref, onMounted } from 'vue'
import { criarTreino, listarExercicios, listarAlunos } from '@/api/TreinoService'

const form = ref({
  titulo: '',
  descricao: '',
  dia_da_semana: 'segunda',
  aluno: '',
  personal: '',  // ou você já define com o ID logado
  exercicios_ids: []
})

const alunos = ref([])
const exercicios = ref([])

onMounted(() => {
  listarAlunos().then(res => alunos.value = res.data)
  listarExercicios().then(res => exercicios.value = res.data)
})

function salvar() {
  criarTreino(form.value)
    .then(() => {
      alert('Treino criado com sucesso!')
      // Resetar formulário
      form.value = {
        titulo: '',
        descricao: '',
        dia_da_semana: 'segunda',
        aluno: '',
        personal: '',
        exercicios_ids: []
      }
    })
    .catch(err => {
      console.error(err)
      alert('Erro ao criar treino.')
    })
}
</script>

<template>
  <form @submit.prevent="salvar">
    <h2>Cadastrar Treino</h2>

    <div>
      <label>Aluno:</label>
      <select v-model="form.aluno" required>
        <option disabled value="">Selecione um aluno</option>
        <option v-for="a in alunos" :key="a.id" :value="a.id">
          {{ a.user.username }}
        </option>
      </select>
    </div>

    <div>
      <label>Título:</label>
      <input v-model="form.titulo" required />
    </div>

    <div>
      <label>Descrição:</label>
      <textarea v-model="form.descricao" />
    </div>

    <div>
      <label>Dia da Semana:</label>
      <select v-model="form.dia_da_semana" required>
        <option value="segunda">Segunda</option>
        <option value="terca">Terça</option>
        <option value="quarta">Quarta</option>
        <option value="quinta">Quinta</option>
        <option value="sexta">Sexta</option>
        <option value="sabado">Sábado</option>
        <option value="domingo">Domingo</option>
      </select>
    </div>

    <div>
      <label>Exercícios:</label>
      <select v-model="form.exercicios_ids" multiple required>
        <option v-for="e in exercicios" :key="e.id" :value="e.id">
          {{ e.nome }} ({{ e.grupo_muscular }})
        </option>
      </select>
    </div>

    <button type="submit">Salvar</button>
  </form>
</template>
