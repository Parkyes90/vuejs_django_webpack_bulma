<template>
<nav class="nav-center is-sticky">
  <div class="navbar-brand">
    <a class="navbar-item" href="https://bulma.io">
      <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28">
    </a>

    <a class="navbar-item is-hidden-desktop" href="https://github.com/jgthms/bulma" target="_blank">
      <span class="icon" style="color: #333;">
        <i class="fa fa-lg fa-github"></i>
      </span>
    </a>

    <a class="navbar-item is-hidden-desktop" href="https://twitter.com/jgthms" target="_blank">
      <span class="icon" style="color: #55acee;">
        <i class="fa fa-lg fa-twitter"></i>
      </span>
    </a>

    <div class="navbar-burger burger" data-target="navMenuTransparentExample">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>

  <div id="navMenuTransparentExample" class="navbar-menu">
    <div class="navbar-start">
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link  is-active" href="/documentation/overview/start/">
          국가
        </a>
        <div class="navbar-dropdown is-boxed">
          <a class="navbar-item " href="/documentation/overview/start/">
            한국
          </a>
          <a class="navbar-item " href="https://bulma.io/documentation/modifiers/syntax/">
            동남아
          </a>
          <a class="navbar-item " href="https://bulma.io/documentation/columns/basics/">
            유럽
          </a>
          <a class="navbar-item " href="https://bulma.io/documentation/layout/container/">
            북미
          </a>
          <a class="navbar-item " href="https://bulma.io/documentation/form/general/">
            남미
          </a>
          <a class="navbar-item " href="https://bulma.io/documentation/elements/box/">
            호주
          </a>
            <a class="navbar-item" href="https://bulma.io/documentation/components/breadcrumb/">
              아프리카
            </a>

          <hr class="navbar-divider">
          <div class="navbar-item">
            <div>
              <p class="is-size-6-desktop">
                <strong>모두 보기</strong>
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link " href="https://bulma.io/blog/">
          블로그
        </a>
        <div id="blogDropdown" class="navbar-dropdown is-boxed" data-style="width: 18rem;">

            <a class="navbar-item" href="/2017/10/09/roses-are-red-links-are-blue/">
              <div class="navbar-content">
                <p>
                  <small class="has-text-link">09 Oct 2017</small>
                </p>
                <p>Roses are red – Links are blue</p>
              </div>
            </a>

            <a class="navbar-item" href="/2017/08/03/list-of-tags/">
              <div class="navbar-content">
                <p>
                  <small class="has-text-link">03 Aug 2017</small>
                </p>
                <p>New feature: list of tags</p>
              </div>
            </a>

            <a class="navbar-item" href="/2017/08/01/bulma-bootstrap-comparison/">
              <div class="navbar-content">
                <p>
                  <small class="has-text-link">01 Aug 2017</small>
                </p>
                <p>Bulma / Bootstrap comparison</p>
              </div>
            </a>

          <a class="navbar-item" href="https://bulma.io/blog/">
            More posts
          </a>
          <hr class="navbar-divider">
          <div class="navbar-item">
            <div class="navbar-content">
              <div class="level is-mobile">
                <div class="level-left">
                  <div class="level-item">
                    <strong>Stay up to date!</strong>
                  </div>
                </div>
                <div class="level-right">
                  <div class="level-item">
                    <a class="button bd-is-rss is-small" href="https://bulma.io/atom.xml">
                      <span class="icon is-small">
                        <i class="fa fa-rss"></i>
                      </span>
                      <span>Subscribe</span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar-item has-dropdown is-hoverable">
        <div class="navbar-link">
          More
        </div>
        <div id="moreDropdown" class="navbar-dropdown is-boxed">
          <a class="navbar-item " href="https://bulma.io/bulma-start/">
            <p>
              <strong>Bulma start</strong>
              <br>
              <small>A tiny npm package to get started</small>
            </p>
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item " href="https://bulma.io/made-with-bulma/">
            <p>
              <strong>Made with Bulma</strong>
              <br>
              <small>The official community badge</small>
            </p>
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item " href="https://bulma.io/extensions/">
            <p>
              <strong>Extensions</strong>
              <br>
              <small>Side projects to enhance Bulma</small>
            </p>
          </a>
        </div>
      </div>
      <a class="navbar-item " href="https://bulma.io/expo/">
        <span class="bd-emoji">⭐️</span>
        자유게시판
      </a>
      <a class="navbar-item " href="https://bulma.io/love/">
        <span class="bd-emoji">❤️</span>
        추천
      </a>
    </div>

    <div class="navbar-end">
      <a class="navbar-item is-hidden-desktop-only" href="https://github.com/jgthms/bulma" target="_blank">
        <span class="icon" style="color: #333;">
          <i class="fa fa-lg fa-github"></i>
        </span>
      </a>
      <a class="navbar-item is-hidden-desktop-only" href="https://twitter.com/jgthms" target="_blank">
        <span class="icon" style="color: #55acee;">
          <i class="fa fa-lg fa-twitter"></i>
        </span>
      </a>
      <div class="navbar-item">
        <div class="field is-grouped">
          <p class="control">
            <a class="bd-tw-button button"
  data-social-network="Twitter"
  data-social-action="tweet"
  data-social-target="https://bulma.io"
  target="_blank"
  href="https://twitter.com/intent/tweet?text=Bulma: a modern CSS framework based on Flexbox&hashtags=bulmaio&url=https://bulma.io&via=jgthms">
  <span class="icon">
    <i class="fa fa-twitter"></i>
  </span>
  <span>
    Tweet
  </span>
</a>

          </p>
          <p class="control">
            <a class="button is-info" href="https://github.com/jgthms/bulma/releases/download/0.6.0/bulma-0.6.0.zip">
              <span class="icon">
                <i class="fa fa-sign-in"></i>
              </span>
              <span>Sign Up / Sign In</span>
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    // Get all "navbar-burger" elements
    var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0)

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {
      // Add a click event on each of them
      $navbarBurgers.forEach(function ($el) {
        $el.addEventListener('click', function () {
          // Get the target from the "data-target" attribute
          var target = $el.dataset.target
          var $target = document.getElementById(target)
          // Toggle the class on both the "navbar-burger" and the "navbar-menu"
          $el.classList.toggle('is-active')
          $target.classList.toggle('is-active')
        })
      })
    }
  })
</script>


<style lang="scss">
  @import '../assets/font-awesome-4.7.0/css/font-awesome.css';
  @import '../assets/scss/Header';
</style>
