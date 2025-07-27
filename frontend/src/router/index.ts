import { createRouter, createWebHistory } from 'vue-router'

// Importações diretas de componentes .vue
import Aluno from '@/views/aluno/Aluno.vue'
import Exercicio from '@/views/exercicio/Exercicio.vue'
import ExercicioForm from '@/views/exercicio/ExercicioForm.vue'
import PersonalForm from '@/views/personal/PersonalForm.vue'
import FormTreino  from '@/views/treino/FormTreino.vue'
import Login from '@/views/paginas/Login.vue'
import PainelAluno from '@/views/paginas/pagAluno/PainelAluno.vue'
import PainelPersonal from '@/views/paginas/pagPersonal/PainelPersonal.vue'



const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/painel-aluno',
    name: 'PainelAluno',
    component: PainelAluno,
  },
  {
    path: '/painel-personal',
    name: 'PainelPersonal',
    component: PainelPersonal,
  },

  // suas rotas existentes:
  {
    path: '/alunos',
    name: 'Alunos',
    component: Aluno,
  },
  {
    path: '/exercicios',
    name: 'Exercicios',
    component: Exercicio,
  },
  {
    path: '/exercicios/novo',
    name: 'NovoExercicio',
    component: ExercicioForm,
  },
  {
    path: '/personal/novo',
    name: 'NovoPersonal',
    component: PersonalForm,
  },
  {
    path: '/treinos/novo',
    name: 'TreinoNovo',
    component: FormTreino,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
