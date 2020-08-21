<template>
    <div class="strength">
        <div>
            <h1> This is a strength page</h1>
        </div>
        <div>
            <h1> 当月卡强度预测 </h1>
        </div>
        <div>
            <h1>投票数据强度</h1>
            <h2 style="text-align:left">ss</h2>
            <el-row>
                <el-col :span="1" v-for="(item, index) of level.ss" :key="item.id" :offset="index > 0 ? 1 : 0">
                    <el-card :body-style="{ padding: '0px'}" shadow="hover">
                        <img :src="item.url" class="image">
                        <div>
                            <span>{{item.name}}</span>
                            <!-- <span>test</span> -->
                        </div>
                    </el-card>
                </el-col>
            </el-row>
            <h2 style="text-align:left">s</h2>
            <el-row>
                <el-col :span="1" v-for="(item, index) of level.s" :key="item.id" :offset="index > 0 ? 1 : 0">
                    <el-card :body-style="{ padding: '0px'}" shadow="hover" class="box-card">
                        <img :src="item.url" class="image">
                        <div>
                            <span>{{item.name}}</span>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
            <h2 style="text-align:left">a</h2>
            <el-row>
                <el-col :span="1" v-for="(item, index) of level.a" :key="item.id" :offset="index > 0 ? 1 : 0">
                    <el-card :body-style="{ padding: '0px'}" shadow="hover">
                        <img :src="item.url">
                        <div>
                            <span>{{item.name}}</span>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
            <h2 style="text-align:left">b</h2>
            <el-row>
                <el-col :span="1" v-for="(item, index) of level.b" :key="item.id" :offset="index > 0 ? 1 : 0">
                    <el-card :body-style="{ padding: '0px'}" shadow="hover" style="width: 120px;height: 160px;">
                        <img :src="item.url">
                        <div>
                            <span>{{item.name}}</span>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<style>
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .image {
    width: 100%;
    height: 100%;
    display: block;
  }
   .box-card {
    width: 150%;
  }
</style>

<script>
const axios = process.env.VUE_APP_RESET_SERVER ==='json-mock'
    ? require('axios').create({baseURL: 'http://localhost:3000'})
    : require('axios').create()
export default {
    data() {
        return{
            level: {}
        }
    },
    methods:{
        updateLevel: async function(){
            const response = await axios.get('/api/level');
            this.level = response.data
        }
    },
    mounted(){
        this.updateLevel();
    }
}
</script>