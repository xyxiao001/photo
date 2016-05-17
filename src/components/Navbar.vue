<template>
  <section class="menu">
    <nav class="left">
      <ul>
        <li v-for="menu in menus">
          <a v-link="{name: menu.link}">{{menu.name}}</a>
        </li>
      </ul>
    </nav>
    <section id="logo">
      <a class="logo" v-link="{name: 'Dashboard', exact: true}">摄影爱好者 <span>图片聚集地！</span></a>
    </section>
    <nav class="right">
      <ul>
        <li>
          <a>注册</a>
        </li>
        <li>
          <a>登陆</a>
        </li>
      </ul>
    </nav>
  </section>
</template>

<style lang="scss">
   section.menu {
     width: 100%;
     height: 85px;
     background-color: #0c0d0d;
     color: #b4b9b9;
     transition: all 0.3s ease-out;
     overflow: hidden;

     nav a.active {
       color: #84e900;
     }

     nav.left {
       padding: 0;
       width: 50%;
       float: left;
     }

     nav.right {
       padding: 0;
       width: 50%;
       float: right;

       ul li {
         float: right;

         a {
           color: white;
           opacity: 0.9;
         }

         a:hover {
           color: #02a388;
         }
       }
     }

     li {
       display: inline-block;
       font-size: 1rem;
       line-height: 85px;
       padding: 0 30px;
       white-space: nowrap;

       a {
         transition: all 0.3s ease-out;
         color: #b4b9b9;
       }

       a:hover {
         color: #02a388;
       }
     }

     #logo {
       height: 0;
       margin: 0 auto;
       position: absolute;
       text-align: center;
       width: 100%;
       min-width: 1024px;

       a {
         display: block;
         width: 200px;
         height: 58px;
         margin: 0 auto;
         position: relative;
         font-size: 26px;
         color: white;
         padding-top: 10px;
         transition: all 0.5s;

         span {
           margin: auto;
           display: block;
           font-size: 15px;
           color: white;
           opacity: 0.9;
           transition: all 0.5s;
         }
       }
       a.logo:hover {
         opacity: 0.5;
       }

       a.logo:hover span{
         opacity: 0.4;
       }
     }
   }
</style>


<script>
  export default {
    data () {
      return {
        menus: [
          {
            name: '照片',
            link: 'Photo'
          },
          {
            name: '表情包',
            link: 'Biao'
          },
          {
            name: '视频',
            link: 'Video'
          },
          {
            name: '图标',
            link: 'Icon'
          }
        ]
      }
    }
  }
</script>
