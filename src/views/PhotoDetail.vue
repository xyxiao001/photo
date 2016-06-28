<template>
  <div class="imgBox">
    <div class="loading">
      <i class="fa fa-spinner" aria-hidden="true"></i>
      <span>全速加载中。。。。。</span>
    </div>
    <div class="photos">
      <nav>
        <a v-link="{name: 'Dashboard', exact: true}">
          <img src="../assets/logo.png" alt="首页" />
        </a>
      </nav>
    </div>
    <div class="down">
      <nav>
        <a v-bind:href="downloads" target="_blank">
          下载
        </a>
      </nav>
    </div>
  </div>
</template>

<style lang="scss">
  div.imgBox {
    width: 100%;

    .photos {
      width: 100%;
      background-position: center center;
      background-repeat: no-repeat;
      background-size: cover;
      left: 0;
      padding-right: 40px;
      position: fixed;
      text-align: right;
      width: 100%;
      height: 100%;

      nav {
        position: fixed;
        width: 100%;
        height: 75px;
        padding-top: 10px;
        background: rgba(255, 255, 255, 0.3);

        img {
          display: inline-block;
          position: absolute;
          left: 50%;
          margin-left: -25px;
          width: 60px;
          height: 60px;
          transition: all 0.5s ease-out;
        }

        img:hover {
          width: 50px;
          height: 50px;
        }
      }
    }

    .loading {
      position: absolute;
      width: 600px;
      left : 50%;
      margin-top: 200px;
      margin-left: -200px;

      span {
        padding-left: 20px;
        font-size: 50px;
      }

      i {
        float: left;
        padding-top: 10px;
        font-size: 50px;
        animation: start 0.5s infinite ease-in-out;
        @keyframes start {
          0%   {transform: rotate(0deg);}
          20%  {transform: rotate(60deg);}
          40%  {transform: rotate(120deg);}
          60%  {transform: rotate(180deg);}
          80% {transform: rotate(240deg);}
          100% {transform: rotate(300deg);}
        }
      }
    }

    .down {
      nav {
        position: fixed;
        top: 100%;
        margin-top: -75px;
        width: 100%;
        height: 75px;
        padding-top: 10px;
        background: rgba(255, 255, 255, 0.3);

        a {
          display: block;
          width: 100px;
          margin: auto;
          font-size: 20px;
          text-align: center;
          margin-top: 10px;
          padding: 5px;
          border: 1px solid black;
          color: black;
          transition: all 0.5s ease;
        }

        a:hover {
          border: 1px solid red;
        }
      }
    }
  }
</style>

<script>
  // 导入模块
  import $ from 'jquery'

  export default {
    data () {
      return {
        placeholder: 'hi ! 想找到什么图片',
        downloads: ''
      }
    },
    route: {
      data () {
        const that = this
        $.get('https://api.unsplash.com/photos/' + that.$route.params.id + '?client_id=fc1ad074b94abad2fa784ab7740425e91b4ec8db73473371fa36aaa88e866658', function (data) {
          $('.loading').show()
          $('.photos').css('background-image', 'url(' + data.urls.regular + ')')
          that.downloads = data.links.download
        })
      }
    }
  }
</script>
