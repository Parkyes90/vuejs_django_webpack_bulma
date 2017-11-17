<template>
  <div class="columns">
    <div class="column">
      <div class="tile is-ancestor">
        <div class="tile is-vertical">
          <div class="tile">
            <div class="tile is-parent is-vertical">
              <div class="card tile is-child" v-for="post in posts" v-if="post.idx % 3 == 1">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img v-bind:src="'http://127.0.0.1:8003/media/' + post.image">
                  </figure>
                </div>
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img v-bind:src="'http://127.0.0.1:8003/media/' + post.image">
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-4">{{ post.title }}</p>
                      <p class="subtitle is-6">@{{ post.user }}</p>
                    </div>
                  </div>
                  <div class="content">
                    {{ post.content }}
                    <a href="#">#css</a> <a href="#">#responsive</a>
                    <br>
                    <time datetime="2016-1-1">{{ post.create_date }}</time>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="column">
      <div class="tile is-ancestor">
        <div class="tile is-vertical">
          <div class="tile">
            <div class="tile is-parent is-vertical">
              <div class="card tile is-child" v-for="post in posts" v-if="post.idx % 3 == 2">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img v-bind:src="'http://127.0.0.1:8003/media/' + post.image">
                  </figure>
                </div>
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img v-bind:src="'http://127.0.0.1:8003/media/' + post.image">
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-4">{{ post.title }}</p>
                      <p class="subtitle is-6">@{{ post.user }}</p>
                    </div>
                  </div>
                  <div class="content">
                    {{ post.content }}
                    <a href="#">#css</a> <a href="#">#responsive</a>
                    <br>
                    <time datetime="2016-1-1">{{ post.create_date }}</time>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="column">
      <div class="tile is-ancestor">
        <div class="tile is-vertical">
          <div class="tile">
            <div class="tile is-parent is-vertical">
              <div class="card tile is-child" v-for="post in posts" v-if="post.idx % 3 == 0">
                <div class="card-image">
                  <figure class="image is-4by3">
                    <img v-bind:src="'http://127.0.0.1:8003/media/' + post.image">
                  </figure>
                </div>
                <div class="card-content">
                  <div class="media">
                    <div class="media-left">
                      <figure class="image is-48x48">
                        <img v-bind:src="'http://127.0.0.1:8003/media/' + post.image">
                      </figure>
                    </div>
                    <div class="media-content">
                      <p class="title is-4">{{ post.title }}</p>
                      <p class="subtitle is-6">@{{ post.user }}</p>
                    </div>
                  </div>
                  <div class="content">
                    {{ post.content }}
                    <a href="#">#css</a> <a href="#">#responsive</a>
                    <br>
                    <time datetime="2016-1-1">{{ post.create_date }}</time>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
  axios.defaults.xsrfCookieName = 'csrftoken'
  export default {
    data () {
      return {
        posts: []
      }
    },
    created () {
      axios.get('http://127.0.0.1:8003/rpc/list_up')
        .then(res => {
          this.posts = res.data.data
          let j = 1
          for (let post of this.posts) {
            post.idx = j
            j++
          }
        })
        .catch(error => console.log(error))
    }
  }
</script>
<style lang="scss" scoped>
  @import '../assets/scss/Main';
</style>
