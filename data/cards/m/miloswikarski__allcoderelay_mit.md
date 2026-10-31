# miloswikarski/allcoderelay_mit

⭐ 15 · Dart · 推送 2026-04-15 · [GitHub](https://github.com/miloswikarski/allcoderelay_mit) · [官网](https://grapph.com/allcoderelay/) · 组织维护

**移动端二维码/条码/NFC 扫描器，扫描数据经 webhook 中继到外部系统**

基于 Flutter 3.24+ 的移动应用，扫描多种格式的条码、二维码并读取 NFC 标签，将扫描数据通过 HTTP POST 发送到用户配置的 webhook 端点，服务器处理后返回结构化结果在应用内展示；发送失败时用 SQLite 本地保存历史。Webhook URL 与自定义请求头通过 Flutter Secure Storage 加密存储，支持扫描特定格式二维码完成配置，或使用内置默认 n8n webhook（该外部工作流集成 OpenAI 做扫描内容的 AI 分析）。提供 Google Play 与 App Store 下载，也可用 Flutter 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多格式条码/二维码扫描与 NFC 读取
- 扫描数据以 HTTP POST 中继到自定义 webhook，支持自定义请求头
- webhook 失败时 SQLite 本地保存扫描历史
- 通过扫描特定格式二维码（allcoderelay://）配置 webhook

## 适用场景

- 企业/自动化场景中将扫描的条码、二维码或 NFC 标签实时交给外部系统处理
- 库存管理中扫描 EAN13 条码查询产品信息
- 扫描 NFC 门禁标签触发开门链接

## 场景标签

 · 领域:移动工具/自动化集成

## 证据(README 行号)

> L133: - Other QR, Aztec, or Data Matrix Codes: Uses AI to analyze and provide information about the scanned code
> L138: - integration with OpenAI for AI analysis

## 星数曲线

```mermaid
xychart-beta
    title "miloswikarski/allcoderelay_mit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `14d79b764a80` · [字段定义](../../DATASET.md)*
