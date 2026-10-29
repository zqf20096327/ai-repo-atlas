# sunls24/nextai

⭐ 22 · TypeScript · 推送 2025-12-09 · [GitHub](https://github.com/sunls24/nextai) · [官网](https://next.sunls.de) · 个人维护 · 中文 README

**基于 Next.js 的 AI 聊天程序，支持函数调用与联网搜索**

一个 Next.js 实现的 AI 聊天 Web 应用：通过 OpenAI API 进行对话，支持 ChatGPT 函数调用机制，内置基于 Programmable Search Engine 的 Google 搜索插件。配置 OPENAI_API_KEY、可选的 OPENAI_BASE_URL（兼容代理或 OneAPI 地址）以及 Google 搜索相关密钥后，本地以 pnpm 安装依赖并运行开发服务器，也可通过 Vercel 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OpenAI API 的对话聊天
- 支持 ChatGPT 函数调用
- 内置 Google 搜索插件（Programmable Search Engine）
- 支持 Vercel 部署与 OPENAI_BASE_URL 自定义端点

## 适用场景

- 搭建一个可自定义 API 端点的个人 AI 聊天页面
- 体验带联网搜索的函数调用对话
- 通过 Vercel 快速部署聊天服务

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: 一个简单而优雅的 AI 聊天程序
> L5: 支持 ChatGPT **函数调用：**

## 星数曲线

```mermaid
xychart-beta
    title "sunls24/nextai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `fc8605f48cd4` · [字段定义](../../DATASET.md)*
