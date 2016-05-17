<template>
  <div class="waterfall">
    <div class="show-photo">
      <div class="d-photo" v-for="img in imgs">
        <img v-bind:src="img.src">
        <a>{{img.title}}</a>
      </div>
    </div>
    <div class="show-more">
      <a v-on:click="showMore">展示更多</a>
    </div>
  </div>
</template>

<style  lang="scss">
  .waterfall {
    padding-right: 20px;
    padding-left: 20px;
  }

  @media screen and (max-width: 1250px)  {
    .waterfall {
      padding-left: 0;
    }
  }

  .d-photo {
    display: inline-block;
    height: 230px;
    max-width: 23%;
    margin: 8px 10px;
    cursor: pointer;
    overflow: hidden;
    transition: all 0.3s ease-out;

    img {
      width: 100%;
      height: 100%;
    }

    a {
      position: relative;
      top: -230px;
      display: inline-block;
      height: 230px;
      width: 100%;
      opacity: 0;
      color: black;
      transition: all 0.3s ease-out;

    }
  }

  .d-photo:hover img{
    opacity: 0.3;
  }

  .d-photo:hover a {
    opacity: 1;
    padding-left: 50px;
  }

  .show-more {
    width: 100%;
    height: 50px;
    text-align: center;

    a {
      display: inline-block;
      width: 80px;
      height: 30px;
      color: black;
      margin: auto;
      padding: 2px;
      border: 1px solid black;
      border-radius: 5px;
    }

    a:hover {
      color: #028a71;
    }
  }
</style>

<script>
  export default {
    props: ['imgs'],
    methods: {
      showMore () {
        for (var i = 0; i < 10; i++) {
          var f = parseInt(Math.random() * this.imgs.length - 1)
          var div = document.createElement('div')
          div.className = 'd-photo'
          var img = document.createElement('img')
          img.src = this.imgs[f].src
          var a = document.createElement('a')
          a.innerHTML = this.imgs[f].title
          div.appendChild(img)
          div.appendChild(a)
          document.getElementsByClassName('show-photo')[0].appendChild(div)
        }
      }
    }
  }
</script>
