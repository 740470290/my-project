<template>
  <div class="goodsinfo-container">
    <div class="mui-card">
      <div class="mui-card-content-inner lun">
        <mt-swipe :auto="6000" :speed="1000">
          <mt-swipe-item v-for="item in lunbotu" :key="item.src"><img :src="item.src" alt=""></mt-swipe-item>
        </mt-swipe>
      </div>
      <div class="mui-card-content">
      </div>
    </div>
    <div class="mui-card">
      <div class="mui-card-header">{{goodsinfo.title}}</div>
      <div class="mui-card-content">
        <div class="mui-card-content-inner">
          <p class="price">
            市场价:
            <del>¥{{goodsinfo.market_price}}</del>&nbsp;&nbsp;销售价:<span class="now_price">¥{{goodsinfo.sell_price}}</span>
          </p>
          <div>购买数量:
            <div class="mui-numbox" data-numbox-min='1' data-numbox-max='9'>
              <button class="mui-btn mui-btn-numbox-minus" type="button">-</button>
              <input id="test" class="mui-input-numbox" type="number" value="1"/>
              <button class="mui-btn mui-btn-numbox-plus" type="button">+</button>
            </div>
          </div>
          <p>
            <mt-button type="primary" size="small">立即购买</mt-button>
            <mt-button type="danger" size="small">加入购物车</mt-button>
          </p>
        </div>
      </div>
    </div>
    <div class="mui-card">
      <div class="mui-card-header">商品参数</div>
      <div class="mui-card-content">
        <div class="mui-card-content-inner">
          <p>商品货号:{{goodsinfo.goods_no}}</p>
          <p>库存情况:{{goodsinfo.stock_quantity}}</p>
          <p>上架时间:{{goodsinfo.add_time}}</p>
        </div>
      </div>
      <div class="mui-card-footer">
        <mt-button type="primary" size="large" plain @click="goDesc(id)">图文介绍</mt-button>
        <mt-button type="danger" size="large" plain @click="goComment(id)">商品评论</mt-button>
      </div>
    </div>
  </div>
</template>

<script>
import mui from '../../lib/mui/js/mui.min.js'

export default {
  name: 'GoodsInfo',
  mounted () {
    mui('.mui-numbox').numbox()
  },
  data () {
    return {
      lunbotu: [
        {
          src: 'http://demo.dtcms.net/upload/201504/20/thumb_201504200046589514.jpg'
        },
        {
          src: 'http://demo.dtcms.net/upload/201504/20/thumb_201504200046594439.jpg'
        }
      ],
      goodsinfo: {
        id: 87,
        title: '小米（Mi）小米Note 16G双网通版',
        add_time: '2015-04-19T17:19:30.000Z',
        goods_no: 'SD2932214404',
        stock_quantity: 60,
        market_price: 2699,
        sell_price: 2199
      }
    }
  },
  methods: {
    goDesc (id) {
      this.$router.push({name: '/home/goodsdesc', params: {id}})
    },
    goComment (id) {
      this.$router.push({name: '/home/goodscomment', params: {id}})
    }
  }
}
</script>

<style scoped>
  .goodsinfo-container {
    background-color: #eee;
    /*overflow: hidden;*/
  }

  .lun {
    height: 400px;
  }

  .mint-swipe-item {
    text-align: center;
  }

  .now_price {
    color: red;
  }

  .mui-card-footer {
    display: block;
  }

  .mui-card-footer button {
    margin: 15px 0;
  }
</style>
