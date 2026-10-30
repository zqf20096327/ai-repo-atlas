# PriceNing/LLM-AIO-Gateway

⭐ 45 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/PriceNing/LLM-AIO-Gateway) · 个人维护 · 中文 README

**统一 LLM API 网关：多协议代理多提供商并注入视觉能力**

基于 FastAPI 的统一 LLM API 网关，同时暴露 OpenAI Chat Completions、旧版 Completions、Anthropic Messages、OpenAI Responses 与 Images 接口，代理多个 OpenAI 兼容（经 liteLLM）与 Anthropic 兼容上游。所有协议先转为统一内部消息格式（IR），共享策略层完成路由、reasoning 缓存、工具调用修复与断路器，支持按用户/Key/模型通配符的主动路由和按失败类型的被动 fallback。特色包括视觉模型注入（视觉模型生成图片描述后替换为文本，让纯文本模型处理图片）、图像生成后端（含 ComfyUI 工作流导入）、Web 管理面板与 SQLite 存储。面向需要聚合多上游、统一鉴权与多协议兼容的开发者/团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时暴露 OpenAI Chat/Completions、Anthropic Messages、Responses、Images 等多协议端点
- 统一内部 IR + 结构化 RoutingDecision，主动路由与按失败类型的被动 fallback 链
- 视觉模型注入：图片转文本描述，使纯文本模型可处理图片上下文
- 工具调用修复、reasoning_content 缓存回传与工具调用循环断路器
- Web 管理面板管理提供商/用户/Key/路由规则，SQLite 存储

## 适用场景

- 用一个网关聚合多个 OpenAI/Anthropic 兼容上游并统一发 Key
- 让 Claude Code、Codex、OpenCode 等客户端经同一网关访问不同模型
- 给纯文本模型加图片理解能力（视觉模型注入）
- 配置全局生图后端（含 ComfyUI 工作流）供聊天模型调用

## 场景标签

`模型网关` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L6: LLM AIO Gateway 是一个基于 FastAPI 的统一 LLM API 网关，用一个服务代理多个 OpenAI 兼容和 Anthropic 兼容的上游提供商。它同时暴露 OpenAI Chat Completions、旧
> L8: 当前代理核心基于统一内部消息格式：所有客户端协议先转换为 `InternalRequest` / `InternalMessage`，再进入共享策略层。策略层会产出结构化 `RoutingDecision`，随后由上游适配器发送给 
> L14: |统一协议网关|支持 `/chat/completions`、`/completions`、`/messages`、`/responses`、`/models`，同时挂载在根路径和 `/v1` 前缀。|

## 星数曲线

```mermaid
xychart-beta
    title "PriceNing/LLM-AIO-Gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-30 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d3ba0fc25776` · [字段定义](../../DATASET.md)*
