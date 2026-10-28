# arefbhrn/IRDebitCardScanner

⭐ 20 · Kotlin · 推送 2026-02-23 · [GitHub](https://github.com/arefbhrn/IRDebitCardScanner) · 个人维护

**Android 库：实时扫描伊朗借记卡卡号并校验**

面向 Android 开发者的轻量级库，使用深度学习与 TensorFlow Lite 实时扫描伊朗借记卡，仅识别有效卡号。通过启动 ScanActivity 获取扫描结果，支持调试模式预览与自定义界面文案；另提供 DebitCardUtils 工具类，含 Luhn 校验加银行前缀查表、银行 slug 识别、IBAN 校验、卡号格式化及自定义 6 位前缀注册。经 Gradle/JitPack 引入，文档建议发布时拆分 ABI 以缩减包体。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度学习 + TensorFlow Lite 实时扫描伊朗借记卡卡号
- Luhn 校验结合银行前缀查表的卡号验证与银行 slug 识别
- 伊朗 IBAN 校验与每 4 位加空格的卡号格式化
- 支持注册自定义 6 位卡号前缀映射到银行 slug

## 适用场景

- 在支付或绑卡流程中让用户用摄像头扫描借记卡卡号
- 根据卡号识别发卡银行 slug
- 校验用户输入的卡号或伊朗 IBAN 是否有效

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L5: A lightweight android library to scan Iranian debit cards fast and realtime using Deep Learning and TensorFlow-Lite.
> L30: ScanActivity.start(this)

## 星数曲线

```mermaid
xychart-beta
    title "arefbhrn/IRDebitCardScanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1ec69aef92ed` · [字段定义](../../DATASET.md)*
