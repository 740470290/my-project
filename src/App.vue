<template>
  <div class="app-container">
    <mt-header fixed title="Vue项目"></mt-header>
    <transition :name="transitionName">
      <router-view></router-view>
    </transition>
    <nav class="mui-bar mui-bar-tab">
        <router-link class="mui-tab-item-lib" to="/home">
          <span class="mui-icon mui-icon-home"></span>
          <span class="mui-tab-label">首页</span>
        </router-link>
        <router-link class="mui-tab-item-lib" to="/member">
          <span class="mui-icon mui-icon-contact"></span>
          <span class="mui-tab-label">会员</span>
        </router-link>
        <router-link class="mui-tab-item-lib" to="/shopcar">
          <span class="mui-icon mui-icon-extra mui-icon-extra-cart"><span class="mui-badge">0</span></span>
          <span class="mui-tab-label">购物车</span>
        </router-link>
        <router-link class="mui-tab-item-lib" to="/search">
          <span class="mui-icon mui-icon-search"></span>
          <span class="mui-tab-label">搜索</span>
        </router-link>
  </nav>
  </div>
</template>
<script>
// import Hello from './components/Hello'
// import {Toast} from 'mint-ui'
// import HelloWorld from './components/HelloWorld'
export default {
  components: {
  },
  data () {
    return {
      transitionName: ''
    }
  },
  methods: {
  },
  watch: {
    '$route.path': function (newVal, oldVal) {
      var list = ['/home', '/member', '/shopcar', '/search']
      console.log(newVal + '----' + oldVal)
      if (newVal.includes(oldVal)) {
        this.transitionName = 'left'
      } else if (list.indexOf(newVal) > list.indexOf(oldVal) && list.indexOf(oldVal) !== -1) {
        this.transitionName = 'left'
      } else {
        this.transitionName = 'right'
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.mint-header{
  z-index: 99;
}
.app-container{
  padding-top: 40px;
  padding-bottom: 50px;
  overflow-x: hidden;
}
.left-enter{
  opacity: 0;
  transform: translateX(100%);
}
.left-leave-to{
  opacity: 0;
  transform: translateX(-100%);
  position: absolute;
}
.right-enter{
  opacity: 0;
  transform: translateX(-100%);
}
.right-leave-to{
  opacity: 0;
  transform: translateX(100%);
  position: absolute;
}
.left-enter-active,
.left-leave-active,
.right-enter-active,
.right-leave-active{
  transition: all 0.5s ease;
}
.mui-bar-tab .mui-tab-item-lib.mui-active {
    color: #007aff;
}
.mui-bar-tab .mui-tab-item-lib .mui-icon {
  top: 3px;
  width: 24px;
  height: 24px;
  padding-top: 0;
  padding-bottom: 0;
}
.mui-bar-tab .mui-tab-item-lib {
  display: table-cell;
  overflow: hidden;
  width: 1%;
  height: 50px;
  text-align: center;
  vertical-align: middle;
  white-space: nowrap;
  text-overflow: ellipsis;
  color: #929292;
}
.mui-bar-tab .mui-tab-item-lib .mui-icon ~ .mui-tab-label {
    font-size: 11px;
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
