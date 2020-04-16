/**
 * Created by jiachenpan on 16/11/18.
 */

/* 合法uri*/
export function validateURL(textval) {
  const urlregex = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+(:[a-zA-Z0-9.&%$-]+)*@)*((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(:[0-9]+)*(\/($|[a-zA-Z0-9.,?'\\+&%$#=~_-]+))*$/;
  return urlregex.test(textval);
}

/* 小写字母*/
export function validateLowerCase(str) {
  const reg = /^[a-z]+$/;
  return reg.test(str);
}

/* 大写字母*/
export function validateUpperCase(str) {
  const reg = /^[A-Z]+$/;
  return reg.test(str);
}

/* 大小写字母*/
export function validatAlphabets(str) {
  const reg = /^[A-Za-z]+$/;
  return reg.test(str);
}

/**
 * 验证邮箱
 * @param str
 * @returns {boolean}
 */
export function validatEmail(str) {
  const reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
  return reg.test(str);
}

// 手机号验证
export function isvalidPhone(str) {
  const reg = /^1[3|4|5|7|8][0-9]\d{8}$/;
  return reg.test(str);
}

// 不能输入中文
export function isvalidChinaese(str) {
  const reg = /^[a-zA-Z0-9_]+$/g;
  return reg.test(str);
}

export function checkWeightValue(rule, value, callback) {
  if (value == "" || value == undefined || value == null) {
    callback(new Error("请输入数字"));
  } else if (!Number(value)) {
    callback(new Error("请输入正确数字"));
  } else if (value < 0) {
    callback(new Error("请输入大于 1 的数字"));
  } else {
    callback();
  }
}

export function checkUnit_price(rule, value, callback) {
  if(value == 0){
    callback();
  }
  else if (value == "" || value == undefined || value == null) {
    callback(new Error("请输入数字"));
  } else if (!Number(value)) {
    callback(new Error("请输入正确数字"));
  } else if (value < 0) {
    callback(new Error("请输入大于 1 的数字"));
  } else {
    callback();
  }
}
//验证是否0 1之间
export function checkNaure(rule, value, callback) {
  console.log(value)
  if (value == 0 || value == 1) {
    callback();
  } else {
    callback(new Error("请输入正整数 1:代存   0:收购"));
  }
}

export function isDecimal(rule, value, callback) {
  if (!value && value != 0) {
    return callback(new Error("输入不可以为空c"));
  }
  setTimeout(() => {
    if (value == 0) {
      callback();
    } else {
      if (!Number(value)) {
        callback(new Error("请输入大于等于 0 的数字"));
      } else {
        if (value < 0) {
          callback(new Error("请输入大于等于 0 的数字"));
        } else {
          callback();
        }
      }
    }
  }, 100);
}
