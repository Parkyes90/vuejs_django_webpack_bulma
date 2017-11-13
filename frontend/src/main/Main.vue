<template>
  <div>
    <app-main-template></app-main-template>
  </div>
</template>

<script>
  import MainTemplate from '../main/MainTemplate'
  import axios from 'axios'
  export default {
    components: {
      appMainTemplate: MainTemplate
    },
    data: {
      lists: {}
    },
    mounted: () => {
      axios.get('/board/listup')
        .then((response) => {
          this.lists = response.data
        })
    }
  }
</script>
<style lang="css">
</style>
