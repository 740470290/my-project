<template>
  <div class="shopcar-container">
    <div class="goods-list">
      <div class="mui-card" v-for="item in goodslist" :key="item.id">
        <div class="mui-card-content">
          <div class="mui-card-content-inner">
            <mt-switch></mt-switch>
            <img :src="item.thumb_path" alt="">
            <div class="info">
              <h4>{{item.title}}</h4>
              <div>
                <span class="price">¥{{item.sell_price}}</span>
                <div class="mui-numbox" data-numbox-min='1' data-numbox-max='goodsinfo.stock_quantity'>
                  <button class="mui-btn mui-btn-numbox-minus" type="button">-</button>
                  <input readonly ref="numbox" id="test" class="mui-input-numbox" type="number" value="1"/>
                  <button class="mui-btn mui-btn-numbox-plus" type="button">+</button>
                </div>
                <a href="#">删除{{$store.getters.getGoodsCount[item.id]}}</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="mui-card">
      <div class="mui-card-content">
        <div class="mui-card-content-inner">
          这是一个最简单的卡片视图控件；卡片视图常用来显示完整独立的一段信息，比如一篇文章的预览图、作者信息、点赞数量等
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import mui from '../../lib/mui/js/mui.min.js'

export default {
  data () {
    return {
      goodslist: [
        {
          cou: 1,
          id: 87,
          title: '华为（HUAWEI）荣耀6Plus 16G双4G版',
          sell_price: 2195,
          thumb_path: 'http://demo.dtcms.net/upload/201504/20/thumb_201504200046589514.jpg'
        },
        {
          cou: 1,
          id: 88,
          title: '苹果Apple iPhone 6 Plus 16G 4G手机（联通三网版）',
          sell_price: 5780,
          thumb_path: 'http://demo.dtcms.net/upload/201504/20/thumb_201504200059017695.jpg'
        },
        {
          cou: 1,
          id: 89,
          title: '小米（Mi）小米Note 16G双网通版',
          sell_price: 2199,
          thumb_path: 'http://demo.dtcms.net/upload/201504/20/thumb_201504200119256512.jpg'
        }
      ]
    }
  },
  methods: {
    getGoodsList () {

    }
  },
  name: 'memberContainer',
  mounted () {
    mui('.mui-numbox').numbox()
  }
}
</script>

<style scoped>
  .shopcar-container {
    background-color: #eee;
    overflow: hidden;
  }

  .price {
    color: red;
    font-weight: bold;
  }

  .mui-card-content-inner {
    display: flex;
    align-items: center;
  }

  img {
    width: 60px;
    height: 60px;
  }
</style>
