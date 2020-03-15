<template>
<el-table v-loading="sup_this.loading" :data="sup_this.data" size="small" show-summary border style="width: 100%">
    <el-table-column prop="name" label="类型" width="180">
    </el-table-column>
    <el-table-column prop="sum_net" label="重量">
    </el-table-column>
</el-table>
</template>

<script>
export default {
    props: {
        sup_this: {
            type: Object,
            required: true
        }
    },
    data() {
        return {}
    },
    methods: {
    }
};
</script>
