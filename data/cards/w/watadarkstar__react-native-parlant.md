# watadarkstar/react-native-parlant

⭐ 56 · TypeScript · MIT · 推送 2026-07-19 · [GitHub](https://github.com/watadarkstar/react-native-parlant) · [官网](https://www.npmjs.com/package/react-native-parlant) · 个人维护

**在 React Native/Expo/React 应用中接入 Parlant AI agent 的聊天库**

非官方社区维护的 React Native 库，提供 useChat hook 连接 Parlant AI agent，支持实时消息收发、自动会话创建、长轮询消息拉取、自动重连（默认最多重试）、消息审核配置与自定义请求头。兼容 React Native、Expo 与 React 应用，附带 TypeScript 类型定义，可搭配 react-native-gifted-chat 使用。要求 React 16.8+，默认 API 端点为 localhost:8800。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- useChat hook 管理与 Parlant agent 的聊天会话
- 自动会话创建、长轮询消息获取与自动重连
- 完整 TypeScript 类型定义
- 跨平台支持 React Native / Expo / React

## 适用场景

- 在移动 App 中嵌入 Parlant AI agent 聊天界面
- 为已有 React/Expo 应用添加实时 AI 对话功能
- 自定义请求头与审核策略接入自托管 Parlant API

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A React Native library for integrating <a href="https://www.parlant.io"
> L52: import { useChat } from "react-native-parlant";
> L61: The main hook for managing chat sessions with Parlant AI agents.

## 星数曲线

```mermaid
xychart-beta
    title "watadarkstar/react-native-parlant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-29 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `86125051fe2b` · [字段定义](../../DATASET.md)*
