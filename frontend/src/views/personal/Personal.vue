<template>
  <div>
    <h1>Personal</h1>
    <FormPersonal 
      @personal-criado="buscarPersonal" 
      :PersonalParaEditar="personalParaEditar" 
      @atualizar-listar="buscarPersonal"
    />
    <PersonalFormList 
      :personal="personal" 
      @editar="editarPersonal" 
      @deletar="deletarPersonal"
    />
  </div>
</template>

<script>
import { listarPersonal, deletarPersonal } from '@api/personalService'
import PersonalFormList from './PersonalFormList.vue'
import FormPersonal from './FormPersonal.vue'

export default {
  components: {
    PersonalFormList,
    FormPersonal
  },
  data() {
    return {
      personal: [],
      personalParaEditar: null
    }
  },
  methods: {
    buscarPersonal() {
      listarPersonal()
        .then(res => {
          console.log('Personal recebidos:', res.data)
          this.personal = res.data
        })
        .catch(e => console.error(e))
    },
    editarPersonal(personal) {
      this.personalParaEditar = personal
    },
    deletarPersonal(id) {
      if (confirm('Confirma exclusão?')) {
        deletarPersonal(id).then(() => this.buscarPersonal())
      }
    }
  },
  mounted() {
    this.buscarPersonal()
  }
}
</script>
