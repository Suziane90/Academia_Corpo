<!-- src/views/exercicio/ExerciciosLista.vue -->
<template>
  <div class="exercicios-container">
    <button class="btn-adicionar" @click="$emit('abrir-form')">Adicionar Exercício</button>

    <div v-if="exercicios.length === 0" class="vazio">
      Nenhum exercício cadastrado.
    </div>

    <div class="lista-cards" v-else>
      <div v-for="ex in exercicios" :key="ex.id" class="exercicio-card">
        <img :src="ex.imagemUrl || '/imagens/foto-padrao.png'" alt="Imagem exercício" />
        <h3>{{ ex.nome_exercicio }}</h3>

        <div class="botoes">
          <button @click="$emit('editar-exercicio', ex)">Editar</button>
          <button @click="$emit('deletar-exercicio', ex)">Deletar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const exercicios = ref([])

onMounted(async () => {
  try {
    const token = localStorage.getItem('token')
    const res = await axios.get('http://localhost:8000/api/exercicio/', {
      headers: { Authorization: `Bearer ${token}` }
    })
    exercicios.value = res.data
  } catch (error) {
    console.error('Erro ao carregar exercícios:', error)
  }
})
</script>

<style scoped>
.exercicios-container {
  padding: 10px;
}
.btn-adicionar {
  background-color: #4caf50;
  color: white;
  padding: 10px 16px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  margin-bottom: 16px;
  font-weight: bold;
  transition: background-color 0.3s ease;
}
.btn-adicionar:hover {
  background-color: #388e3c;
}
.lista-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
.exercicio-card {
  width: 240px;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 12px;
  box-shadow: 0 2px 6px rgb(0 0 0 / 0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  background: white;
}
.exercicio-card img {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 10px;
  border: 2px solid #4caf50;
}
.exercicio-card h3 {
  margin: 0;
  text-align: center;
  color: #333;
}
.botoes {
  display: flex;
  gap: 12px;
  width: 100%;
}
.botoes button {
  flex: 1;
  padding: 8px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}
.botoes button:first-child {
  background-color: #2196f3;
  color: white;
}
.botoes button:first-child:hover {
  background-color: #1976d2;
}
.botoes button:last-child {
  background-color: #f44336;
  color: white;
}
.botoes button:last-child:hover {
  background-color: #d32f2f;
}
.vazio {
  color: #777;
  font-style: italic;
}
</style>
