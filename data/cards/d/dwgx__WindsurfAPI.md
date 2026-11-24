# dwgx/WindsurfAPI

⭐ 3,159 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/dwgx/WindsurfAPI) · [官网](https://dwgx.github.io/WindsurfAPI/) · 个人维护 · 中文 README

**把 Windsurf/Devin 云端模型转成 OpenAI/Anthropic/Gemini 兼容 API 的自托管网关**

自托管反向代理网关（Node.js，零 npm 运行时依赖，端口 3003），将部署者自有 Windsurf/Devin 账号通过本地 Language Server 的 gRPC 协议接入，同时暴露 OpenAI Chat/Completions/Responses、Anthropic、Gemini 四套兼容端点。维护账号池并做轮询、速率限制与故障转移。使用前提是部署者自行提供上游账号（BYO-account），项目声明不提供、不出售账号或订阅。提供 git/Docker 部署、Dashboard 加账号、一键更新脚本与环境变量配置。

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

- 同时暴露 OpenAI Chat/Completions/Responses、Anthropic、Gemini 四套兼容 API 端点
- 通过本地 Language Server 将请求翻译为 Windsurf 内部 gRPC 协议
- 账号池自动轮询、速率限制与故障转移
- Docker 一键更新脚本支持健康检查与自动回滚

## 适用场景

- 让 Claude Code / Cline / Cursor 直接连自建网关调用 Windsurf 云端模型
- 用 OpenAI SDK 或 Gemini SDK 无改代码接入自有 Windsurf 账号
- 多账号场景下做故障切换与健康检查

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L54: WindsurfAPI 是一个独立的、开源的、自托管协议兼容网关，用于将部署者**自己拥有或获授权使用的 Windsurf / Devin 账号能力**接入 OpenAI、Anthropic 和 Gemini 兼容客户端。
> L92: 2. 把请求翻译成 Windsurf 内部 gRPC 协议，通过本地 Language Server 发给 Windsurf 云

## 星数曲线

```mermaid
xychart-beta
    title "dwgx/WindsurfAPI 星数(近 26 点)"
    x-axis ["2026-10-21", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-24"]
    y-axis "stars" 3093 --> 3165
    line [3099, 3105, 3106, 3108, 3107, 3108, 3107, 3109, 3112, 3115, 3119, 3108, 3127, 3130, 3132, 3133, 3134, 3135, 3138, 3142, 3148, 3149, 3153, 3156, 3159, 3159]
```

2026-10-21 3,099 → 2026-11-24 3,159（+60）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `e31f82955231` · [字段定义](../../DATASET.md)*
