<template>
  <Navbar></Navbar>
  <section class="show">
    <Search :placeholder="placeholder" choose="图片"></Search>
  </section>
  <section class="page-content">
    <div class="title">
      <h1>没有你找不到的资源, 如果有, 那也没办法!!</h1>
    </div>
    <div class="see">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <div class="row">
              <div class="col-md-6">
                <Photo v-bind:photo="photo1"></Photo>
              </div>
              <div class="col-md-6">
                <Photo v-bind:photo="photo2"></Photo>
              </div>
            </div>
            <div class="row">
              <div class="col-md-6">
                <Photo v-bind:photo="photo3"></Photo>
              </div>
              <div class="col-md-6">
                <Photo v-bind:photo="photo4"></Photo>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="video">
              <Photo v-bind:photo="videoImage"></Photo>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="all-categories">
            <h3>全部类别</h2>
          </div>
          <div class="col-md-3">
            <ul>
              <li v-for="category in category1">
                <a>{{category.name}}</a>
              </li>
            </ul>
          </div>
          <div class="col-md-3">
            <ul>
              <li v-for="category in category2">
                <a>{{category.name}}</a>
              </li>
            </ul>
          </div>
          <div class="col-md-3">
            <ul>
              <li v-for="category in category3">
                <a>{{category.name}}</a>
              </li>
            </ul>
          </div>
          <div class="col-md-3">
            <ul>
              <li v-for="category in category4">
                <a>{{category.name}}</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="slogan">
      <div class="container">
        <div class="col-md-6">
          <img src="../assets/slogan.jpg">
        </div>
        <div class="col-md-6">
          <div class="slogan-text">
            <h4>爱上摄影, 寻找更美的你</h4>
            <p>
              按下快门的瞬间，不是你留住了时间，而是时间记住了你
            </p>
            <p>
              此刻，你是最美的
            </p>
            <p>
              哥拍的不只风景，还有心情
            </p>
            <p>
              回头看看来时路，你会发现途中的脚印总让人感动
            </p>
            <p>
              某些时光，值得留存
            </p>
            <p>
              时光流逝留在这，美丽青春留给你
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="video">
      <div class="container">
        <h4>观看免费视频</h4>
        <div class="row">
          <div class="col-md-4" v-for="video in videos">
            <Video v-bind:video="video"></Video>
          </div>
        </div>
      </div>
    </div>
    <Foot></Foot>
  </section>
</template>

<style lang="scss">
  body {
    margin: 0;
    padding: 0;
    min-width: 1024px;

    .show {
      width: auto;
      height: 440px;
      background-size: cover;
      background-image: url('../assets/show.jpg');
      background-color: black;
    }

    li {
      list-style: none;
    }

    a {
      cursor: pointer;
    }

    a:hover, a:focus, a:link {
      text-decoration: none;
    }

    .focus {
      opacity: 1!important;
      box-shadow: 0 0 10px white;
    }

    .hide>a>i {
      visibility: hidden;
    }

    .page-content {
      background-color: #e8eded;
      background-attachment: fixed;
      min-height: 600px;

      .title {
        height: 150px;
        text-align: center;
         h1 {
            padding-top: 50px;
         }
      }

      .see {
        min-width: 1024px;
        min-height: 650px;
        text-align: center;

        .video .photo-show {
          height: 630px;

          .photo-item {
            height: 630px;

            .photo-img {
              height: 93%;
            }
          }
        }

        .all-categories {
          margin-top: 30px;

          h3 {
            margin-bottom: 40px;
          }
        }
        ul li {
          height: 25px;

          a {
            color: #028a71;
            padding: 5px;
            font-weight: bold;
          }

          a:hover {
            opacity: 0.8;
          }
        }
      }

      .slogan {
        min-width: 1024px;
        height: 404px;
        background-color: #dce1e1;

        img {
          width: 100%;
          height: 100%;
          margin-top: 40px;
        }

        .slogan-text {
          margin-top: 40px;

          h4 {
            text-align: center;
            margin-bottom: 40px;
            font-weight: bold;
          }

          p {
            padding: 0;
            padding-left: 60px;
          }

        }
      }

      .video {
        background: #e8eded;
        height: 250px;

        h4 {
          margin-top: 20px;
        }
      }
    }
}
</style>

<script>
  // 暂时先试用保存在本地的图片
  import One from '../assets/photo1.jpg'
  import Two from '../assets/photo2.jpg'
  import Three from '../assets/photo3.jpg'
  import Four from '../assets/photo4.jpg'
  import VideoJpg from '../assets/video.jpg'

  // 导入模块
  import Navbar from 'Navbar'
  import $ from 'jquery'
  import Search from 'Search'
  import Photo from 'PhotoShow'
  import Foot from 'Footer'
  import Video from 'VideoShow'

  export default {
    data () {
      return {
        placeholder: '找到完美的照片, 视频和更多…',
        photo1: {
          url: One,
          id: '#877245',
          title: '体验VR'
        },
        photo2: {
          url: Two,
          id: '#877246',
          title: '基本背景和纹理'
        },
        photo3: {
          url: Three,
          id: '#877247',
          title: '童话'
        },
        photo4: {
          url: Four,
          id: '#877248',
          title: '使用ipad学习'
        },
        videoImage: {
          url: VideoJpg,
          id: '#877249',
          title: '观看4K极致清晰视频'
        },
        category1: [
          {id: 1, name: '表情包', url: ''},
          {id: 2, name: '壁纸', url: ''},
          {id: 3, name: '图标', url: ''},
          {id: 4, name: '风景', url: ''},
          {id: 5, name: '人文景观', url: ''}
        ],
        category2: [
          {id: 1, name: '家人', url: ''},
          {id: 2, name: '自然', url: ''},
          {id: 3, name: '动物照片', url: ''},
          {id: 4, name: '老式', url: ''},
          {id: 5, name: '背景', url: ''}
        ],
        category3: [
          {id: 1, name: '食品', url: ''},
          {id: 2, name: '体育', url: ''},
          {id: 3, name: '娱乐', url: ''},
          {id: 4, name: '动物', url: ''},
          {id: 5, name: '美女视频', url: ''}
        ],
        category4: [
          {id: 1, name: '科技视频', url: ''},
          {id: 2, name: '健身视频', url: ''},
          {id: 3, name: '旅游视频', url: ''},
          {id: 4, name: '学习视频', url: ''},
          {id: 5, name: '搞笑视频', url: ''}
        ],
        videos: [
          {
            id: 1,
            url: 'http://i.istockimg.com/video_passthrough/73017509/151/73017509.mp4',
            img: 'http://i.istockimg.com/file_thumbview_approve/73017509/11/stock-video-73017509-machine-gear-wheel.jpg'
          },
          {
            id: 2,
            url: 'http://i.istockimg.com/video_passthrough/89634773/151/89634773.mp4',
            img: 'http://i.istockimg.com/file_thumbview_approve/89634773/11/stock-video-89634773-road-to-moon.jpg'
          },
          {
            id: 3,
            url: 'http://i.istockimg.com/video_passthrough/81034259/151/81034259.mp4',
            img: 'http://i.istockimg.com/file_thumbview_approve/81034259/11/stock-video-81034259-chemical-elements.jpg'
          }
        ]
      }
    },
    components: {
      Navbar,
      Search,
      Photo,
      Foot,
      Video
    },
    ready () {
      const that = this
      // 滚动条事件
      $(document).scroll(function () {
        if (that.$route.name === 'Dashboard') {
          if (window.scrollY < 120) {
            $('.search').css('top', window.scrollY + 150)
            $('.search').width('900px')
            $('.option').css('top', window.scrollY + 150)
            $('.option').width('900px')
          } else if (window.scrollY <= 310) {
            $('.search').width('900px')
            $('.option').width('900px')
          } else if (window.scrollY < 520) {
            $('.search').width('100%')
            $('.search').css('top', window.scrollY - 90)
            $('.option').width('100%')
            $('.option').css('top', window.scrollY - 90)
          }
        }
      })
    }
  }
</script>
