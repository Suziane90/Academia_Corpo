import { createRouter, createWebHistory } from 'vue-router'
import Aluno from '@/views/aluno/Aluno.vue'

const routes = [
  {
    path: '/alunos',
    name: 'Alunos',
    component: Aluno
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

