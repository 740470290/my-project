import Vue from 'vue'
import Router from 'vue-router'
import HomeContainer from '../components/tabbar/HomeContainer'
import MemberContainer from '../components/tabbar/MemberContainer'
import SearchContainer from '../components/tabbar/SearchContainer'
import ShopcarContainer from '../components/tabbar/ShopcarContainer'
import NewsList from '../components/news/NewsList'
import NewsInfo from '../components/news/NewsInfo'
import PhotoList from '../components/photos/PhotoList'
import PhotoInfo from '../components/photos/PhotoInfo'
import GoodsList from '../components/goods/GoodsList'
import GoodsInfo from '../components/goods/GoodsInfo'
import GoodsDesc from '../components/goods/GoodsDesc'
import GoodsComment from '../components/goods/GoodsComment'
// 监听路由是前进还是后退
// Router.prototype.goBack = function () {
//   this.isBack = true
//   window.history.go(-1)
// }
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/home',
      component: HomeContainer
    },
    {
      path: '/member',
      component: MemberContainer
    },
    {
      path: '/shopcar',
      component: ShopcarContainer
    },
    {
      path: '/search',
      component: SearchContainer
    },
    {
      path: '/home/newslist',
      component: NewsList
    },
    {
      path: '/home/newslist/:id',
      component: NewsInfo
    },
    {
      path: '/home/photolist',
      component: PhotoList
    },
    {
      path: '/home/photolist/:id',
      component: PhotoInfo
    },
    {
      path: '/home/GoodsList',
      component: GoodsList
    },
    {
      path: '/home/GoodsList/:id',
      component: GoodsInfo
    },
    {
      name: 'goodsdesc',
      path: '/home/goodslist/:id/GoodsDesc',
      component: GoodsDesc
    },
    {
      name: 'goodscomment',
      path: '/home/goodslist/:id/GoodsComment',
      component: GoodsComment
    }
  ],
  linkActiveClass: 'mui-active'
})
