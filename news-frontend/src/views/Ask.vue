<template>
  <section>
    <div class="container">
      <div class="box" id="content">
        <h1 class="title">Ask HN</h1>
        <hr class="hr">
        <ListItem v-for="post in posts"
                  :key="post.id"
                  :title="post.title"
                  :link="post.url"
                  :score="post.score"
                  :user="post.by"
                  :comment_link="`https://news.ycombinator.com/item?id=${post.id}`"
                  :comment_count="post.descendants"
        />
      </div>
    </div>
  </section>
</template>
<style lang="stylus">
  #content {
    margin-left: 10px
    margin-right: 10px
  }
</style>
<script>
import axios from 'axios'
import ListItem from '../components/ListItem'

export default {
  components: { ListItem },
  data () {
    return {
      posts: []
    }
  },
  async created () {
    try {
      let response = await axios.get(`https://hacker-news.firebaseio.com/v0/askstories.json`)
      response.data.slice(0, 20).map(async post => {
        try {
          let postData = await axios.get(`https://hacker-news.firebaseio.com/v0/item/${post}.json`)
          this.posts.push(postData.data)
        } catch (err) {
          console.log('Another thing happened', err)
        }
      })
    } catch (err) {
      console.log('Something happened', err)
    }
  }
}
</script>
