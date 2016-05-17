<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="图片"></Search>
  </section>
  <foot></foot>
</template>

<style lang="scss">
  section.page-content {
    .searchDiv {
      width: 100%;
      height: 322px;

      .search {
        width: 100%;
        top: 0;
      }

      .option {
        width: 100%;
        top: 0;
      }
    }
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
        placeholder: 'hi ! 想找到什么图片'
      }
    },
    components: {
      Navbar,
      Foot,
      Search
    }
  }
</script>
