<template>
  <div class="aluno-card">
    <img :src="fotoCompleta" alt="Foto do aluno" />
    <h3>{{ aluno.user?.username || 'Sem nome' }}</h3>
    <p><strong>Objetivo:</strong> {{ aluno.objetivo || 'Sem objetivo' }}</p>

    <button @click="$emit('ver-treinos', aluno)">Treino</button>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  aluno: {
    type: Object,
    required: true
  }
})

const fotoPadrao = '/imagens/foto-padrao.png'

const fotoCompleta = computed(() => {
  const foto = props.aluno?.user?.foto
  return foto || fotoPadrao
})
</script>

<style scoped>
.aluno-card {
  width: 320px;
  height: 380px;
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 2px 6px rgb(0 0 0 / 0.15);
  background: #fff;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

  flex-shrink: 0;
  flex-grow: 0;
  box-sizing: border-box;
}

.aluno-card img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #4caf50;
}

.aluno-card h3 {
  margin: 0;
  color: #333;
  font-size: 1.3rem;
  text-align: center;
  max-height: 2.4em; /* cerca de 2 linhas */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.aluno-card p {
  color: #555;
  font-size: 1rem;
  text-align: center;
  margin: 0;
  max-height: 3.6em; /* cerca de 3 linhas */
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
}

.aluno-card button {
  background-color: #4caf50;
  border: none;
  border-radius: 6px;
  color: white;
  padding: 10px 18px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
  margin-top: auto;
  width: 100%;
}

.aluno-card button:hover {
  background-color: #388e3c;
}
</style>
