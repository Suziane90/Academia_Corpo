<template>
  <div>
    <h1>Treinos</h1>

    <!-- Formulário para criar treino -->
    <form @submit.prevent="criarTreino">
      <div>
        <label>Título:</label>
        <input v-model="form.titulo" required />
      </div>
      <div>
        <label>Descrição:</label>
        <input v-model="form.descricao" />
      </div>
      <div>
        <label>Dia da semana:</label>
        <select v-model="form.dia_da_semana" required>
          <option v-for="(label, value) in diasDaSemana" :value="value" :key="value">{{ label }}</option>
        </select>
      </div>
      <div>
        <label>Exercícios:</label>
        <select v-model="form.exercicios_ids" multiple>
          <option v-for="ex in exercicios" :key="ex.id" :value="ex.id">
            {{ ex.nome_exercicio }}
          </option>
        </select>
      </div>
      <button type="submit">Criar Treino</button>
    </form>

    <hr />

    <!-- Lista de treinos existentes -->
    <div v-for="treino in treinos" :key="treino.id" style="margin-bottom: 20px;">
      <h3>{{ treino.titulo }} ({{ treino.dia_da_semana }})</h3>
      <p>{{ treino.descricao }}</p>
      <ul>
        <li v-for="ex in treino.exercicios" :key="ex.id">
          {{ ex.nome_exercicio }} - {{ ex.grupo_muscular }} - {{ ex.series }}x{{ ex.repeticoes }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      treinos: [],
      exercicios: [],
      form: {
        titulo: '',
        descricao: '',
        dia_da_semana: '',
        exercicios_ids: []
      },
      diasDaSemana: {
        segunda: 'Segunda-feira',
        terca: 'Terça-feira',
        quarta: 'Quarta-feira',
        quinta: 'Quinta-feira',
        sexta: 'Sexta-feira',
        sabado: 'Sábado',
        domingo: 'Domingo',
      }
    }
  },
  mounted() {
    this.buscarTreinos()
    this.buscarExercicios()
  },
  methods: {
    buscarTreinos() {
      axios.get('http://localhost:8000/api/treino/')
        .then(res => {
          this.treinos = res.data
        })
        .catch(err => {
          console.error('Erro ao buscar treinos:', err)
        })
    },
    buscarExercicios() {
      axios.get('http://localhost:8000/api/exercicio/')
        .then(res => {
          this.exercicios = res.data
        })
        .catch(err => {
          console.error('Erro ao buscar exercícios:', err)
        })
    },
    criarTreino() {
      const payload = {
        personal: 1,  // coloque o ID do personal correto aqui
        titulo: this.form.titulo,
        descricao: this.form.descricao,
        dia_da_semana: this.form.dia_da_semana,
        exercicios_ids: this.form.exercicios_ids
      }

      axios.post('http://localhost:8000/api/treino/', payload)
        .then(() => {
          alert('Treino criado!')
          this.form = { titulo: '', descricao: '', dia_da_semana: '', exercicios_ids: [] }
          this.buscarTreinos()
        })
        .catch(err => {
          console.error('Erro ao criar treino:', err)
        })
    }
  }
}
</script>
