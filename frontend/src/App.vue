<template>
  <div id="app">
    <div>
      <h1> 欢迎来到スタリラ</h1>
    </div>
    <el-menu :default-active="activeIndex" mode="horizontal" router>
      <el-menu-item index="home" :route="{path:'home'}">主页</el-menu-item>
      <el-menu-item index="dress" :route="{path:'dress'}">少女索引</el-menu-item>
      <el-menu-item index="data" :route="{path:'data'}">数据收集</el-menu-item>
      <el-menu-item index="strength" :route="{name: 'home'}">强度预测</el-menu-item>
      <el-menu-item>
        <a href="https://element.eleme.io" target="_blank">Link</a>
      </el-menu-item>
    </el-menu> 
    <router-view v-if="isRouterAlive"/>
  </div>
</template>

<script>
export default {
  name: 'app',
  provide(){
    return {
        reload: this.reload
      }
  },
  data () {
    return{
      isRouterAlive: true,
      activeIndex: this.$route.name
    }
  },
  methods: {
    reload() {
      this.isRouterAlive = false,
      this.$nextTick(() => (this.isRouterAlive = true))
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
}
a {
  text-decoration: none;
}
</style>
