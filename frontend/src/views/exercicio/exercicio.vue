<template>
  <div>
    <h2>Cadastrar Exercício</h2>
    <form @submit.prevent="criarExercicio" enctype="multipart/form-data">

      <label>Nome do Exercício:</label>
      <input v-model="form.nome_exercicio" required />

      <label>Descrição:</label>
      <textarea v-model="form.descricao" />

      <label>Grupo Muscular:</label>
      <select v-model="form.grupo_muscular">
        <option value="peito">Peito</option>
        <option value="costas">Costas</option>
        <option value="ombros">Ombros</option>
        <option value="biceps">Bíceps</option>
        <option value="triceps">Tríceps</option>
        <option value="abdomen">Abdômen</option>
        <option value="gluteos">Glúteos</option>
        <option value="quadriceps">Quadríceps</option>
        <option value="posterior_coxa">Posterior da Coxa</option>
        <option value="panturrilha">Panturrilha</option>
        <option value="antebraco">Antebraço</option>
      </select>

      <label>Séries:</label>
      <input type="number" v-model.number="form.series" required />

      <label>Repetições:</label>
      <input type="number" v-model.number="form.repeticoes" required />

      <label>Carga:</label>
      <select v-model="form.carga">
        <option value="leve">Leve</option>
        <option value="moderada">Moderada</option>
        <option value="padrao">Padrão</option>
        <option value="maxima">Máxima</option>
      </select>

      <label>Descanso (segundos):</label>
      <input type="number" v-model.number="form.descanso" required />

      <label>Imagem:</label>
      <input type="file" @change="onImagemChange" />

      <label>Vídeo:</label>
      <input type="file" @change="onVideoChange" />

      <button type="submit">Salvar Exercício</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      form: {
        personal: 1, // coloque aqui o ID do personal que está logado
        nome_exercicio: '',
        descricao: '',
        grupo_muscular: 'peito',
        series: 3,
        repeticoes: 10,
        carga: 'padrao',
        descanso: 60,
        imagem: null,
        video: null
      }
    }
  },
  methods: {
    onImagemChange(e) {
      this.form.imagem = e.target.files[0]
    },
    onVideoChange(e) {
      this.form.video = e.target.files[0]
    },
    criarExercicio() {
      const formData = new FormData()
      formData.append('personal', this.form.personal)
      formData.append('nome_exercicio', this.form.nome_exercicio)
      formData.append('descricao', this.form.descricao)
      formData.append('grupo_muscular', this.form.grupo_muscular)
      formData.append('series', this.form.series)
      formData.append('repeticoes', this.form.repeticoes)
      formData.append('carga', this.form.carga)
      formData.append('descanso', this.form.descanso)
      if (this.form.imagem) {
        formData.append('imagem', this.form.imagem)
      }
      if (this.form.video) {
        formData.append('video', this.form.video)
      }

      axios.post('http://localhost:8000/api/exercicios/', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      })
      .then(() => {
        alert('Exercício cadastrado com sucesso!')
        this.resetarFormulario()
      })
      .catch(error => {
        console.error('Erro ao cadastrar exercício:', error)
      })
    },
    resetarFormulario() {
      this.form = {
        personal: 1,
        nome_exercicio: '',
        descricao: '',
        grupo_muscular: 'peito',
        series: 3,
        repeticoes: 10,
        carga: 'padrao',
        descanso: 60,
        imagem: null,
        video: null
      }
    }
  }
}
</script>
