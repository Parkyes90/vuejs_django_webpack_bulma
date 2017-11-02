<template>
  <div class="container is-fluid">
    <index-header-title></index-header-title>
    <index-header></index-header>
    <index-main></index-main>
    <index-footer></index-footer>

  </div>
</template>

<script>
  import Header from '../header/Header'
  import HeaderTitle from '../header/HeaderTitle'
  import Footer from '../footer/Footer'
  import Main from '../main/Main'
  export default {
    name: 'HelloWorld',
    components: {
      indexHeader: Header,
      indexHeaderTitle: HeaderTitle,
      indexFooter: Footer,
      indexMain: Main
    }
  }
</script>


