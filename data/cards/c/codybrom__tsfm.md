# codybrom/tsfm

⭐ 23 · TypeScript · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/codybrom/tsfm) · [官网](http://tsfm.dev) · 个人维护

**Apple 端侧 Foundation Models 的 TypeScript/Node.js SDK**

为 Apple 的 Foundation Models 框架提供 TypeScript/Node.js 绑定，使 Node.js 应用调用 macOS 端侧 Apple Intelligence 进行推理：支持流式文本生成、类型化 schema 的结构化输出、工具调用、会话持久化，以及 Chat 风格与 Responses 风格 API。数据不离开本机，无需 API key。限制：仅支持 Apple Silicon Mac 且需 macOS 26+、开启 Apple Intelligence、Node.js 24+；通过 npm 安装，预构建二进制，无需 Xcode（源码构建除外）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端侧推理，数据不离开本机，无需 key
- 流式生成、结构化输出、工具调用
- Chat 风格与 Responses 风格 API（tsfm-sdk/chat）
- npm 安装 koffi 预构建二进制，无需 Xcode

## 适用场景

- 在 Node.js 应用中调用 macOS 端侧 Apple Intelligence 模型
- 本地离线生成文本或结构化数据，不上传数据
- 为已有 Chat/Responses 风格接口的应用切换到 Apple 端侧模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5:  TypeScript SDK for Apple's Foundation Models framework.
> L6:  On-device Apple Intelligence in Node.js — No keys. No fees. It just works.

## 星数曲线

```mermaid
xychart-beta
    title "codybrom/tsfm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3e0a8905b0fc` · [字段定义](../../DATASET.md)*
