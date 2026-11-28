# Cansiny0320/bili-agent-kit

⭐ 3 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Cansiny0320/bili-agent-kit) · [官网](https://www.npmjs.com/package/@bili-agent-kit/core) · 个人维护 · 中文 README

**给 AI Agent 接入 B 站的 MCP/CLI/SDK 工具包**

以 TypeScript 编写的 B 站接入工具包，提供 MCP server、CLI 与 SDK 三种形态，让 AI 助手或脚本执行搜索、音视频下载、本地 ASR 转写、收藏管理、消息收发与动态发布等操作。通过扫码登录和 Cookie/OAuth 管理维持会话，CLI 侧带操作确认机制；需 Node.js 22.18+ 或更高版本运行。README 声明项目与 Bilibili 官方无关联。

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

- 同一能力以 MCP、CLI、SDK 三种接口提供
- 覆盖读取（搜索/字幕/评论/弹幕）与写入（发评论/私信/发动态）双向操作
- 内置本地 ASR 转写，支持音视频下载与定点抽帧
- 扫码登录与操作审批机制

## 适用场景

- 在支持 MCP 的 AI 助手里搜索和下载 B 站视频
- 批量导出收藏夹并转写视频字幕
- 用脚本管理私信、评论与动态发布

## 场景标签

 · 领域:AI 生态/平台接入工具

## 证据(README 行号)

> L2:  给你的 Agent 接入 B 站，支持 MCP、CLI、SDK。
> L38: |@bili-agent-kit/mcp|接入支持 stdio MCP 的 AI 助手|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `010925597bf8` · [字段定义](../../DATASET.md)*
