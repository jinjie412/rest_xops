<template>
<div class="head-container">
    <!-- 搜索 -->
    <el-input v-model="query.voucher_number" clearable placeholder="输入关键字搜索" style="width: 200px;" class="filter-item" @keyup.enter.native="toQuery" />
    <el-date-picker v-model="query.rangedate" size="small" value-format="yyyy-mm-dd" type="daterange" start-placeholder="开始日期" end-placeholder="结束日期">
    </el-date-picker>
    <el-button class="filter-item" size="mini" type="primary" icon="el-icon-search" @click="toQuery">搜索</el-button>
    <!-- 新增 -->
    <div style="display: inline-block;margin: 0px 2px;">
        <el-button v-if="checkPermission(['admin','user_all','user_create'])" class="filter-item" size="mini" type="primary" icon="el-icon-plus" @click="$refs.form.dialog = true; getOrgUserTree()">新增</el-button>
        <eForm ref="form" :roles="roles" :organizations="organizations" :orgusers="orgusers" :is-add="true" />
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
        organizations: {
            type: Array,
            required: true
        },
        roles: {
            type: Array,
            required: true
        },
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
            ]
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
                const tHeader = ['ID', '用户名', '邮箱', '头像地址', '状态', '注册日期', '最后修改密码日期']
                const filterVal = ['id', 'username', 'email', 'avatar', 'createTime', 'lastPasswordResetTime']
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
            return jsonData.map(v => filterVal.map(j => {}))
        }
    }
}
</script>
