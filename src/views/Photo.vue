<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="图片"></Search>
    <Photo-List :imgs="imgs"></PhotoList>
  </section>
  <Top></Top>
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
        position: absolute;
        top: 72px;
        right: 0;
        z-index: 999;

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
  import Search from 'Search'
  import PhotoList from 'PhotoList'
  import Top from 'Top'
  import $ from 'jquery'

  export default {
    data () {
      return {
        placeholder: 'hi ! 想找到什么图片',
        page: 1,
        imgs: [],
        url: 'https://pixabay.com/api/?key=2831718-1f9b7c1b490ec182487b38a60&lang=zh&image_type=photo&page='
      }
    },
    components: {
      Navbar,
      Search,
      PhotoList,
      Top
    },
    ready () {
      const that = this
      $.get(this.url + this.page, function (data) {
        that.imgs = data.hits
      })
      var loading = false
      $(document).scroll(function () {
        const img = that.imgs
        if ($(window).scrollTop() + $(window).height() >= $(document).height() && that.imgs.length >= 1) {
          if (loading === false) {
            loading = true
            that.page += 1
            const photolist = []
            $.get(that.url + that.page, function (data) {
              for (var j = 0; j < data.hits.length; j++) {
                photolist.push(data.hits[j])
              }
              that.imgs = img.concat(photolist)
            })
            loading = false
          }
        }
      })
    }
  }
</script>
