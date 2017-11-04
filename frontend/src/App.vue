<template>
    <div>
        <Header></Header>
        <header-title></header-title>
        <div class="container">
          <router-view></router-view>
        </div>
        <Footer></Footer>
    </div>

</template>

<script>
  import Header from './header/Header'
  import HeaderTitle from './header/HeaderTitle'
  import Footer from './footer/Footer'
  import Main from './main/Main'

  export default {
    components: {
      Header: Header,
      HeaderTitle: HeaderTitle,
      Footer: Footer,
      Main: Main
    }
  }
</script>
