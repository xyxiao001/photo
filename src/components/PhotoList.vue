<template>
  <div class="waterfall">
    <div class="show-photo">
      <div class="d-photo" v-for="img in imgs">
        <img v-bind:src="img.urls.small">
        <a v-link="{ name: this.$route.name + 'Detail', params: {id: img.id }}">{{img.title}}</a>
      </div>
    </div>
    <div class="show-more">
      <a><i class="fa fa-spinner" aria-hidden="true"></i>加载中..</a>
    </div>
  </div>
</template>

<style  lang="scss">
  .waterfall {
    padding-right: 20px;
    padding-left: 20px;
  }

  .d-photo {
    display: inline-block;
    width: 18%;
    height: 180px;
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
      top: -180px;
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
    margin-top: 50px;
    text-align: center;

    a {
      display: inline-block;
      width: 120px;
      height: 30px;
      color: black;
      margin: auto;
      padding: 2px;
      border: 1px solid black;
      border-radius: 5px;

      i {
        animation: start 0.3s infinite;
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


  @media screen and (max-width: 1060px)  {
    .waterfall {
      width: 100%;
      padding: 0;
      margin: auto;

      .d-photo {
        width: 30%;
      }
    }
  }

  @media screen and (max-width: 620px)  {
    .waterfall {
      .d-photo {
        width: 45%;
      }
    }
  }

  @media screen and (max-width: 420px)  {
    .waterfall {
      .d-photo {
        width: 95%;
      }
    }
  }
</style>

<script>
  export default {
    props: ['imgs']
  }
</script>
