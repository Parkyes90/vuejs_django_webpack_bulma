<template>
  <div>
    <button type=button :click="listup()">as</button>
    <app-main-template></app-main-template>
  </div>
</template>

<script>
  import MainTemplate from '../main/MainTemplate'
  import axios from 'axios'
  axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
  axios.defaults.xsrfCookieName = 'csrftoken'
  export default {
    components: {
      appMainTemplate: MainTemplate
    },
    methods: {
      listup () {
        axios.get('/rpc/list_up')
          .then(res => console.log(res.data))
          .catch(error => console.log(error))
      }
    }
  }
</script>
<style lang="css">
</style>
