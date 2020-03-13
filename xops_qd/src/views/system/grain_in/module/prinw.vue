<template>
  <div>
    <el-button size="mini" type="success" @click="to">打印</el-button>
    <eForm ref="form" :orgusers="orgusers" :sup_this="sup_this" :is-add="false"/>
  </div>
</template>
<script>
import eForm from './formprint'
import { getOrganizationUserTree } from '@/api/organization'
export default {
  components: { eForm },
  props: {
    data: {
      type: Object,
      required: true
    },
    // index.vue 的this 可用于刷新数据
    sup_this: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      orgusers: []
    }
  },
  methods: {
    to() {
      const _this = this.$refs.form
      _this.form = {
          voucher_number: this.data.voucher_number,
          customer_name: this.data.customer_name,
          gross_weight: this.data.gross_weight,
          vehicle_weight: this.data.vehicle_weight,
          sub_weight: this.data.sub_weight,
          net_weight: this.data.net_weight,
          unit_price: this.data.unit_price,
          amount_pay: this.data.amount_pay,
        }
      _this.dialog = true
    }
  }
}
</script>

<style scoped>
  div{display: inline-block;margin-right: 3px;}
</style>
