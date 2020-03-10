<template>
<el-dialog :append-to-body="true" :visible.sync="dialog" :title="isAdd ? '新增' : '编辑'" width="850px">
    <el-form ref="form" :model="form" :rules="rules" size="small" label-width="80px">
        <el-row v-show="isAdd === false">
            <el-col>
                <el-form-item label="凭证编号" prop="voucher_number">
                    <el-input v-model="form.voucher_number" :disabled="isAdd === false" style="width: 300px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="12">
                <el-form-item label="客户名" prop="customer_name">
                    <el-input v-model="form.customer_name" style="width: 300px;" />
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-form-item label="手机" prop="mobile">
                    <el-input v-model="form.mobile" style="width: 300px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="8">
                <el-form-item label="毛重(吨)" prop="gross_weight">
                    <el-input type="number" v-model.number="form.gross_weight" style="width: 150px;" />
                </el-form-item>
            </el-col>
            <el-col :span="8">
                <el-form-item label="皮重(吨)" prop="vehicle_weight">
                    <el-input type="number" v-model.number="form.vehicle_weight" style="width: 150px;" />
                </el-form-item>
            </el-col>
            <el-col :span="8">
                <el-form-item label="扣量(吨)" prop="sub_weight">
                    <el-input type="number" v-model.number="form.sub_weight" style="width: 150px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="24">
                <el-form-item label="收购单价" prop="unit_price">
                    <el-input type="number" v-model.number="form.unit_price" style="width: 300px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row v-show="isAdd === false">
            <el-col :span="12">
                <el-form-item label="应付款" prop="amount_pay">
                    <el-input type="number" v-model.number="form.amount_pay" :disabled="isAdd === false" style="width: 300px;" />
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-form-item label="已付款" prop="actual_pay">
                    <el-input type="number" v-model.number="form.actual_pay" style="width: 300px;" />
                </el-form-item>
            </el-col>
        </el-row>
        <el-row>
            <el-form-item label="性质" prop="naure">
                <el-select v-model="form.naure" clearable class="filter-item" style="width: 90px">
                    <el-option v-for="item in formItem.stateList" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
            </el-form-item>
        </el-row>
        <el-row v-show="isAdd === false">
            <el-col :span="12">
                <el-form-item label="创建时间" prop="invoice_date">
                    <el-input v-model="form.invoice_date" :disabled="isAdd === false" style="width: 200px;" />
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-form-item label="更新时间" prop="update_time">
                    <el-input v-model="form.update_time" :disabled="isAdd === false" style="width: 200px;" />
                </el-form-item>
            </el-col>
        </el-row>     
    </el-form>
    <div slot="footer" class="dialog-footer">
        <el-button type="text" @click="cancel">取消</el-button>
        <el-button :loading="loading" type="primary" @click="doSubmit">确认</el-button>
    </div>
</el-dialog>
</template>

<script>
import {
    add, add_w,
    edit, edit_w
} from "@/api/graincentre.js";
import Treeselect from "@riophae/vue-treeselect";
import "@riophae/vue-treeselect/dist/vue-treeselect.css";
import {
    isvalidPhone,
    checkWeightValue,
    checkNaure,
    isDecimal,
    checkUnit_price
} from "@/utils/validate";
var validPhone = (rule, value, callback) => {
    if (!value) {
        callback();
    } else if (!isvalidPhone(value)) {
        callback(new Error("请输入正确的11位手机号码"));
    } else {
        callback();
    }
};
export default {
    name: "Form",
    components: {
        Treeselect
    },
    props: {
        orgusers: {
            type: Array,
            required: true
        },
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
            form: {
                voucher_number: "",
                customer_name: "张三",
                mobile: "13888888888",
                gross_weight: 1110,
                vehicle_weight: 100,
                sub_weight: 10,
                net_weight: 0,
                unit_price: 1,
                amount_pay: 0,
                actual_pay: 0,
                naure: 1,
                sub_warehous: 1
            },
            rules: {
                customer_name: [{
                        required: true,
                        message: "请输入客户名",
                        trigger: "blur"
                    },
                    {
                        min: 1,
                        max: 20,
                        message: "长度在 3 到 20 个字符",
                        trigger: "blur"
                    }
                ],
                mobile: [{
                    required: true,
                    trigger: "blur",
                    validator: validPhone
                }],
                gross_weight: [{
                    required: true,
                    message: "毛重不能为空",
                    validator: checkWeightValue,
                    trigger: "blur"
                }],
                vehicle_weight: [{
                    required: true,
                    message: "皮重不能为空",
                    validator: checkWeightValue,
                    trigger: "blur"
                }],
                sub_weight: [{
                    required: true,
                    validator: isDecimal,
                    trigger: "blur"
                }],
                unit_price: [{
                    required: true,
                    validator: checkUnit_price
                }],
                naure: [{
                    required: true,
                    validator: checkNaure
                }],
                actual_pay:[{
                    validator: checkUnit_price,
                }
                ]
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
        };
    },
    methods: {
        cancel() {
            this.resetForm();
        },
        doSubmit() {
            this.$refs["form"].validate(valid => {
                if (valid) {
                    this.loading = true;
                    if (this.isAdd) {
                        this.doAdd();
                    } else this.doEdit();
                } else {
                    return false;
                }
            });
        },
        doAdd() {
            add_w(this.form)
                .then(res => {
                    this.resetForm();
                    this.$message({
                        showClose: true,
                        type: "success",
                        message: "添加成功!默认密码123456!",
                        duration: 2500
                    });
                    this.loading = false;
                    this.$parent.$parent.init();
                })
                .catch(err => {
                    this.loading = false;
                    console.log(err);
                });
        },
        doEdit() {
            edit_w(this.form.voucher_number, this.form)
                .then(res => {
                    this.resetForm();
                    this.$message({
                        showClose: true,
                        type: "success",
                        message: "修改成功!",
                        duration: 2500
                    });
                    this.loading = false;
                    this.sup_this.init();
                })
                .catch(err => {
                    this.loading = false;
                    console.log(err);
                });
        },
        resetForm() {
            this.dialog = false;
            this.$refs["form"].resetFields();
            this.form = {
                customer_name: "",
            };
        }
    }
};
</script>

<style scoped>
</style>
