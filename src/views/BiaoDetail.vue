<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="图片"></Search>
  </section>
  <Foot></Foot>
</template>

<style lang="scss">
</style>

<script>
  // 导入模块
  import Navbar from 'Navbar'
  import Search from 'Search'
  import Photo from 'PhotoShow'
  import Foot from 'Footer'
  export default {
    data () {
      return {
        placeholder: 'hi ! 想找到什么图片'
      }
    },
    components: {
      Navbar,
      Search,
      Photo,
      Foot
    }
  }
</script>
