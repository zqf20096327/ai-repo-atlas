# QuecPython/solution-xiaozhiAI

⭐ 52 · Python · 推送 2026-01-08 · [GitHub](https://github.com/QuecPython/solution-xiaozhiAI) · 组织维护 · 中文 README

**基于小智平台的 QuecPython AI 语音聊天机方案，面向开发板**

移远（Quectel）QuecPython 团队提供的 AI 聊天机器人嵌入式方案：在小智（xiaozhi.me）AI 平台上，通过 WebSocket 协议实现语音对话，支持关键词语音唤醒与语音打断，使用 Python 便于二次开发。运行于搭载 EC800MCNLE 模块的移远 AI 开发板，需通过 QPYcom 工具烧写固件并导入代码，首次唤醒需在小智后台绑定设备。硬件与开发板需向移远获取或购买。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 WebSocket 协议的跨平台方案，兼容多数 QuecPython 模块
- 支持关键词语音唤醒与语音打断（barge-in）
- 使用 Python 编写，支持二次开发
- 仓库提供 beta 固件与示例演示视频

## 适用场景

- 在移远 AI 开发板上搭建语音对话聊天机器人
- 基于 Python 进行嵌入式 AI 应用的二次开发与学习
- 接入小智平台实现设备语音交互产品原型

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L1: # QuecPython AI Chatbot Based on Xiaozhi Platform
> L7: QuecPython introduces the Xiaozhi Platform AI Chatbot solution. This solution is based on the WebSocket protocol, of
> L15: - Supports voice interruption/barge-in.

## 星数曲线

```mermaid
xychart-beta
    title "QuecPython/solution-xiaozhiAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-30 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `85870da38d94` · [字段定义](../../DATASET.md)*
