<template>
  <div class="goodsinfo-container">
    <div class="mui-card">
      <div class="mui-card-content-inner">
        <mt-swipe :auto="6000" :speed="1000">
          <mt-swipe-item v-for="item in lunbotu" :key="item.src"><img :src="item.src" alt=""></mt-swipe-item>
        </mt-swipe>
      </div>
      <div class="mui-card-content">
      </div>
    </div>
    <div class="mui-card">
      <div class="mui-card-header">页眉</div>
      <div class="mui-card-content">
        <div class="mui-card-content-inner">445645
          包含页眉页脚的卡片，页眉常用来显示面板标题，页脚用来显示额外信息或支持的操作（比如点赞、评论等）
        </div>
      </div>
    </div>
    <div class="mui-card">
      <div class="mui-card-header">页眉</div>
      <div class="mui-card-content">
        <div class="mui-card-content-inner">
          包含页眉页脚的卡片，页眉常用来显示面板标题，页脚用来显示额外信息或支持的操作（比如点赞、评论等）
        </div>
      </div>
      <div class="mui-card-footer">页脚</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GoodsInfo',
  data () {
    return {
      lunbotu: [
        {
          src: 'http://demo.dtcms.net/upload/201504/20/thumb_201504200046589514.jpg'
        },
        {
          src: 'http://demo.dtcms.net/upload/201504/20/thumb_201504200046594439.jpg'
        }
      ]
    }
  }
}
</script>

<style scoped>
  .goodsinfo-container {
    background-color: #eee;
    /*overflow: hidden;*/
  }
  .mui-card-content-inner{
    height: 400px;
  }
  .mint-swipe-items-wrap{
    width: 100%;
  }
  .mint-swipe-items-wrap img{
    margin: 0 auto;
  }
</style>
