<template>
<div class="app-container">
    <div class="head-container">
        <el-date-picker v-model="rangedate" size="small" value-format="yyyy-MM-dd" type="daterange" start-placeholder="开始日期" end-placeholder="结束日期">
        </el-date-picker>
    </div>
    <div class="tab-container">
        <el-tabs v-model="activeName" style="margin-top:15px;" type="border-card" @tab-click="handleClick">
            <el-tab-pane label="出库详情(小麦)" name="unit_price_wheat">
                <keep-alive>
                    <table_unit :sup_this="sup_this"></table_unit>
                </keep-alive>
            </el-tab-pane>
            <el-tab-pane label="出库总计(小麦)" name="net_weight_wheat">
                <keep-alive>
                    <table_net :sup_this="sup_this"></table_net>
                </keep-alive>
            </el-tab-pane>

            <el-tab-pane label="出库详情(玉米)" name="unit_price_corn">
                <keep-alive>
                    <table_unit :sup_this="sup_this"></table_unit>
                </keep-alive>
            </el-tab-pane>
            <el-tab-pane label="出库总计(玉米)" name="net_weight_corn">
                <keep-alive>
                    <table_net :sup_this="sup_this"></table_net>
                </keep-alive>
            </el-tab-pane>
        </el-tabs>
    </div>
    <!--分页组件-->
    <el-pagination :total="total" :page-sizes='[10,50,100,500,1000,3000]' style="margin-top: 8px;" layout="total, prev, pager, next, sizes" @size-change="sizeChange" @current-change="pageChange" /></div>
</template>

<script>
import checkPermission from '@/utils/permission'
import table_net from './module/table_net'
import table_unit from './module/table_unit'
import table_naure from './module/table_naure'
import initData from '@/mixins/initData'
import detail from '@/api/graincentre'
export default {
    components: {
        table_net,
        table_unit,
        table_naure,
    },
    mixins: [initData],
    data() {
        return {
            sup_this: this,
            activeName: 'all',
            dialog: false,
            loading: false,
            value: null,
            rangedate: [],
            oldpara: 'aa',
            environments: [{
                    value: '出库详情',
                    key: 'detailEntry'
                },
                {
                    value: 'a1',
                    key: 'b1'
                },
                {
                    value: 'a2',
                    key: 'b2'
                },
            ]
        }
    },
    methods: {
        checkPermission,
        beforeInit() {
            this.url = 'api/warehousoutdetail/'
            const query = this.query
            const value = query.value
            const active = this.activeName
            const rangedate = this.rangedate
            this.params = {
                page: this.page,
                size: this.size,
            }
             if(rangedate && rangedate.length==2){
                console.log(rangedate)
                this.params['min_cdate'] = rangedate[0]
                this.params['max_cdate'] = rangedate[1]
            }
            if (active === 'unit_price_wheat') {
                this.params['sub_warehous'] = 1
                this.params['unit_price'] = true
                if (this.oldpara !== 'unit_price_wheat'){
                    this.params['page'] = 1
                }else{
                    // console.log(this.oldpara)    
                }
                this.oldpara = 'unit_price_wheat'
            } else if (active === 'net_weight_wheat') {
                this.params['sub_warehous'] = 1
                this.params['net_weight'] = true
                if (this.oldpara !== 'net_weight_wheat'){
                    this.params['page'] = 1
                }else{
                    // console.log(this.oldpara)    
                }
                this.oldpara = 'net_weight_wheat'
            } else if (active === 'naure_wheat') {
                this.params['sub_warehous'] = 1
                this.params['naure'] = true
                if (this.oldpara !== 'naure_wheat'){
                    this.params['page'] = 1
                }else{
                    // console.log(this.oldpara)
                }
                this.oldpara = 'naure_wheat'
            } else if (active === 'unit_price_corn') {
                this.params['sub_warehous'] = 0
                this.params['unit_price'] = true
                if (this.oldpara !== 'unit_price_corn'){
                    this.params['page'] = 1
                }else{
                    // console.log(this.oldpara)
                }
                this.oldpara = 'unit_price_corn'
            } else if (active === 'net_weight_corn') {
                this.params['sub_warehous'] = 0
                this.params['net_weight'] = true
                if (this.oldpara !== 'net_weight_corn'){
                    this.params['page'] = 1
                }else{
                    // console.log(this.oldpara)    
                }
                this.oldpara = 'net_weight_corn'
            } else if (active === 'naure_corn') {
                this.params['sub_warehous'] = 0
                this.params['naure'] = true
                if (this.oldpara !== 'naure_corn'){
                    this.params['page'] = 1
                }else{
                    // console.log(this.oldpara)    
                }
                this.oldpara = 'naure_corn'
            }

            return true
        },
        handleClick(tab, event) {
            this.$nextTick(() => {
                this.init()
            })
        },
        toQuery() {
            this.page = 1
            this.query.value = this.value
            this.init()
        },
        toCreate() {}
    }
}
</script>

<style scoped>

</style>
