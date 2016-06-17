<template>
  <section class="menu">
    <section id="logo">
      <a class="logo" v-link="{name: 'Dashboard', exact: true}">摄影爱好者 <span>图片聚集地！</span></a>
      <i class="fa fa-bars fa-2x" aria-hidden="true" v-on:click="drop"></i>
    </section>
    <div class="drop">
      <nav class="left">
        <ul>
          <li v-for="menu in menus">
            <a v-link="{name: menu.link}">{{menu.name}}</a>
          </li>
        </ul>
      </nav>
      <nav class="right" v-if="this.login === true">
        <ul>
          <li>
            <a  v-link="{name: 'Login'}">登陆</a>
          </li>
          <li>
            <a>注册</a>
          </li>
        </ul>
      </nav>
      <nav class="right" v-if="this.login === false">
        <ul>
          <li>
            <a>好男孩</a>
          </li>
          <li>
            <a v-on:click="logOut">退出登录</a>
          </li>
        </ul>
      </nav>
    </div>
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
       color: #84e900 !important;
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

       ul {
         float: right;

         li {
           float: left;

           a {
             color: white;
             opacity: 0.9;
           }

           a:hover {
             color: #02a388;
           }
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

       i.fa-bars {
         display: none;
       }
     }
   }

   @media screen and(max-width: 968px) {
     section.menu {
       width: 100%;
       height: auto;
       transition: all 0.3s ease-out;

       #logo {
         position: relative;
         display: block;
         width: 100%;
         height: 80px;

         a {
           width: auto;
           display: inline-block;;
           text-align: center;
         }

         i.fa-bars {
           display: inline-block;
           float: right;
           padding-top: 25px;
           padding-right: 20px;
           margin-left: -20px;
           cursor: pointer;
         }

       }

       .drop {
         position: relative;
         width: 100%;
         height: 1px;
         overflow: hidden;
         -webkit-overflow-scrolling: touch;
         transition: height 0.5s ease;
         -webkit-transform:transition3d/translateZ;

         nav.left, nav.right {
           width: 100%;
           position: relative;

           ul {
             width: 100%;
             padding: 0;
             margin: 0;

             li {
               display: block;
               width: 100%;
               height: 60px;
               padding: 0;
               line-height: 60px;

               a {
                  display: inline-block;
                  width: 100%;
                  height: 60px;
                  padding-left: 20px;
               }

               &:hover {
                 background-color: rgba(0, 0, 0, 0.5);
               }
             }
           }
         }
       }
     }
   }
</style>


<script>
  import { getToken, removeToken } from '../token'
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
        ],
        login: false,
        drops: false
      }
    },
    computed: {
      login () {
        return !getToken()
      }
    },
    methods: {
      logOut () {
        removeToken()
        this.$router.go('/login')
      },
      drop () {
        const drop = document.querySelector('.drop')
        if (this.drops) {
          this.drops = false
          drop.style.height = '1px'
        } else {
          this.drops = true
          drop.style.height = '350px'
        }
      }
    },
    ready () {
    }
  }
</script>
