<template>
	<view class="content">
		
		<view class="content_box">
			<view class="input_box">
				<input class="input" v-model="userName" type="text" placeholder="请输入账号" />
			</view>
			
			<view class="input_box">
				<input class="input" v-model="password" type="password" placeholder="请输入密码" />
			</view>
			
			<button size="mini" type="primary"
				style="color:#ffffff;backgroundColor:#1AAD19;borderColor:#1AAD19"
				hover-class="is-hover" @click='clickSub'>登录</button>
		</view>
	
	</view>
</template>

<script>
	import {requesturl} from "@/comment/js/common";

    export default {
		data() {
			return {
				userName:'',
				password:''
			}
		},
		onLoad() {

		},
		methods: {
			clickSub() {
				if(!this.userName) {
					uni.showToast({
					    title: '请输入账号',
					    icon: 'none',
					    duration: 4000,
					});
					return false
				}
				
				if(!this.password) {
					uni.showToast({
					    title: '请输入密码',
					    icon: 'none',
					    duration: 4000,
					});
					return false
				}

                uni.request({
                    url:`${requesturl}/user/login`,
                    data:{
                        userName:this.userName,
                        password:this.password,
                    },
                    methods:'GET',
                    success:(res) => {
                        let data = res.data
                        if(data.code == 200) {
                            let _data_ = data.data
                            uni.setStorageSync('userInfo', JSON.stringify(_data_));
                            console.log(_data_)
                        } else {
                            uni.showToast({
                                title: data.msg,
                                icon: 'none',
                                duration: 4000,
                            });
                        }
                        // console.log(res)
                    }

                })
                // console.log(requesturl)
				
			}
		}
	}
</script>

<style>
	.content {
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
	}
	
	.content_box {
		width: 500rpx;
		height: auto;
		box-sizing: border-box;
		padding: 20rpx;
		display: flex;
		flex-direction: column;
		align-items: center;
		/* background: red; */
	}
	
	.input_box {
		width: 100%;
		height: auto;
	}
	
	.input {
		width: 100%;
		height: 40rpx;
		margin-bottom: 40rpx;
		border-bottom: 1px solid #dfe2e5;
		box-sizing: border-box;
		padding-bottom: 10rpx;
		font-size: 14px;
	}

	/* .logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	} */
</style>
