<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="图片"></Search>
    <WaterFall :imgs="imgs"></Waterfall>
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
  import Foot from 'Footer'
  import Search from 'Search'
  import Waterfall from 'Waterfall'

  import One from '../assets/photo1.jpg'
  import Two from '../assets/photo2.jpg'
  import Three from '../assets/photo3.jpg'
  import Four from '../assets/photo4.jpg'

  export default {
    data () {
      return {
        placeholder: 'hi ! 想找到什么图片',
        imgs: [
          {src: One, title: '体验VR, 炫酷的体验'},
          {
            src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_ceugbpm7bb2-SxDi3dsmcMpqusqvmAvL9QUqMWCX1RL-5qJY',
            title: '好萌，好萌的'
          },
          {
            src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXQ118ASvPuMDxDOIL9dAq5MSjx71eX0YCFsd8ijxEwpMqTooz',
            title: '这是谁 好想知道'
          },
          {src: Two, title: '纹理， 还不错哟'},
          {
            src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPmHRdfF5bMyxS6K-ZawTItxqRZyW5ery3e1rSAjFkzqkhnNz8Cw',
            title: '美丽的晚霞'
          },
          {
            src: 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS3sVVUtnTDrv0lObNUy6AG6iILM2qo4lhEr7yMkqirEQfFDh28',
            title: '埃菲尔铁塔'
          },
          {src: Three, title: '大灰狼和小红帽的故事'},
          {src: Four, title: '拿着iPad学习的'}
        ]
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
