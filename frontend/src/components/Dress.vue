<template>
    <div class="dress">
        <h1> This is a dress page</h1>
        <el-table class="dress-table" :data="dressData" stripe>
        <el-table-column prop="name" label="name" width="180"></el-table-column>
        <el-table-column prop="charaId" label="charaId" width="180"></el-table-column>
        <el-table-column label="select">
            <template slot-scope="scope">
                <el-checkbox v-model="scope.row.checked"></el-checkbox> 
            </template>
        </el-table-column>
        </el-table>
        <el-row>
            <el-button type="primary" size="medium" @click="PostData">确定</el-button>
        </el-row>
    </div>
</template>

<script>
// const axios = require('axios').create()
const axios = 
    process.env.VUE_APP_RESET_SERVER ==='json-mock'
    ? require('axios').create({baseURL: 'http://localhost:3000'})
    : require('axios').create()
export default {
    data(){
        return {
            dressData: []
        }
    },
    methods: {
        updateDressData: async function (){
            const response = await axios.get('/api/dress')
            this.dressData = response.data
        },
        PostData: async function (){
            let test = {"streth": [{"name": "123", "charaId": "234"}, {"name": "234", "charaId": "345"}]}
            await axios.post('/api/dress', test)
            .then(res=>{
                console.log('res=>', res)
            })
        }
    },
    mounted(){
        this.updateDressData();
    }
}
</script>

<style scoped>
.dress-table{
    width: 80%;
    margin: auto;
}
</style>