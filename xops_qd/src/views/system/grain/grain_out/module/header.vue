<template>
<div class="head-container">
    <!-- 搜索 -->
    <el-input v-model="query.voucher_number" clearable placeholder="输入关键字搜索" style="width: 200px;" class="filter-item" @keyup.enter.native="toQuery" />
    <el-date-picker v-model="query.rangedate" size="small" value-format="yyyy-mm-dd" type="daterange" start-placeholder="开始日期" end-placeholder="结束日期">
    </el-date-picker>
    <el-select v-model="query.pay" clearable placeholder="款项" class="filter-item" style="width: 90px" @change="toQuery">
        <el-option v-for="item in stateList" :key="item.key" :label="item.display_name" :value="item.key" />
    </el-select><!-- 新增 -->
    <el-button class="filter-item" size="mini" type="primary" icon="el-icon-search" @click="toQuery">搜索</el-button>
    <div style="display: inline-block;margin: 0px 2px;">
        <el-button v-if="checkPermission(['admin','user_all','user_create'])" class="filter-item" size="mini" type="primary" icon="el-icon-plus" @click="$refs.form.dialog = true; getOrgUserTree()">新增</el-button>
        <eForm ref="form" :orgusers="orgusers" :is-add="true" />
    </div>
    <!-- 导出 -->
    <el-button v-if="checkPermission(['admin'])" :loading="downloadLoading" size="mini" class="filter-item" type="primary" icon="el-icon-download" style="display: inline-block;margin: 0px 20px;float: right" @click="download">导出</el-button>
</div>
</template>

<script>
import checkPermission from '@/utils/permission' // 权限判断函数
import {
    getOrganizationUserTree
} from '@/api/organization'
import eForm from './form'
// 查询条件
export default {
    components: {
        eForm
    },
    props: {
        query: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            orgusers: [],
            downloadLoading: false,
            enabledTypeOptions: [{
                    key: 0,
                    display_name: '收购'
                },
                {
                    key: 1,
                    display_name: '代存'
                }
            ],
            stateList: [{
                    key: 0,
                    display_name: '欠账'
                },
                {
                    key: 1,
                    display_name: '付款'
                }
            ],
        }
    },
    methods: {
        checkPermission,
        // 去查询
        toQuery() {
            this.$parent.page = 1
            this.$parent.init()
        },
        // 导出
        getOrgUserTree() {
            getOrganizationUserTree().then(res => {
                this.orgusers = res.detail
            })
        },
        download() {
            this.downloadLoading = true
            import('@/vendor/Export2Excel').then(excel => {
                const tHeader = ['凭证编号', '客户名', '手机', '毛重(吨)', '皮重(吨)', '净重(吨)', '单价', '应付款', '款项', '已付款', '创建时间', '更新时间']
                const filterVal = ['voucher_number', 'customer_name', 'mobile', 'gross_weight', 'vehicle_weight', 'net_weight', 'unit_price', 'amount_pay', 'pay_name', 'actual_pay', 'invoice_date', 'update_time']
                const data = this.formatJson(filterVal, this.$parent.data)
                excel.export_json_to_excel({
                    header: tHeader,
                    data,
                    filename: 'table-list'
                })
                this.downloadLoading = false
            })
        },
        // 数据转换
        formatJson(filterVal, jsonData) {
            return jsonData.map(v => filterVal.map(j => {
               return v[j] 
            }))
        }
    }
}
</script>
