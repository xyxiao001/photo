<template>
  <div class="photo-show">
    <a class="photo-item">
      <div class="photo-img">
        <img v-bind:src="photo.url">
      </div>
      <h5>{{photo.title}}</h5>
    </a>
    <a class="photo-id">
      <i class="fa fa-camera"></i>
      <span>{{photo.id}}</span>
    </a>
  </div>
</template>

<style lang="scss">
  .photo-show {
    width: 100%;
    height: 305px;
    background-color: white;
    margin-bottom: 20px;
    padding: 8px;
    text-align: center;

    a.photo-item {
      width: 100%;
      height: 305px;
      display: block;
      z-index: 1;
    }

    h5 {
      color: black;
      padding: 8px;
    }

    .photo-img{
      height: 85%;
      overflow: hidden;
      transition: all 0.25s ease-out;

      img {
        width: 100%;
        height: 100%;
        transition: all 0.25s ease-out;
        transform: scale(1.1);
        background-size: cover;
      }
    }

    a.photo-id {
      display: none;
      position: absolute;
      top: 8px;
      left: 22px;
      z-index: 99;
      color: gray;
      min-width: 100px;
      height: 30px;
      background-color: white;
      padding-top: 3px;

      i {
        padding-left: 4px;
        padding-right: 4px;
      }
    }

    a.photo-id:hover span{
      color: #02a388;
    }

    .photo-item:hover  img{
      width: 96%;
      height: 96%;
      opacity: 0.8;
    }
  }
</style>

<script>
  import $ from 'jquery'

  export default {
    props: ['photo'],
    ready () {
      $('.photo-show').mouseover(function () {
        $(this).children('a.photo-id').show()
      }).mouseout(function () {
        $(this).children('a.photo-id').hide()
      })
    }
  }
</script>
