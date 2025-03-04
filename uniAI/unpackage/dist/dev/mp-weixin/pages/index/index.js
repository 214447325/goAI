"use strict";
const common_vendor = require("../../common/vendor.js");
const comment_js_common = require("../../comment/js/common.js");
const _sfc_main = {
  data() {
    return {
      userName: "",
      password: ""
    };
  },
  onLoad() {
  },
  methods: {
    clickSub() {
      if (!this.userName) {
        common_vendor.index.showToast({
          title: "请输入账号",
          icon: "none",
          duration: 4e3
        });
        return false;
      }
      if (!this.password) {
        common_vendor.index.showToast({
          title: "请输入密码",
          icon: "none",
          duration: 4e3
        });
        return false;
      }
      common_vendor.index.request({
        url: `${comment_js_common.requesturl}/user/login`,
        data: {
          userName: this.userName,
          password: this.password
        },
        methods: "GET",
        success: (res) => {
          let data = res.data;
          if (data.code == 200) {
            let _data_ = data.data;
            common_vendor.index.setStorageSync("userInfo", JSON.stringify(_data_));
            common_vendor.index.__f__("log", "at pages/index/index.vue:66", _data_);
          } else {
            common_vendor.index.showToast({
              title: data.msg,
              icon: "none",
              duration: 4e3
            });
          }
        }
      });
    }
  }
};
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {
    a: $data.userName,
    b: common_vendor.o(($event) => $data.userName = $event.detail.value),
    c: $data.password,
    d: common_vendor.o(($event) => $data.password = $event.detail.value),
    e: common_vendor.o((...args) => $options.clickSub && $options.clickSub(...args))
  };
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render]]);
wx.createPage(MiniProgramPage);
//# sourceMappingURL=../../../.sourcemap/mp-weixin/pages/index/index.js.map
