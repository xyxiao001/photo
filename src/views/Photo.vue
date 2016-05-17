<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="图片"></Search>
    <WaterFall></Waterfall>
  </section>
  <foot></foot>
</template>

<style lang="scss">
  section.page-content {
    .searchDiv {
      position: relative;
      width: 100%;

      .search {
        width: 100%;
        top: 0;
      }

      .option {
        width: 20%;
        float: right;
        z-index: 999;
        top: 0;

        ul {
          float: right;
          width: 100%;
        }
      }
    }

  }
</style>

<script>
  // 导入模块
  import Navbar from 'Navbar'
  import Foot from 'Footer'
  import Search from 'Search'
  import Waterfall from 'Waterfall'

  export default {
    data () {
      return {
        placeholder: 'hi ! 想找到什么图片'
      }
    },
    components: {
      Navbar,
      Foot,
      Search,
      Waterfall
    }
  }
</script>
