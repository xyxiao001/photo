<template>
  <Navbar></Navbar>
  <section class="show">
    <section class="search">
      <div class="icon">
        <i class="fa fa-search fa-2x"></i>
      </div>
      <div class="searchBar">
        <input type="text" name="name" value="">
      </div>
    </section>
  </section>
</template>

<style lang="scss">
  body {
    margin: 0;
    padding: 0;
    min-width: 1024px;
    min-height: 1000px;

    li {
      list-style: none;
    }

    a {
      cursor: pointer;
    }

    a:hover {
      text-decoration: none;
    }

    .show {
      width: auto;
      height: 400px;
      background-size: cover;
      background-image: url(/show.jpg);

      .search {
        width: 900px;
        height: 72px;
        top: 100px;
        position: relative;
        background-color: white;
        margin: auto;

        .icon {
          display: inline-block;
          width: 20%;
          height: 100%;
          float: left;

          i {
            padding-left: 20px;
            padding-top: 5px;
            opacity: 0.8;
          }
        }
      }

      .searchBar {
        display: inline-block;
        width: 60%;
        height: 100%;
        float: left;

      }

    }
  }
</style>

<script>
  // 导入模块
  import Navbar from 'Navbar'
  import $ from 'jquery'

  export default {
    data () {
      return {
      }
    },
    components: {
      Navbar
    },
    ready () {
      console.log($)
    }
  }
</script>
