<template>
  <a class="to-top" v-on:click="top">
    <i class="fa fa-hand-o-up fa-2x"></i>
  </a>
</template>

<style lang="scss">
  .to-top {
    position: fixed;
    display: none;
    top: 80%;
    right: 0;
    z-index: 9999;
    width: 40px;
    height: 40px;

    i {
      color: black;
    }
  }

  a.to-top:hover i{
    color: red;
  }
</style>

<script>
  import $ from 'jquery'

  export default {
    methods: {
      top () {
        $('body').animate({
          scrollTop: '0px'
        }, 1000)
      }
    },
    ready () {
      $(document).scroll(function () {
        if (window.scrollY > 1000) {
          $('.to-top').show()
        } else {
          $('.to-top').hide()
        }
      })
    }
  }
</script>
