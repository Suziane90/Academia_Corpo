exercicoForm ta assim

<script>
export default {
  props: {
    exercicio: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      form: {
        nome_exercicio: '',
        grupo_muscular: 'peito',
        series: 3,
        repeticoes: 10,
        carga: 'padrao',
        descanso: 60,
        descricao: '',
        imagem: null,
        video: null,
        personal: null
      }
    }
  },
  watch: {
    exercicio: {
      immediate: true,
      handler(newVal) {
        if (newVal) {
          this.form = { ...newVal }
        } else {
          this.resetForm()
        }
      }
    }
  },
  methods: {
    resetForm() {
      this.form = {
        nome_exercicio: '',
        grupo_muscular: 'peito',
        series: 3,
        repeticoes: 10,
        carga: 'padrao',
        descanso: 60,
        descricao: '',
        imagem: null,
        video: null,
        personal: null
      }
    },
    handleFileChange(event, field) {
      const file = event.target.files[0]
      this.form[field] = file
    },
    async submitForm() {
      try {
        const formData = new FormData()

        formData.append('nome_exercicio', this.form.nome_exercicio)
        formData.append('grupo_muscular', this.form.grupo_muscular)
        formData.append('series', this.form.series)
        formData.append('repeticoes', this.form.repeticoes)
        formData.append('carga', this.form.carga)
        formData.append('descanso', this.form.descanso)
        formData.append('descricao', this.form.descricao)
        formData.append('personal', this.form.personal)

        if (this.form.imagem instanceof File) formData.append('imagem', this.form.imagem)
        if (this.form.video instanceof File) formData.append('video', this.form.video)

        const token = localStorage.getItem('token')
        const url = this.exercicio ? `/api/exercicio/${this.exercicio.id}/` : '/api/exercicio/'
        const method = this.exercicio ? 'PUT' : 'POST'

        const response = await fetch(url, {
          method,
          headers: { Authorization: `Bearer ${token}` },
          body: formData
        })

        if (!response.ok) {
          const errorData = await response.json()
          alert('Erro: ' + JSON.stringify(errorData))
          return
        }

        alert('Exercício salvo com sucesso!')
        this.$emit('salvo')
      } catch (error) {
        console.error('Erro ao salvar exercício:', error)
        alert('Erro ao salvar exercício.')
      }
    },
    cancelar() {
      this.$emit('cancelar')
    }
  }
}
</script>
<template>
  <div>
    <h1>{{ exercicio ? 'Editar Exercício' : 'Cadastrar Exercício' }}</h1>
    <form @submit.prevent="submitForm">
      <div>
        <label for="nome_exercicio">Nome exercício</label>
        <input v-model="form.nome_exercicio" type="text" id="nome_exercicio" required />
      </div>

      <div>
        <label for="grupo_muscular">Grupo Muscular</label>
        <select v-model="form.grupo_muscular" id="grupo_muscular" required>
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
      </div>

      <div>
        <label for="series">Séries</label>
        <select v-model.number="form.series" id="series" required>
          <option :value="1">1 série</option>
          <option :value="2">2 séries</option>
          <option :value="3">3 séries</option>
          <option :value="4">4 séries</option>
          <option :value="5">5 séries</option>
        </select>
      </div>

      <div>
        <label for="repeticoes">Repetições</label>
        <select v-model.number="form.repeticoes" id="repeticoes" required>
          <option :value="6">6 reps</option>
          <option :value="8">8 reps</option>
          <option :value="10">10 reps</option>
          <option :value="12">12 reps</option>
          <option :value="15">15 reps</option>
        </select>
      </div>

      <div>
        <label for="carga">Carga</label>
        <select v-model="form.carga" id="carga" required>
          <option value="leve">Leve</option>
          <option value="moderada">Moderada</option>
          <option value="padrao">Padrão</option>
          <option value="maxima">Máxima</option>
        </select>
      </div>

      <div>
        <label for="descanso">Descanso</label>
        <select v-model.number="form.descanso" id="descanso" required>
          <option :value="30">30 segundos</option>
          <option :value="45">45 segundos</option>
          <option :value="60">1 minuto</option>
          <option :value="90">1 minuto e 30</option>
          <option :value="120">2 minutos</option>
          <option :value="180">3 minutos ou mais</option>
        </select>
      </div>

      <div>
        <label for="descricao">Descrição</label>
        <textarea v-model="form.descricao" id="descricao" rows="4" placeholder="Descreva o exercício e como executá-lo corretamente" required></textarea>
      </div>

      <div>
        <label for="imagem">Imagem</label>
        <input type="file" id="imagem" @change="handleFileChange($event, 'imagem')" accept="image/*" />
      </div>

      <div>
        <label for="video">Vídeo</label>
        <input type="file" id="video" @change="handleFileChange($event, 'video')" accept="video/*" />
      </div>

      <button type="submit">Salvar</button>
      <button type="button" @click="cancelar">Cancelar</button>
    </form>
  </div>
</template>

