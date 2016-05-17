<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search placeholder="什么图标呢  O(∩_∩)O~~" choose="图标"></Search>
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
    components: {
      Navbar,
      Foot,
      Search
    }
  }
</script>
