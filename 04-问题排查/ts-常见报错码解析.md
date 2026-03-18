# TS 常见报错码解析（FAQ）

## 适用范围
- **芯片**：TS8001 / TS8010
- **覆盖**：BLE 连接/配对/GATT 交互中常见错误码与定位思路

## 1) 断连原因（HCI/LL 常见）
> 实际枚举以 SDK/协议栈定义为准；建议在日志里同时打印十六进制与名称。

- **对端终止连接**：对端主动断开（例如 APP 退后台、用户手动断开）
- **连接超时**：supervision timeout（空口质量差/参数不合理/阻塞）
- **认证失败/加密失败**：SMP 流程未完成或密钥不一致

## 2) ATT/GATT 常见错误码
- **0x01 Invalid Handle**：handle 不存在/服务发现未完成/缓存过期
- **0x02 Read Not Permitted**：属性不支持读
- **0x03 Write Not Permitted**：属性不支持写
- **0x05 Insufficient Authentication**：需要认证（MITM 等）
- **0x0F Insufficient Encryption**：需要加密
- **0x13 Invalid Attribute Value Length**：写入长度不符合要求

## 3) SMP（配对）常见失败原因
- **参数不兼容**：IO 能力/认证需求/LESC 不匹配
- **密钥分发异常**：bonding 数据未保存或保存错误

## 定位建议（通用）
1. **先抓住一个“确定的码”**：断连 reason、ATT error、SMP reason，三者至少拿到其一。
2. **对齐时间线**：错误码出现前后各 2–5 秒的日志 + 抓包。
3. **最小化复现**：关掉加密/关掉大数据/关掉多连接逐项排除。
