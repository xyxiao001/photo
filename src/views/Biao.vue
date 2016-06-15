<template>
  <Navbar></Navbar>
  <section class="page-content">
    <Search :placeholder="placeholder" choose="表情包"></Search>
    <WaterFall :imgs="biaos"></Waterfall>
  </section>
  <Top></Top>
</template>

<script>
  // 导入图片
  import biao1 from '../assets/biao/biao1.jpg'
  import biao2 from '../assets/biao/biao2.jpg'
  import biao3 from '../assets/biao/biao3.jpg'
  import biao4 from '../assets/biao/biao4.png'
  import biao5 from '../assets/biao/biao5.jpg'
  import biao6 from '../assets/biao/biao6.jpg'
  import biao7 from '../assets/biao/biao7.gif'
  import biao8 from '../assets/biao/biao8.jpg'
  import biao9 from '../assets/biao/biao9.gif'
  import biao10 from '../assets/biao/biao10.gif'
  import biao11 from '../assets/biao/biao11.gif'
  import biao12 from '../assets/biao/biao12.gif'
  import biao13 from '../assets/biao/biao13.jpg'
  import biao14 from '../assets/biao/biao14.jpg'
  import biao15 from '../assets/biao/biao15.jpg'
  import biao16 from '../assets/biao/biao16.jpg'
  import biao17 from '../assets/biao/biao17.jpg'
  import biao18 from '../assets/biao/biao18.png'
  import biao19 from '../assets/biao/biao19.gif'
  import biao20 from '../assets/biao/biao20.gif'
  import biao21 from '../assets/biao/biao21.jpg'

  // 导入模块
  import Navbar from 'Navbar'
  import Foot from 'Footer'
  import Search from 'Search'
  import Waterfall from 'Waterfall'
  import Top from 'Top'
  import $ from 'jquery'

  export default {
    data () {
      return {
        placeholder: '搞笑的表情包给我来一打！！ ☺',
        biaos: [
          {src: biao1, title: '小冷 你太天真了'},
          {src: biao2, title: ''},
          {src: biao3, title: ''},
          {src: biao4, title: ''},
          {src: biao5, title: ''},
          {src: biao6, title: ''},
          {src: biao7, title: ''},
          {src: biao8, title: ''},
          {src: biao9, title: ''},
          {src: biao10, title: ''},
          {src: biao11, title: ''},
          {src: biao12, title: ''},
          {src: biao13, title: ''},
          {src: biao14, title: ''},
          {src: biao15, title: ''},
          {src: biao16, title: ''},
          {src: biao17, title: ''},
          {src: biao18, title: ''},
          {src: biao19, title: ''},
          {src: biao20, title: ''},
          {src: biao21, title: ''}
        ]
      }
    },
    components: {
      Navbar,
      Foot,
      Search,
      Waterfall,
      Top
    },
    ready () {
      const that = this
      var loading = false
      $(document).scroll(function () {
        const biao = that.biaos
        if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
          if (loading === false) {
            loading = true
            setTimeout(function () {
              const arr = []
              for (var i = 0; i < 20; i++) {
                const f = parseInt(Math.random() * biao.length)
                arr.push(
                  {src: biao[f].src, title: biao[f].title}
                )
              }
              that.biaos = biao.concat(arr)
            }, 1500)
            loading = false
          }
        }
      })
    }
  }
</script>
