<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="视频"></Search>
  </section>
  <foot></foot>
</template>

<style lang="scss">
  section.page-content {
  }
</style>

<script>
  // 导入模块
  import Navbar from 'Navbar'
  import Foot from 'Footer'
  import Search from 'Search'

  export default {
    data () {
      return {
        placeholder: '搜什么视频呢 (*@ο@*) 哇～'
      }
    },
    components: {
      Navbar,
      Foot,
      Search
    }
  }
</script>
