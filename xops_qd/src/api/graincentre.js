import request from '@/utils/request'

export function add(data) {
  return request({
    url: 'api/warehousentry/',
    method: 'post',
    data
  })
}

export function edit(id, data) {
  return request({
    url: 'api/warehousentry/',
    method: 'put',
    data
  })
}