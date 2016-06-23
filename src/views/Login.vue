<template>
  <div class="login">
    <section class="loginBg"></section>
    <div class="loginBox">
      <section class="title">
        <a class="logo" v-link="{name: 'Dashboard'}">
          图片聚集地
          <span>免费图片！</span>
        </a>
      </section>
      <section>
        <form>
          <div class="form-group">
            <input
              type="username"
              class="form-control"
              v-model="username"
              v-on:focus="clear"
              placeholder="用户名 测试 xxy">
          </div>
          <div class="form-group">
            <input
              type="password"
              class="form-control"
              v-model="password"
              v-on:focus="clear"
              placeholder="密码 测试 1234">
          </div>
          <button type="submit" class="btn btn-primary" v-on:click="login">登录</button>
          <p class="error">{{error}}</p>
        </form>
      </section>
    </div>
  </div>
</template>

<style lang="scss">
  .login {

    .loginBg {
      background-image: url('../assets/login.jpg');
      background-position: center center;
      background-repeat: no-repeat;
      background-size: cover;
      left: 0;
      padding-right: 40px;
      position: fixed;
      text-align: right;
      width: 100%;
      height: 100%;
    }

    .loginBox {
      position: absolute;
      height: 350px;
      width: 400px;
      left : 50%;
      top : 20%;
      margin-left : -200px; /*一半的高度*/
      background: white;
      box-shadow:2px 3px 11px #333333;

      .title {
        width: 100%;
        height: 80px;
        padding: 10px;
        background-color: black;

        a {
          display: block;
          margin: 0 auto;
          position: relative;
          font-size: 26px;
          color: white;
          text-align: center;
          transition: all 0.5s;

          span {
            margin: auto;
            display: block;
            font-size: 15px;
            color: white;
            opacity: 0.9;
            transition: all 0.5s;
          }
          &:hover {
            color: #02a388;
          }
        }
      }

      form {
        margin: auto;
        width: 80%;
        margin-top: 50px;

        button {
          display: inline-block;
          width: 100%;
        }
      }
    }
  }

  .error {
    text-align: center;
    color: red;
    font-size: 13px;
    padding-top: 10px;
  }

  /*手把手写兼容手机端*/
  @media screen and (max-width: 440px){
    .login {
      .loginBox {
        position: absolute;
        height: 320px;
        width: 80%;
        top: 70px;
        left: 230px;
        background: white;
        box-shadow:2px 3px 11px #333333;
      }
    }
  }
</style>

<script>
  // 导入模块
  import { setToken } from '../token'

  export default {
    data () {
      return {
        username: '',
        password: '',
        error: ''
      }
    },
    methods: {
      login (event) {
        event.preventDefault()
        if (this.username !== 'xxy' || this.password !== '1234') {
          this.error = '用户名,密码错误'
        } else {
          setToken('xyxiao')
          this.$router.go('/')
        }
      },
      clear () {
        this.error = ''
      }
    }
  }
</script>
