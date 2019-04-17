<template>
  <div>
    <ul class="mui-table-view" v-for="item in newslist" :key="item.id">
      <li class="mui-table-view-cell mui-media">
        <router-link :to="'/home/newslist/' + item.id">
          <img class="mui-media-object mui-pull-left" :src="item.img_url">
          <div class="mui-media-body">
            {{ item.title }}
            <p class='mui-ellipsis'>
              <span>发表时间:{{item.add_time | dataFormat}}</span>
              <span>点击:{{item.click}}次</span>
            </p>
          </div>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'NewsList',
  data () {
    return {
      newslist: []
    }
  },
  created () {
    this.getNewsList()
  },
  methods: {
    getNewsList () {
      this.$http.get('api/getnewslist').then(res => {
        this.newslist = res.body.message
      }, res => {
        alert('获取新闻列表失败')
      })
    }
  }
}
</script>

<style scoped>
.mui-ellipsis{
  color: #226aff;
  display: flex;
  justify-content: space-between;
}
</style>
