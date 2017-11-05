<template>
    <div>
        <appHeader></appHeader>
        <app-header-title></app-header-title>
        <div class="container">
          <router-view></router-view>
        </div>
        <appFooter></appFooter>
    </div>

</template>

<script>
  import Header from './header/Header'
  import HeaderTitle from './header/HeaderTitle'
  import Footer from './footer/Footer'

  export default {
    components: {
      appHeader: Header,
      appHeaderTitle: HeaderTitle,
      appFooter: Footer
    }
  }
</script>
