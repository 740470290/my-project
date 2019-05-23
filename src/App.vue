<template>
  <div class="app-container">
    <mt-header fixed title="Vue项目">
      <router-link v-show=!isIndex to="" slot="left">
      <mt-button icon="back" @click="back">返回</mt-button>
      </router-link>
    </mt-header>
    <transition :name="transitionName">
      <router-view></router-view>
    </transition>
    <nav v-show=isIndex class="mui-bar mui-bar-tab">
        <router-link class="mui-tab-item-lib" to="/home">
          <span class="mui-icon mui-icon-home"></span>
          <span class="mui-tab-label">首页</span>
        </router-link>
        <router-link class="mui-tab-item-lib" to="/member">
          <span class="mui-icon mui-icon-contact"></span>
          <span class="mui-tab-label">会员</span>
        </router-link>
        <router-link class="mui-tab-item-lib" to="/shopcar">
          <span class="mui-icon mui-icon-extra mui-icon-extra-cart"><span class="mui-badge" id="badge">{{$store.getters.getAllCount}}</span></span>
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
export default {
  components: {
  },
  data () {
    return {
      transitionName: '',
      isIndex: true
    }
  },
  methods: {
    back () {
      history.go(-1)
    }
  },
  watch: {
    '$route.path': function (newVal, oldVal) {
      const list = ['/home', '/member', '/shopcar', '/search']
      console.log(newVal + '----' + oldVal)
      if (list.indexOf(newVal) === -1) {
        this.isIndex = false
      } else {
        this.isIndex = true
      }
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
.mint-button-text{
  position: relative;
  top: 2.1px;
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
