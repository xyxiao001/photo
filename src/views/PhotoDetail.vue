<template>
  <Navbar></Navbar>
  <section class="page-content detail">
    <Search :placeholder="placeholder" choose="图片"></Search>
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <div class="imgBox">
            <img src="../assets/photo1.jpg"></img>
          </div>
        </div>
        <div class="col-md-4">
          <button class="btn btn-primary" v-on:click="down">下载</button>
        </div>
      </div>
    </div>
    <iframe class="down" v-bind:src="src"></iframe>
  </section>
  <Foot></Foot>
</template>

<style lang="scss">
  section.detail {
    .imgBox {
      width: auto;

      img {
        padding: 50px;
      }
    }

    .btn-primary {
      margin-top: 200px;
    }

    .down {
      display: none;
    }
  }
</style>

<script>
  // 导入模块
  import Navbar from 'Navbar'
  import Search from 'Search'
  import Photo from 'PhotoShow'
  import Foot from 'Footer'

  import img from '../assets/photo1.jpg'
  export default {
    data () {
      return {
        placeholder: 'hi ! 想找到什么图片',
        src: '#'
      }
    },
    components: {
      Navbar,
      Search,
      Photo,
      Foot
    },
    methods: {
      down () {
        const that = this
        setTimeout(function () {
          that.src = img
        }, 1000)
      }
    }
  }
</script>
