<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="表情包"></Search>
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
        placeholder: '搞笑的表情包给我来一打！！ ☺'
      }
    },
    components: {
      Navbar,
      Foot,
      Search
    }
  }
</script>
