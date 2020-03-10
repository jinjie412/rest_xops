<template>
<div class="app-container">
    <eHeader :roles="roles" :organizations="organizations" :query="query" />
    <!--表格渲染-->
    <el-table v-loading="loading" :data="data" size="small" border style="width: 100%;">
        <el-table-column label="编号" width="50px">
            <el-table-column label="客户名" width="150px" />
            <el-table-column label="手机" width="100px" />
            <el-table-column label="毛重/吨" width="100px" />
            <el-table-column label="皮重/吨" width="100px" />
            <el-table-column label="扣量/吨" width="100px" />
            <el-table-column label="净重/吨" width="100px" />
            <el-table-column label="单价" width="100px" />
            <el-table-column label="应付款" width="100px" />
            <el-table-column label="已付款" width="100px" />
            <el-table-column label="性质" width="100px" />
            <template slot-scope="scope">
                <span>{{ scope.row.is_active ? '激活':'锁定' }}</span>
            </template>
        </el-table-column>
        <el-table-column label="操作" width="200px" align="center">
        </el-table-column>
    </el-table>
    <!--分页组件-->
    <el-pagination :total="total" style="margin-top: 8px;" layout="total, prev, pager, next, sizes" @size-change="sizeChange" @current-change="pageChange" />
</div>
</template>

<script>
import checkPermission from '@/utils/permission'
import initData from '@/mixins/initData'
import {
    parseTime
} from '@/utils/index'
import eHeader from './module/header'
import edit from './module/edit'
import updatePass from './module/updatePass'
export default {
    components: {
        eHeader,
        edit,
        updatePass
    },
    mixins: [initData],
    data() {
        return {
            roles: [],
            organizations: [],
            delLoading: false,
            sup_this: this
        }
    },
    created() {
        this.$nextTick(() => {
            this.init()
        })
    },
    methods: {
        parseTime,
        checkPermission,
        beforeInit() {
            this.url = 'api/grain/'
            const sort = 'id'
            const query = this.query
            const value = query.value
            const is_active = query.is_active
            this.params = {
                page: this.page,
                size: this.size,
                ordering: sort
            }
            if (is_active !== '' && is_active !== null) {
                this.params['is_active'] = is_active
            }
            if (value) {
                this.params['search'] = value
            }
            return true
        },
        subDelete(id) {
            this.delLoading = true
            del(id).then(res => {
                this.delLoading = false
                this.$refs[id].doClose()
                this.init()
                this.$message({
                    showClose: true,
                    type: 'success',
                    message: '删除成功!',
                    duration: 2500
                })
            }).catch(err => {
                this.delLoading = false
                this.$refs[id].doClose()
                console.log(err)
            })
        },
        getOrganizations() {
            getOrganizationTree().then(res => {
                this.organizations = res.detail
            })
        },
        getRoleALL() {
            getRoles().then(res => {
                const newres = res.results.map(item => {
                    return {
                        ...item,
                        label: item.name
                    }
                })
                this.roles = newres
            })
        }
    }
}
</script>

<style scoped>

</style>
