import request from "@/utils/request";

export function add(data) {
  return request({
    url: "api/warehousentry/",
    method: "post",
    data
  });
}

export function edit(voucher_number, data) {
  return request({
    url: "api/warehousentry/" + voucher_number + "/",
    method: "put",
    data
  });
}

export function del(voucher_number) {
  return request({
    url: "api/warehousentry/" + voucher_number + "/",
    method: "delete"
  });
}

export function add_w(data) {
  return request({
    url: "api/warehous/",
    method: "post",
    data
  });
}

export function edit_w(voucher_number, data) {
  return request({
    url: "api/warehous/" + voucher_number + "/",
    method: "put",
    data
  });
}

export function del_w(voucher_number) {
  return request({
    url: "api/warehous/" + voucher_number + "/",
    method: "delete"
  });
}
