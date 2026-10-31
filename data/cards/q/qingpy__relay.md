# qingpy/relay

⭐ 14 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/qingpy/relay) · 个人维护 · 中文 README

**浏览器中运行的个人 LLM 聊天界面，自托管、数据单文件**

基于 Hono/React/TypeScript 的自托管网页聊天应用，面向个人用户，通过 OpenAI 兼容 API 或 Google Vertex AI 服务账号接入模型。数据存储为磁盘上的一个 JSON 文件，网络活动仅限模型调用与可选的 WebDAV 同步；密钥存于独立文件，支持本地备份目录与环境变量配置。提供 Docker、Node 20+ zip 包与源码三种运行方式，默认仅本机可访问，无 HTTP 认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据为单个 JSON 文件，密钥独立存放
- 支持 OpenAI 兼容 API 与 Google Vertex AI 服务账号接入
- 可选 WebDAV 同步与本地备份目录
- Docker / Node zip / 源码三种运行方式

## 适用场景

- 个人在本地或私有服务器托管 LLM 聊天界面
- 用一份 JSON 文件管理与迁移聊天数据
- 通过 OpenRouter 等 OpenAI 兼容服务调用模型

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: Personal LLM chat in the browser. OpenAI-compatible APIs and Google Vertex AI.
> L6: Data is one JSON file on disk; the network is model calls and optional WebDAV.

## 星数曲线

```mermaid
xychart-beta
    title "qingpy/relay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e164af070f69` · [字段定义](../../DATASET.md)*
