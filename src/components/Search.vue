<template>
  <div class="searchDiv">
    <section class="search">
      <div class="icon">
        <i class="fa fa-search fa-2x" v-on:click="startSearch"></i>
      </div>
      <div class="searchBar">
        <input
          type="text"
          v-model="input"
          :placeholder="placeholder">
        <i class="fa fa-times fa-2x"></i>
      </div>
      <div class="select">
        <div class="select-box">
          <span>{{choose}}<i class="fa fa-chevron-down"></i></span>
        </div>
      </div>
    </section>
    <section class="option">
      <ul class="show-item">
        <li class="hide">
          <a><i class="fa fa-check"></i>图片</a>
        </li>
        <li class="hide">
          <a><i class="fa fa-check"></i>表情包</a>
        </li>
        <li class="hide">
          <a><i class="fa fa-check"></i>视频</a>
        </li>
        <li class="hide">
          <a><i class="fa fa-check"></i>图标</a>
        </li>
      </ul>
    </section>
  </div>
</template>

<style lang="scss">
  .search {
    width: 900px;
    height: 72px;
    top: 150px;
    position: relative;
    background-color: white;
    margin: auto;
    overflow: hidden;
    transition: all 0.3s ease-out;
    opacity: 0.9;

    .icon {
      display: inline-block;
      width: 10%;
      height: 100%;
      position: relative;
      left: 0;
      top: 0;
      float: left;

      i {
        padding-left: 20%;
        padding-top: 20px;
        opacity: 0.8;
        cursor: pointer;
      }
    }
    .searchBar {
      display: inline-block;
      position: relative;
      width: 70%;
      height: 100%;
      top: 0;
      float: left;

      input {
        width: 90%;
        height: 100%;
        border: 0;
        font-size: 25px;
        outline: inherit;
        z-index: 1;
      }

      i {
        position: relative;
        cursor: pointer;
        top: 5px;
        opacity: 0.8;
        display: none;
      }
    }

    .select {
      display: inline-block;
      position: relative;
      width: 20%;
      height: 100%;
      top: 0;
      float: left;
      cursor: pointer;

      .select-box {
        margin-top: 15px;
        margin-bottom: 15px;
        height: 40px;
        border-left: 1px solid gray;
        padding-left: 30%;
        padding-top: 5px;
        font-size: 20px;

        i {
          padding-left: 10px;
        }
      }

      .select-box:hover i {
        color: #02a388;
      }

    }
  }



  .option {
    margin: auto;
    width: 900px;
    height: 0px;
    display: block;
    position: relative;
    top: 150px;
    transition: all 0.3s ease-out;
    opacity: 0.9;
    overflow: hidden;
    z-index: 9999;

    ul.show-item {
      width: 20%;
      height: 100%;
      margin-left: 80%;
      padding-left: 0;
      background-color: white;
      overflow: hidden;
      transition: all 0.5s ease-out;

      li {
        margin: auto;
        width: 90%;
        height: 50px;

         a {
           display: inline-block;
           width: 100%;
           height: 50px;
           font-size: 20px;
           padding-top: 10%;
           padding-left: 30%;
           color: black;
         }

         a:hover {
            color: #02a388;
         }

         i {
           padding-right: 10px;
           color: #02a388;
         }
      }
    }
  }
</style>

<script>
  import $ from 'jquery'
  export default {
    data () {
      return {
        input: ''
      }
    },
    props: ['placeholder', 'choose'],
    watch: {
      input () {
        if (this.input.length > 0) {
          $('.searchBar i').show()
        } else {
          $('.searchBar i').hide()
        }
      },
      choose () {
        switch (this.choose) {
          case '图片':
            this.placeholder = 'hi ! 想找到什么图片'
            break
          case '表情包':
            this.placeholder = '搞笑的表情包给我来一打！！ ☺'
            break
          case '视频':
            this.placeholder = '搜什么视频呢 (*@ο@*) 哇～'
            break
          case '图标':
            this.placeholder = '什么图标呢  O(∩_∩)O~~'
            break
        }
      }
    },
    methods: {
      startSearch () {
        if (this.input !== '') {
          console.log('开始搜索...')
          console.log(this.input)
        }
      }
    },
    ready () {
      const that = this
      $('.searchBar input').focus(function () {
        $('.search').addClass('focus')
      }).blur(function () {
        $('.search').removeClass('focus')
      }).keydown(function (event) {
        if (event.keyCode === 13) {
          that.startSearch()
        }
      })

      $('.searchBar i').click(function () {
        that.input = ''
        $(this).hide()
      })

      // 右边的选择
      $('.select').click(function () {
        if ($('.option').height() > 0) {
          $('.option').height('0')
          $(this).find('i').removeClass('fa-chevron-up').addClass('fa-chevron-down')
        } else {
          $(this).find('i').removeClass('fa-chevron-down').addClass('fa-chevron-up')
          $('.option').height('230px')
        }
      })

      $('.show-item>li').click(function () {
        $(this).removeClass('hide')
        .siblings().addClass('hide')
        $('.select').find('i').removeClass('fa-chevron-up').addClass('fa-chevron-down')
        that.choose = $(this).children('a').text()
        $('.option').height('0')
      })

      // 默认选中
      var li = document.querySelectorAll('.show-item li a')
      for (var i = 0; i < li.length; i++) {
        if (li[i].text === that.choose) {
          li[i].parentNode.setAttribute('class', '')
        }
      }
    }
  }
</script>
