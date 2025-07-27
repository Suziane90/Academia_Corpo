<template>
  <div>
    <h1>Alunos</h1>
    <FormAluno @aluno-criado="buscarAlunos" :alunoParaEditar="alunoParaEditar" @atualizar-lista="buscarAlunos" />
    <AlunoList :alunos="alunos" @editar="editarAluno" @deletar="deletarAluno" />
  </div>
</template>

<script>
import { listarAlunos, deletarAluno } from '@/api/alunoService'
import AlunoList from './AlunoList.vue';
import FormAluno from './FormAluno.vue';

export default {
  components: { AlunoList, FormAluno },
  data() {
    return {
      alunos: [],
      alunoParaEditar: null,
    };
  },
  methods: {
    buscarAlunos() {
  listarAlunos()
    .then(res => {
      console.log('Alunos recebidos:', res.data)
      this.alunos = res.data;
    })
    .catch(e => console.error(e));
},
    editarAluno(aluno) {
      this.alunoParaEditar = aluno;
    },
    deletarAluno(id) {
      if (confirm('Confirma exclusão?')) {
        deletarAluno(id).then(() => this.listarAlunos());
      }
    },
  },
  mounted() {
  this.buscarAlunos();
},
};
</script>
