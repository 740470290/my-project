<template>
  <div class="photoinfo-container">
    <h4>{{photoinfo.title}}</h4>
    <p class="subtitle">
      <span>发表时间:{{photoinfo.add_time|dataFormat}}</span>
      <span>点击: {{photoinfo.click}}次</span>
    </p>
    <hr>
    <!--<img class="preview-img" v-for="(item, index) in list" :src="item.src" height="100" @click="$preview.open(index, list)" :key="item.src">-->
    <vue-preview :slides="list" @close="handleClose"></vue-preview>
    <div class="content" v-html="photoinfo.content"></div>
    <comment :id=1></comment>
  </div>
</template>

<script>
import comment from '../subcomponents/comment'
export default {
  name: 'PhotoInfo',
  data () {
    return {
      id: this.$route.params.id,
      photoinfo: {},
      list: [
        {
          src: 'https://farm6.staticflickr.com/5591/15008867125_68a8ed88cc_b.jpg',
          msrc: 'https://farm6.staticflickr.com/5591/15008867125_68a8ed88cc_m.jpg',
          alt: 'picture1',
          title: 'Image Caption 1',
          w: 600,
          h: 400
        },
        {
          src: 'https://farm4.staticflickr.com/3902/14985871946_86abb8c56f_b.jpg',
          msrc: 'https://farm4.staticflickr.com/3902/14985871946_86abb8c56f_m.jpg',
          alt: 'picture2',
          title: 'Image Caption 2',
          w: 600,
          h: 400
        }]
    }
  },
  components: {
    comment
  },
  created () {
    this.getPhotoInfo()
    // this.getThumbs()
  },
  methods: {
    handleClose () {
      console.log('close event')
    },
    getPhotoInfo () {
      this.$http.get('api/getimageInfo/' + this.id).then(res => {
        this.photoinfo = res.body.message[0]
      }, red => {
        alert('加载失败')
      })
    },
    getThumbs () {
      this.$http.get('api/getthuimages/' + this.id).then(res => {
        res.body.message.forEach(item => {
          item.w = 600
          item.h = 400
        })
        this.list = res.body.message
      })
    }
  }
}
</script>

<style scoped>
.photoinfo-container{
  padding: 5px;
}
h4{
  color: #26A2FF;
  text-align: center;
  margin: 15px 0;
}
  .subtitle{
    display: flex;
    justify-content: space-between;
  }
</style>
