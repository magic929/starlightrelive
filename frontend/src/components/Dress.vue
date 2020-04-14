<template>
    <div class="dress">
        <h1> This is a dress page</h1>
        <el-table class="dress-table" :data="dressData" stripe>
        <el-table-column prop="name" label="name" width="180"></el-table-column>
        <el-table-column prop="charaId" label="charaId" width="180"></el-table-column>
        </el-table>
    </div>
</template>

<script>
const axios = require('axios').create()
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