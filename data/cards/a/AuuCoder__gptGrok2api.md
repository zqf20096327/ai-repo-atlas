# AuuCoder/gptGrok2api

⭐ 294 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/AuuCoder/gptGrok2api) · [官网](https://muyuai.top) · 个人维护 · 中文 README

**自托管 GPT/Grok 统一网关：订阅账号转 OpenAI 兼容 API**

自托管网关，将已接入的 GPT 与 Grok 订阅账号转换为 OpenAI/Anthropic 兼容 API，提供 /v1 按模型分流与 /grok/v1 独立入口。围绕账号运营提供注册中心（临时邮箱、Outlook Token、iCloud Privacy Mail）、账号池调度、额度同步、后台探测与自动恢复、代理轮换（WARP/Privoxy/FlareSolverr）、本地 Turnstile 打码，以及覆盖账号、代理、日志、图片管理的 Vue3 控制台。部署以 Docker Compose 为主，数据后端支持 JSON/SQLite/PostgreSQL/Git。

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

- 提供 Chat Completions、Responses、Images、Anthropic Messages 兼容入口
- 内置 Grok 账号池、SSO 失效重登与 OAuth 自动恢复队列
- 注册中心整合临时邮箱、Outlook Token、iCloud Privacy Mail 等邮箱来源
- 内置 Captcha Solver 在 Docker/Xvfb 中处理 Grok Turnstile

## 适用场景

- 把已有的 GPT/Grok 订阅账号汇聚成统一 API 供程序调用
- 批量注册并管理 GPT/Grok 账号池与邮箱
- 需要代理轮换与账号存活探测的长时间运行网关

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: GPTGrok2API 是一个自托管的 GPT 与 Grok 统一网关，将已接入的订阅账号能力转换为 OpenAI 兼容 API，并提供账号、代理、注册、日志、图片和运行状态管理控制台。
> L31: |统一 API 网关|合并 GPT、Grok SSO 与 Grok Build OAuth 模型目录；根 `/v1` 根据模型自动分流，同时保留 `/grok/v1` 完整 Grok 接口。|
> L32: |协议兼容|提供 Chat Completions、Responses、Images、Anthropic Messages 兼容入口，支持流式与非流式响应、工具调用、搜索和推理强度。|

## 星数曲线

```mermaid
xychart-beta
    title "AuuCoder/gptGrok2api 星数(近 15 点)"
    x-axis ["2026-10-25", "2026-10-27", "2026-10-28", "2026-10-30", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-15", "2026-11-20", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 284 --> 295
    line [285, 286, 287, 288, 289, 285, 288, 291, 292, 291, 292, 293, 292, 293, 294]
```

2026-10-25 285 → 2026-11-27 294（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `2b60631f4282` · [字段定义](../../DATASET.md)*
