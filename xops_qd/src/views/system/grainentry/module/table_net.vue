<template>
<el-table stripe="true" v-loading="sup_this.loading" :data="sup_this.data" size="small" border :summary-method="getSummaries" show-summary style="width: 100%">
    <el-table-column prop="customer_name" label="客户名" width="180">
    </el-table-column>
    <el-table-column prop="sum_net" label="总净重(斤)">
    </el-table-column>
    <el-table-column prop="sum_amount_pay" sortable label="总应付金额">
    </el-table-column>
    <el-table-column prop="sum_actual_pay" sortable label="总已付金额">
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
        getSummaries(param) {
            const {
                columns,
                data
            } = param;
            const sums = [];
            columns.forEach((column, index) => {
                if (index === 0) {
                    sums[index] = '合计';
                    return;
                }
                const values = data.map(item => Number(item[column.property]));
                if (!values.every(value => isNaN(value))) {
                    sums[index] = values.reduce((prev, curr) => {
                        const value = Number(curr);
                        if (!isNaN(value)) {
                            return prev + curr;
                        } else {
                            return prev;
                        }
                    }, 0);
                    if (index == 1) {
                        sums[index] += ' 斤';
                    }
                    else{
                        sums[index] += ' 元';
                    }
                } else {
                    sums[index] = 'N/A';
                }
            });

            return sums;
        }
    }
};
</script>
