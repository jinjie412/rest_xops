<template>
<div class="app-container">
    <eHeader :query="query" />
    <!--表格渲染-->
    <el-table v-loading="loading" :data="data" size="small" border style="width: 100%;">
        <el-table-column label="详情" width="50px">
            <el-table-column prop="voucher_number" label="凭证编号" width="116px" />
            <el-table-column prop="customer_name" label="客户名" width="100px" />
            <el-table-column prop="mobile" label="手机" width="95px" />
            <el-table-column prop="gross_weight" label="毛重(吨)" width="64px" />
            <el-table-column prop="vehicle_weight" label="皮重(吨)" width="64px" />
            <el-table-column prop="sub_weight" label="扣量(吨)" width="64px" />
            <el-table-column prop="net_weight" label="净重(吨)" width="64px" />
            <el-table-column prop="unit_price" label="单价" width="50px" />
            <el-table-column prop="amount_pay" label="应付款" width="85px" />
            <el-table-column prop="pay_name" label="款项" width="50px" />
            <el-table-column prop="actual_pay" label="已付款" width="85px" />
            <el-table-column prop="naure_name" label="性质" width="46px" />
            <el-table-column prop="invoice_date" label="创建时间" width="134px" />
            <el-table-column prop="update_time" label="更新时间" width="134px" />
        </el-table-column>
        <el-table-column label="操作" width="205px" align="center">
            <template slot-scope="scope">
                <edit v-if="checkPermission(['admin','user_all','user_edit'])" :data="scope.row" :sup_this="sup_this" width="66" />
                <prin v-if="checkPermission(['admin','user_all','user_edit'])" :data="scope.row" :sup_this="sup_this" />
                <el-popover v-if="checkPermission(['admin','user_all','user_delete'])" :ref="scope.row.voucher_number" placement="top" width="180">
                    <p>确定删除本条数据吗？所有关联的数据将会被清除</p>
                    <div style="text-align: right; margin: 0">
                        <el-button size="mini" type="text" @click="$refs[scope.row.voucher_number].doClose()">取消</el-button>
                        <el-button :loading="delLoading" type="primary" size="mini" @click="subDelete(scope.row.voucher_number)">确定</el-button>
                    </div>
                    <el-button slot="reference" type="danger" size="mini" width="6">删除</el-button>
                </el-popover>
            </template>
        </el-table-column>
    </el-table>
    <!--分页组件-->
    <el-pagination :total="total" :page-sizes='[10,50,100,500,1000,3000]' style="margin-top: 8px;" layout="total, prev, pager, next, sizes" @size-change="sizeChange" @current-change="pageChange" />
</div>
</template>

<script>
import checkPermission from '@/utils/permission'
import {
    del
} from '@/api/graincentre'
import initData from '@/mixins/initData'
import {
    parseTime
} from '@/utils/index'
import eHeader from './module/header'
import edit from './module/edit'
import prin from './module/prinw'
export default {
    components: {
        eHeader,
        edit,
        prin,
    },
    mixins: [initData],
    data() {
        return {
            delLoading: false,
            sup_this: this,
            url_path: "warehous",
            grain_type: {}
        }
    },
    created() {
        // this.getOrganizations()
        this.set_grain()
        this.$nextTick(() => {
            this.init()
        })
    },
    methods: {
        parseTime,
        checkPermission,
        set_grain() {
            const path = this.$router.history.current.path
            if (path == '/system/corn') {
                this.grain_type = {
                    "grain": '{玉米}',
                    'sub_warehous': 0
                }
                this.$store.dispatch('set_grain', this.grain_type)
            } else if (path == '/system/wheat') {
                this.grain_type = {
                    "grain": '{小麦}',
                    'sub_warehous': 1
                }
                this.$store.dispatch('set_grain', this.grain_type)
            }
        },
        beforeInit() {
            this.url = 'api/' + this.url_path + '/'
            const sort = '-invoice_date'
            const query = this.query
            const value = query.voucher_number
            const naure = query.naure
            const rangedate = query.rangedate
            const pay = query.pay
            this.params = {
                page: this.page,
                size: this.size,
                ordering: sort,
                sub_warehous: this.grain_type.sub_warehous
            }
            if (naure !== "" && naure !== null) {
                this.params['naure'] = naure
            }
            if (rangedate && rangedate.length == 2) {
                this.params['min_cdate'] = rangedate[0]
                this.params['max_cdate'] = rangedate[1]
            }
            if (value) {
                this.params['search'] = value
            }
            if (pay !== "" && pay !== null) {
                this.params['pay'] = pay
            }
            return true
        },
        subDelete(voucher_number) {
            this.delLoading = true
            del(voucher_number, this.url_path).then(res => {
                this.delLoading = false
                this.$refs[voucher_number].doClose()
                this.init()
                this.$message({
                    showClose: true,
                    type: 'success',
                    message: '删除成功!',
                    duration: 2500
                })
            }).catch(err => {
                this.delLoading = false
                this.$refs[voucher_number].doClose()
                console.log(err)
            })
        },
    }
}
</script>

<style scoped>

</style>
