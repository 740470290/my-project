<template>
  <div class="photoinfo-container">
    <h4>{{photoinfo.title}}</h4>
    <p class="subtitle">
      <span>发表时间:{{photoinfo.add_time|dataFormat}}</span>
      <span>点击: {{photoinfo.click}}次</span>
    </p>
    <hr>
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
      photoinfo: {}
    }
  },
  components: {
    comment
  },
  created () {
    this.getPhotoInfo()
  },
  methods: {
    getPhotoInfo () {
      this.$http.get('api/getimageInfo/' + this.id).then(res => {
        this.photoinfo = res.body.message[0]
      }, red => {
        alert('加载失败')
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
