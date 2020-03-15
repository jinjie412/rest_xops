import request from "@/utils/request";
//入库
export function add(data, url) {
  return request({
    url: "api/" + url + "/",
    method: "post",
    data
  });
}

//小麦入库编辑
export function edit(voucher_number, data, url) {
  return request({
    url: "api/" + url + "/" + voucher_number + "/",
    method: "put",
    data
  });
}

//小麦入库删除
export function del(voucher_number, url) {
  return request({
    url: "api/" + url + "/" + voucher_number + "/",
    method: "delete"
  });
}

//入库详情
export function detail(data, url) {
  return request({
    url: "api/" + url + "/",
    method: get,
    data: data,
  })
}