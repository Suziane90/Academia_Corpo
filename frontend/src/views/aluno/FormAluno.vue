<template>
  <form @submit.prevent="onSubmit">
    <input v-model="form.user.username" placeholder="Nome completo" required />
    <input v-model="form.user.email" type="email" placeholder="Email" required />
    <input v-model="form.user.telefone" placeholder="Telefone" />
    <input type="file" @change="onFileChange" />
    <input v-model="form.user.password" type="password" placeholder="Senha" :required="!isEditando" />
    <input v-model="form.aluno.objetivo" placeholder="Objetivo" required />
    <button type="submit">{{ isEditando ? 'Atualizar' : 'Criar' }}</button>
  </form>
</template>

<script>
import { criarAluno, atualizarAluno } from '@/api/alunoService'

export default {
  props: ['alunoParaEditar'],
  data() {
    return {
      form: {
        user: {
          username: '',
          email: '',
          telefone: '',
          foto: null,
          password: '',
        },
        aluno: {
          objetivo: '',
        },
      },
      isEditando: false,
    }
  },
  watch: {
    alunoParaEditar: {
      handler(novoAluno) {
        if (novoAluno) {
          this.isEditando = true;
          this.form.user.username = novoAluno.user.username;
          this.form.user.email = novoAluno.user.email;
          this.form.user.telefone = novoAluno.user.telefone || '';
          this.form.aluno.objetivo = novoAluno.objetivo;
        } else {
          this.resetForm();
        }
      },
      immediate: true,
    },
  },
  methods: {
    onFileChange(e) {
      this.form.user.foto = e.target.files[0];
    },
    resetForm() {
      this.isEditando = false;
      this.form = {
        user: {
          username: '',
          email: '',
          telefone: '',
          foto: null,
          password: '',
        },
        aluno: {
          objetivo: '',
        },
      };
    },
    onSubmit() {
      const dados = {
        objetivo: this.form.aluno.objetivo,
        user: {
          username: this.form.user.username,
          email: this.form.user.email,
          telefone: this.form.user.telefone,
          foto: this.form.user.foto,
        },
      };

      if (!this.isEditando || this.form.user.password) {
        dados.user.password = this.form.user.password;
      }

      if (this.isEditando) {
        atualizarAluno(this.alunoParaEditar.id, dados)
          .then(() => {
            this.$emit('atualizar-lista');
            this.resetForm();
          })
          .catch(console.error);
      } else {
        criarAluno(dados)
          .then(() => {
            this.$emit('aluno-criado');
            this.resetForm();
          })
          .catch(console.error);
      }
    },
  },
};
</script>
