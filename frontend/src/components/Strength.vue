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
                <el-col :span="1" v-for="(item, index) of ss" :key="item.id" :offset="index > 0 ? 1 : 0">
                    <el-card :body-style="{ padding: '0px'}" shadow="hover" style="width: 120px;height: 160px;">
                        <img :src="item.url">
                        <div>
                            <span>{{item.name}}</span>
                            <!-- <span>test</span> -->
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
export default {
    name: 'home',
    data() {
        return{
            ss:[
                {"url": "https://image.boom-app.wiki/wiki/5b681c9ab1b4b87b781b5c69/stagegirl/s/140.jpg?w=120", "id": "1050006", "name": "アマテラス"},
                {"url": "https://image.boom-app.wiki/wiki/5b681c9ab1b4b87b781b5c69/stagegirl/s/166.jpg?w=120", "id": "4020008", "name": "ファントム"},
                 {"url": "https://image.boom-app.wiki/wiki/5b681c9ab1b4b87b781b5c69/stagegirl/s/166.jpg?w=120", "id": "4020008", "name": "ファントム"}
            ]
        }
    }
}
</script>