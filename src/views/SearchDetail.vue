<template>
  <Navbar></Navbar>
  <section class="page-content searchDetail">
    <Search :placeholder="placeholder" choose="图片"></Search>
    <div class="loading">
      <p class="loadingSearch"><i class="fa fa-repeat fa-3x" aria-hidden="true"></i></p>
      <p>搜索中。。。。。</p>
    </div>
    <Photo-List :imgs="imgs"></PhotoList>
  </section>
  <section class="search-more" v-show="searchMore">
    <a v-on:click="more"><i class="fa fa-spinner" aria-hidden="true"></i>点击加载更多...</a>
  </section>
  <foot></foot>
  <Top></Top>
</template>

<style lang="scss">
  section.searchDetail {
    .show-more {
      display: none;
    }
    .loading {
      position: relative;
      height: 200px;
      width: 400px;
      left : 53%;
      top : 30%;
      padding-top: 100px;
      margin-left : -200px; /*一半的高度*/
      font-size: 30px;
      text-align: center;

      .loadingSearch {
        margin-left: -50px;
        i {
          animation: search 0.3s infinite;
          padding: 5px;
          @keyframes search {
            0%   {transform: rotate(0deg);}
            25%  {transform: rotate(90deg);}
            50%  {transform: rotate(180deg);}
            75%  {transform: rotate(270deg);}
            100% {transform: rotate(360deg);}
          }
        }
      }
    }

  }
  .search-more {
    width: 100%;
    background-color: #e8eded;
    padding-bottom: 20px;

    a {
      display: block;
      width: 180px;
      height: 30px;
      color: black;
      margin: auto;
      padding: 2px;
      padding-left: 15px;
      border: 1px solid black;
      border-radius: 5px;

      i {
        animation: start 0.5s infinite;
        padding: 5px;
        @keyframes start {
          0%   {transform: rotate(0deg);}
          25%  {transform: rotate(90deg);}
          50%  {transform: rotate(180deg);}
          75%  {transform: rotate(270deg);}
          100% {transform: rotate(360deg);}
        }
      }
    }
  }
</style>

<script>
  // 导入模块
  import Navbar from 'Navbar'
  import PhotoList from 'PhotoList'
  import Top from 'Top'
  import $ from 'jquery'
  import Search from 'Search'
  import Foot from 'Footer'

  export default {
    data () {
      return {
        imgs: [],
        page: 1,
        searchMore: false,
        placeholder: '输入关键词搜索, 目前只支持英文',
        url: 'https://api.unsplash.com/photos/search?client_id=80f66654628683dc7a20a3f2b44a93f8a9f0afaa41be7c7c392c5648dc6bb035&query='
      }
    },
    components: {
      Navbar,
      PhotoList,
      Top,
      Search,
      Foot
    },
    methods: {
      searching () {
        const that = this
        const search = [].concat(this.imgs)
        this.searchMore = false
        $.get(that.url + that.$route.query.text + '&page=' + that.page, function (data) {
          for (var i = 0; i < data.length; i++) {
            search.push(data[i])
          }
          if (search.length > 0) {
            that.imgs = search
            $('.loading').html('成功, 关键词:' + that.$route.query.text)
            if (search.length >= 10 * that.page) {
              that.searchMore = true
            }
          } else {
            that.imgs = search
            $('.loading').html('失败, 关键词:' + that.$route.query.text)
          }
        })
      },
      more () {
        this.page += 1
        this.searching()
      }
    },
    route: {
      data () {
        this.imgs = []
        this.page = 1
        this.searching()
      }
    }
  }
</script>
