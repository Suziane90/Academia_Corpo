<template>
  <ul>
    <li v-for="aluno in alunos" :key="aluno.id">
      {{ aluno.user.username }} - {{ aluno.user.email }} - {{ aluno.objetivo }}
      <button @click="$emit('editar', aluno)">Editar</button>
      <button @click="$emit('deletar', aluno.id)">Excluir</button>
    </li>
  </ul>
</template>

<script>
export default {
  props: ['alunos'],
};
</script>
