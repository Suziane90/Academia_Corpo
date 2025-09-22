<template>
  <div class="painel-personal">
    <h1>Olá, Rayane!</h1>
    <input v-model="busca" placeholder="Buscar..." />

    <nav class="abas">
      <button :class="{ ativa: abaAtiva === 'alunos' }" @click="abaAtiva = 'alunos'">Alunos</button>
      <button :class="{ ativa: abaAtiva === 'exercicios' }" @click="abaAtiva = 'exercicios'">Exercícios</button>
      <button :class="{ ativa: abaAtiva === 'personal' }" @click="abaAtiva = 'personal'">Personal</button>
    </nav>

    <section v-if="abaAtiva === 'alunos'" class="aba-alunos">
      <div v-if="alunosFiltrados.length === 0">Nenhum aluno encontrado.</div>
      <div class="lista-cards">
        <AlunoCard
          v-for="aluno in alunosFiltrados"
          :key="aluno.id"
          :aluno="aluno"
          @ver-treinos="onVerTreinos"
        />
      </div>
    </section>

    <section v-if="abaAtiva === 'exercicios'">
      <ExerciciosLista
        v-if="!mostraForm"
        @abrir-form="abrirForm"
        @editar-exercicio="editarExercicio"
        @deletar-exercicio="deletarExercicio"
      />
      <ExercicioForm
        v-else
        :exercicio="exercicioEditando"
        @salvo="onExercicioSalvo"
        @cancelar="fecharForm"
      />
    </section>

    <section v-if="abaAtiva === 'personal'">
      <p>Aqui vão os dados do personal (ainda não implementado).</p>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import AlunoCard from './AlunoCard.vue' // mesmo diretório
import ExerciciosLista from '../../exercicio/ExerciciosLista.vue' // sobe dois níveis e entra em exercicio
import ExercicioForm from '../../exercicio/ExercicioForm.vue'


const abaAtiva = ref('alunos')
const busca = ref('')
const alunos = ref([])
const mostraForm = ref(false)
const exercicioEditando = ref(null)

const alunosFiltrados = computed(() => {
  if (!busca.value) return alunos.value
  return alunos.value.filter(aluno =>
    aluno.user.username.toLowerCase().includes(busca.value.toLowerCase())
  )
})

function onVerTreinos(aluno) {
  alert(`Ver treinos do aluno: ${aluno.user.username}`)
}

function abrirForm() {
  exercicioEditando.value = null
  mostraForm.value = true
}

function fecharForm() {
  mostraForm.value = false
  exercicioEditando.value = null
}

function editarExercicio(ex) {
  exercicioEditando.value = ex
  mostraForm.value = true
}

async function deletarExercicio(ex) {
  if (!confirm(`Deseja deletar o exercício "${ex.nome_exercicio}"?`)) return
  try {
    const token = localStorage.getItem('token')
    await axios.delete(`http://localhost:8000/api/exercicio/${ex.id}/`, {
      headers: { Authorization: `Bearer ${token}` }
    })
    alert('Exercício deletado com sucesso!')
    // Recarregar lista pode ser feito emitindo evento para ExerciciosLista, ou usar refetch via store/composição
  } catch (error) {
    console.error('Erro ao deletar exercício:', error)
    alert('Erro ao deletar exercício.')
  }
}

function onExercicioSalvo() {
  fecharForm()
  // Aqui você pode atualizar a lista de exercícios (exemplo: emitir evento ou atualizar estado global)
}
 
onMounted(async () => {
  const token = localStorage.getItem('token')
  try {
    const response = await axios.get('http://localhost:8000/api/alunos/', {
      headers: { Authorization: `Bearer ${token}` }
    })
    alunos.value = response.data.map(aluno => ({
      id: aluno.id,
      objetivo: aluno.objetivo,
      user: {
        username: aluno.user.username || 'Sem nome',
        foto: aluno.user.foto || 'https://i.pravatar.cc/150?img=3'
      }
    }))
  } catch (error) {
    console.error('Erro ao buscar alunos:', error)
    alert('Erro ao carregar alunos.')
  }
})
</script>

<style scoped>
.painel-personal {
  max-width: 900px;
  margin: auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

input[type='text'] {
  padding: 8px;
  font-size: 14px;
  width: 250px;
  margin-bottom: 15px;
}

.abas {
  margin-bottom: 15px;
}

.abas button {
  padding: 10px 15px;
  margin-right: 8px;
  border: none;
  background: #eee;
  cursor: pointer;
  border-radius: 4px;
  font-weight: bold;
}

.abas button.ativa {
  background: #007bff;
  color: white;
}

.lista-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}
</style>
