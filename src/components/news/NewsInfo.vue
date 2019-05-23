<template>
  <div class="newsinfo-container">
    <h3 class="title">{{newsinfo.title}}</h3>
    <p class="subtitle">
      <span>发表时间:{{newsinfo.add_time | dataFormat}}</span>
      <span>点击:{{newsinfo.click}}次</span>
    </p>
    <hr>
    <div class="content" v-html="newsinfo.content">
    </div>
    <!--<comment :id="this.id"></comment>-->
    <comment :id=1></comment>
  </div>
</template>

<script>
import comment from '../subcomponents/comment'
export default {
  name: 'NewsInfo',
  data () {
    return {
      id: this.$route.params.id,
      newsinfo: {}
    }
  },
  created () {
    this.getNewsInfo()
  },
  methods: {
    getNewsInfo () {
      this.$http.get('api/getnew/' + this.id).then(res => {
        this.newsinfo = res.body.message[0]
      })
    }
  },
  components: {
    comment
  }
}
</script>

<style scoped>
.newsinfo-container{
  padding: 0 4px;
}
.newsinfo-container .title{
  text-align: center;
  margin: 15px 0;
  color: red;
}
.newsinfo-container .subtitle{
  color: #226aff;
  display: flex;
  justify-content: space-between;
}
.content img{
  width: 100%;
}
</style>
