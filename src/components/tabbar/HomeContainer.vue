<template>
  <div>
    <mt-swipe :auto="6000" :speed="1000">
      <mt-swipe-item><img src="../../images/1.jpg" alt=""></mt-swipe-item>
      <mt-swipe-item><img src="../../images/2.jpg" alt=""></mt-swipe-item>
      <mt-swipe-item><img src="../../images/3.jpg" alt=""></mt-swipe-item>
    </mt-swipe>
    <ul class="mui-table-view mui-grid-view mui-grid-9">
        <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3">
          <router-link to="/home/newslist">
                <img src="../../images/menu1.png" alt="">
                <div class="mui-media-body">新闻资讯</div></router-link></li>
        <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><router-link to="/home/photolist">
                <img src="../../images/menu2.png" alt="">
                <div class="mui-media-body">图片分享</div></router-link></li>
        <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
                <img src="../../images/menu3.png" alt="">
                <div class="mui-media-body">商品购买</div></a></li>
        <br>
        <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
                <img src="../../images/menu4.png" alt="">
                <div class="mui-media-body">留言反馈</div></a></li>
        <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
                <img src="../../images/menu5.png" alt="">
                <div class="mui-media-body">视频专区</div></a></li>
        <li class="mui-table-view-cell mui-media mui-col-xs-4 mui-col-sm-3"><a href="#">
                <img src="../../images/menu6.png" alt="">
                <div class="mui-media-body">联系我们</div></a></li>
    </ul>
</div>
</template>

<script>
export default {
  name: 'home'
}
</script>

<style scoped>
.mint-swipe{
  height: 200px;
}
.mint-swipe img{
  width: 100%;
  height: 200px;
}
.mui-grid-view.mui-grid-9{
  background-color: #fff;
  border: none;
}
.mui-grid-view.mui-grid-9 img{
  width: 60px;
  height: 60px;
}
.mui-grid-view.mui-grid-9 .mui-table-view-cell{
  border: none;
  width: 33%;
}
</style>
