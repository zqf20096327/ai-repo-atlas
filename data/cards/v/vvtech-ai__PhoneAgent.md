# vvtech-ai/PhoneAgent

⭐ 31 · Kotlin · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/vvtech-ai/PhoneAgent) · 组织维护 · 中文 README

**开源安卓客户端：用 AI Agent 完成真实电话任务**

Kotlin/Jetpack Compose 编写的 Android 客户端：用户以语音或文字描述电话任务（如订餐、会议邀约），Agent 补全时间/联系人等要素，确认后经托管服务与 SIP 通讯网络拨打真实电话，返回状态、通话转写与任务结果，并支持实时翻译与切换语音模型。仓库仅含客户端源码，后端、Call Skill SDK 与运行时未开源；需邀请码激活，APK 要求 Android 8.0+ arm64 设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 语音/文字创建任务，确认后执行真实电话流程并返回转写与结果
- 实时翻译通话并展示双方转写文本
- 可在托管服务提供的语音模型间切换
- Call Skill 设计提案机制（SDK 与运行时尚未发布）

## 适用场景

- 让 AI 代打餐厅预订、会议邀约等电话任务
- 进行跨语言实时翻译通话
- 设计并提交可复用的 Call Skill 用例提案

## 场景标签

`语音 Agent` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: **An open-source intelligent Agent built for real phone tasks.**
> L5: Describe a reservation, notification, coordination task, or cross-language call by voice or text. PhoneAgent helps f
> L40: - **Switch voice models**: Select from the models currently available through the hosted service based on the task.

## 星数曲线

```mermaid
xychart-beta
    title "vvtech-ai/PhoneAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2840ac7a6265` · [字段定义](../../DATASET.md)*
