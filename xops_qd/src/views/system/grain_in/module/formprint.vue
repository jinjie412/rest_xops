<template>
<el-dialog :append-to-body="true" :visible.sync="dialog" :title="'打印票据'" width="850px">
    <el-form ref="print" :model="form" :rules="rules" size="small" label-width="80px">
        <el-row v-show="isAdd === false">
            <el-col :span="12">
                <el-form-item label="凭证编号" prop="voucher_number">
                    <el-input class='nonebord' v-model="form.voucher_number" style="width: 300px;" />
                </el-form-item>
            </el-col>

            <el-col :span="12">
                <el-form-item label="客户" prop="customer_name">
                    <el-input class='nonebord' v-model="form.customer_name" style="width: 300px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="8">
                <el-form-item label="毛重(吨)" prop="gross_weight">
                    <el-input class='nonebord' type="string" v-model.number="form.gross_weight" style="width: 150px;" />
                </el-form-item>
            </el-col>
            <el-col :span="8">
                <el-form-item label="皮重(吨)" prop="vehicle_weight">
                    <el-input class='nonebord' type="string" v-model.number="form.vehicle_weight" style="width: 150px;" />
                </el-form-item>
            </el-col>
            <el-col :span="8">
                <el-form-item label="扣量(吨)" prop="sub_weight">
                    <el-input class='nonebord' type="string" v-model.number="form.sub_weight" style="width: 150px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-form-item label="净重(吨)" prop="net_weight">
                    <el-input class='nonebord' type="float" v-model="form.net_weight" style="width: 250px;" />
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-form-item label="单价(元)" prop="unit_price">
                    <el-input class='nonebord' type="float" v-model="form.unit_price" style="width: 300px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row v-show="isAdd === false">
            <el-col :span="12">
                <el-form-item label="应付款(元)" prop="amount_pay">
                    <el-input class='nonebord' type="float" v-model="form.amount_pay" style="width: 250px;" />
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-form-item label="开票时间">
                    <el-date-picker class='nonebord' type="date" v-model="nowdate" :picker-options="pickerOptions">
                    </el-date-picker>
                </el-form-item>
            </el-col>
        </el-row>

    </el-form>
    <div slot="footer" class="dialog-footer">
        <el-button type="text" @click="cancel">取消</el-button>
        <el-button :loading="loading" type="primary" @click="doSubmit">打印</el-button>
    </div>
</el-dialog>
</template>

<script>
import Treeselect from "@riophae/vue-treeselect";
import "@riophae/vue-treeselect/dist/vue-treeselect.css";
export default {
    name: "Form",
    components: {
        Treeselect
    },
    props: {
        isAdd: {
            type: Boolean,
            required: true
        },
        sup_this: {
            type: Object,
            default: null
        }
    },
    data() {
        return {
            dialog: false,
            loading: false,
            nowdate: new Date(),
            form: {
                voucher_number: "",
                customer_name: "李四",
                mobile: "13888888888",
                gross_weight: 1110,
                vehicle_weight: 100,
                sub_weight: 10,
                net_weight: 0,
                unit_price: 1,
                amount_pay: 0,
            },
            formItem: {
                stateList: [{
                        value: 0,
                        label: '收购'
                    },
                    {
                        value: 1,
                        label: '代存'
                    }
                ]

            },
            pickerOptions: {
                shortcuts: [{
                    text: '今天',
                    onClick(picker) {
                        picker.$emit('pick', new Date());
                    }
                }]
            }
        };
    },
    methods: {
        cancel() {
            this.resetForm();
        },
        resetForm() {
            this.dialog = false;
            this.$refs["form"].resetFields();
            this.form = {
                customer_name: "",
            };
        },
        doSubmit() {
            this.$print(this.$refs.print)
        }
    }
};
</script>

<style>
/* 修改input的样式，为了不覆盖本组件其他处的样式，需要自定义一个类名 */
.nonebord input.el-input__inner {
    border-radius: 15px;
    border-style: none;
}
</style>
<style>
/* //写自己的样式 */
</style>
