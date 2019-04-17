<template>
<div>
  <div id="slider" class="mui-slider">
      <div id="sliderSegmentedControl" class="mui-scroll-wrapper mui-slider-indicator mui-segmented-control mui-segmented-control-inverted">
        <div class="mui-scroll">
          <a :class="['mui-control-item', item.id ==1 ? 'mui-active' : '']" v-for="item in cates" :key="item.id" @click="getPhotoListByCateId(item.id)">
            {{item.title}}
          </a>
        </div>
      </div>
    </div>
  <ul class="photo-list">
    <router-link v-for="item in list" :key="item.id" :to="'/home/photolist/'+item.id" tag="li">
      <img v-lazy="item.img_url">
      <div class="info">
        <h4 class="info-title">{{item.title}}</h4>
        <div class="info-body">{{item.zhaiyao}}</div>
      </div>
    </router-link>
  </ul>
</div>
</template>

<script>
import mui from '../../lib/mui/js/mui.min.js'
export default {
  name: 'PhotoList',
  data () {
    return {
      cates: [],
      list: []
    }
  },
  created () {
    this.getAllCategory()
    this.getPhotoListByCateId(1)
  },
  mounted () {
    mui('.mui-scroll-wrapper').scroll({
      deceleration: 0.0005
    })
  },
  methods: {
    getAllCategory () {
      this.$http.get('api/getimgcategory').then(res => {
        this.cates = res.body.message
      })
    },
    getPhotoListByCateId (cateId) {
      this.$http.get('api/getimages/' + cateId).then(res => {
        this.list = res.body.message
      })
    }
  }
}
</script>

<style scoped>
* { touch-action: pan-y;}
img[lazy="loading"]{
  width: 40px;
  height: 300px;
  margin: auto;
}
.photo-list{
    list-style: none;
    margin: 0;
    padding: 10px;
}
.photo-list li{
    background: #ccc;
    text-align: center;
    margin-bottom: 10px;
    box-shadow: 0 0 9px #999;
    position: relative
}
.photo-list li img{
    width: 100%;
    vertical-align: middle;
}
.info{
    color: white;
    text-align: left;
    position: absolute;
    padding: 5px;
    bottom: 0;
    background-color: rgba(0,0,0,0.4);
    max-height: 90px;
}
</style>
