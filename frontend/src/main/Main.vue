<template>
  <div>
    <div v-for="post in posts">
      {{ post }}
    </div>
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
    data () {
      return {
        posts: []
      }
    },
    created () {
      axios.get('/rpc/list_up')
        .then(res => {
          this.posts = res.data.data
          let j = 1
          for (let post of this.posts) {
            post.idx = j
            j++
          }
        })
        .catch(error => console.log(error))
    }
  }
</script>
<style lang="css">
</style>
