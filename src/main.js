// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import MintUI from 'mint-ui'
// import { Header, Swipe, SwipeItem, Button } from 'mint-ui'
import 'mint-ui/lib/style.css'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App'
import router from './router'
import './lib/mui/css/mui.css'
import './lib/mui/css/icons-extra.css'
import VueResource from 'vue-resource'
import moment from 'moment'
import VuePreview from 'vue-preview'
Vue.use(VuePreview)
Vue.use(MintUI)
Vue.use(VueResource)
Vue.http.options.emulateJSON = true
Vue.filter('dataFormat', function (dataStr, pattern = 'YYYY-MM-DD HH:mm:ss') {
  return moment(dataStr).format(pattern)
})
Vue.http.options.root = 'http://172.17.14.250:5000'
// Vue.component(Header.name, Header)
// Vue.component(Swipe.name, Swipe)
// Vue.component(SwipeItem.name, SwipeItem)
// Vue.component(Button.name, Button)
Vue.config.productionTip = false
/* eslint-disable no-new */
window.onload = function () {
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })
}
