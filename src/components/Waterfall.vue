<template>
  <div class="waterfall">
    <div class="waterRow">
      <img src="../assets/photo1.jpg" alt="" />
      <img src="../assets/photo2.jpg" alt="" />
      <img src="../assets/photo1.jpg" alt="" />
      <img src="../assets/photo2.jpg" alt="" />
      <img src="../assets/photo1.jpg" alt="" />
      <img src="../assets/photo2.jpg" alt="" />
      <img src="../assets/show.jpg" alt="" />
      <img src="../assets/photo1.jpg" alt="" />
      <img src="../assets/photo2.jpg" alt="" />
      <img src="../assets/show.jpg" alt="" />
    </div>
  </div>
</template>

<style  lang="scss">
  img {
    margin: 8px;
    width: auto;
    height: 180px;
  }

  @media screen and (min-width: 1920px) {
    img {
      height: 250px;
    }
  }
</style>

<script>
  import One from '../assets/photo1.jpg'
  import Two from '../assets/photo2.jpg'
  import Three from '../assets/photo3.jpg'
  import Four from '../assets/photo4.jpg'

  export default {
    data () {
      return {
        img: [One, Two, Three, Four]
      }
    }
  }
</script>
