# TS 特征值读写示例（FAQ）

## 适用范围
- **芯片**：TS8001 / TS8010
- **主题**：GATT 特征值 read/write/notify/indicate 的典型交互与常见错误码

## 典型交互流程（客户端视角）
1. **扫描并连接**
2. **服务发现**（Primary Service / Characteristic / Descriptor）
3. **读特征值（Read）**
4. **写特征值（Write / Write Without Response）**
5. **启用通知**：写 CCCD = 0x0001（Notify）或 0x0002（Indicate）
6. **接收 Notify/Indicate**（Indicate 需要客户端确认）

## 常见错误码（ATT）
- **0x01**：Invalid Handle
- **0x02**：Read Not Permitted
- **0x03**：Write Not Permitted
- **0x05**：Insufficient Authentication（需要认证/MITM）
- **0x0F**：Insufficient Encryption（需要加密）
- **0x10**：Unsupported Group Type（服务发现相关）

## 服务端实现注意项（通用）
- **权限与安全**：若特征值要求加密/认证，客户端必须先完成配对/加密
- **长度与分包**：大于 \(MTU-3\) 的 ATT 负载需要分包（长写/prepare write 等）
- **CCCD 状态**：必须保存每条连接的 CCCD 使能状态（多连接时尤其重要）

## 验证方法
- 用 nRF Connect 或类似工具跑完完整流程
- 抓包确认 Read/Write/CCCD/Notify opcode 与错误码符合预期
