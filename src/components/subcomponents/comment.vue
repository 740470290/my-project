<template>
  <div>
    <h3>发表评论</h3>
    <hr>
    <textarea placeholder="请输入评论的内容(不超过120字)" maxlength="120" v-model="msg"></textarea>
    <mt-button type="primary" size="large" @click="postComment">发表评论</mt-button>
    <div class="cmt-list">
      <div content="cmt-item" v-for="(item, i) in comments" :key="item.add_time">
        <div class="cmt-title">
          第{{i+1}}楼&nbsp;&nbsp;用户:{{item.user_name}}&nbsp;&nbsp;发表时间:{{item.add_time | dataFormat}}
        </div>
        <div class="cmt-body">
          {{item.content}}
        </div>
      </div>
    </div>
    <mt-button type="danger" size="large" plain @click="getMore">加载更多</mt-button>
  </div>
</template>

<script>
export default {
  name: 'comment',
  props: ['id'],
  data () {
    return {
      pageindex: 1,
      comments: [],
      msg: ''
    }
  },
  created () {
    this.getComments()
  },
  methods: {
    getComments () {
      this.$http.post('api/getcomments/' + this.id, {page: this.pageindex}).then(res => {
        this.comments = this.comments.concat(res.body)
      }, red => {
        alert('没有更多评论')
      })
    },
    getMore () {
      this.pageindex++
      this.getComments()
    },
    postComment () {
      if (this.msg.trim().length === 0) {
        return alert('评论不能为空')
      } else {
        this.$http.post('api/postcomment/' + this.id, {content: this.msg.trim()}).then(res => {
          this.comments = res.body
          this.pageindex = 1
          this.msg = ''
        })
      }
    }
  }
}
</script>

<style scoped>
.cmt-list{
  margin: 5px 0;
}
.cmt-title{
  line-height: 30px;
  background-color: #ccc;
}
.cmt-body{
  line-height: 35px;
  text-indent: 2em;
}
</style>
