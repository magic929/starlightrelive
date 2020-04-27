<template>
    <div class="data">
        <h1> This is a dress page</h1>
        <el-table class="dress-table" :data="dressData" @selection-change="handleSelectionChange" stripe>
        <el-table-column prob="img_url" label="img" width="180">
            <template slot-scope="scope">
                <img :src="scope.row.img_url" width="60" height="60"/>
            </template>
        </el-table-column>
        <el-table-column prop="id" lable="id" width="180" v-if="show"></el-table-column>
        <el-table-column prop="name" label="name" width="180"></el-table-column>
        <el-table-column prop="charaId" label="charaId" width="180"></el-table-column>
        <el-table-column label="select" type="selection" width="180">
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
    inject: ['reload'],
    data(){
        return {
            dressData: [],
            multipleSelection: []
        }
    },
    methods: {
        updateDressData: async function (){
            const response = await axios.get('/api/dress')
            this.dressData = response.data
        },
        PostData: async function (){
            let result = []
            for(var v of this.multipleSelection){
                result.push(v.id)
            }
            await axios.post('/api/dress', {"strength": result})
            .then(()=>{
                this.reload()
            })
        },
        handleSelectionChange(val){
            this.multipleSelection = val
            console.log(this.multipleSelection)
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