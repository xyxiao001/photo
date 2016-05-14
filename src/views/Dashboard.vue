<template>
  <Navbar></Navbar>
  <section class="show">
    <Search v-bind:choose="choose"></Search>
  </section>
</template>

<style lang="scss">
  body {
    margin: 0;
    padding: 0;
    min-width: 1024px;
    min-height: 1200px;

    .show {
      width: auto;
      height: 440px;
      background-size: cover;
      background-image: url(/show.jpg?ecfa96c);
      background-color: black;
    }

    li {
      list-style: none;
    }

    a {
      cursor: pointer;
    }

    a:hover {
      text-decoration: none;
    }

    .focus {
      opacity: 1!important;
      box-shadow: 0 0 10px white;
    }

    .hide>a>i {
      visibility: hidden;
    }
}
</style>

<script>
  // 导入模块
  import Navbar from 'Navbar'
  import $ from 'jquery'
  import Search from 'Search'

  export default {
    data () {
      return {
        choose: '图片'
      }
    },
    components: {
      Navbar,
      Search
    },
    ready () {
      // 绑定this
      const that = this

      // 右边的选择
      $('.select').click(function () {
        if ($('.show-item').height() > 0) {
          $('.show-item').height('0')
          $(this).find('i').removeClass('fa-chevron-up').addClass('fa-chevron-down')
        } else {
          $(this).find('i').removeClass('fa-chevron-down').addClass('fa-chevron-up')
          $('.show-item').height('200px')
        }
      })

      $('.show-item>li').click(function () {
        $(this).removeClass('hide')
        .siblings().addClass('hide')
        $('.select').find('i').removeClass('fa-chevron-up').addClass('fa-chevron-down')
        that.choose = $(this).children('a').text()
        $('.show-item').height('0')
      })

      // 滚动条事件
      $(document).scroll(function () {
        if (window.scrollY < 120) {
          $('.search').css('top', window.scrollY + 100)
          $('.search').width('900px')
          $('.option').css('top', window.scrollY + 100)
          $('.option').width('900px')
        } else if (window.scrollY <= 302) {
          $('.search').width('900px')
          $('.option').width('900px')
        } else if (window.scrollY > 315) {
          $('.search').width('100%')
          $('.search').css('top', window.scrollY - 100)
          $('.option').width('100%')
          $('.option').css('top', window.scrollY - 100)
        }
      })
    }
  }
</script>
