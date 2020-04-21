import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Home from './components/Home.vue'
import About from './components/About.vue'
import Data from './components/Data.vue'
import './plugins/element.js'
import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false

Vue.use(VueRouter)
let router = new VueRouter({
  routes:[
    {path: '/', component: Home},
    {path: '/about', component: About},
    {path: '/data', component: Data},
  ]
});

new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app')

// new Vue({
//   el: '#app',
//   router: router,
//   render: c => c(App)
// })