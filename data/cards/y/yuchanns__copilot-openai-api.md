# yuchanns/copilot-openai-api

⭐ 60 · Python · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/yuchanns/copilot-openai-api) · 个人维护

**把 GitHub Copilot 能力转为 OpenAI 兼容 API 的 FastAPI 代理服务**

基于 FastAPI 的代理服务器：将 GitHub Copilot 订阅的 chat completion、embeddings、responses 与 models 能力封装为 OpenAI 兼容的 /v1 端点，支持流式与非流式响应。使用前需 GitHub Copilot 订阅及由官方插件登录生成的 OAuth 配置文件（apps.json/hosts.json），服务自动管理令牌刷新并以 Bearer Token 鉴权。提供本地 PDM 运行与 Docker 两种部署方式，监听端口与 worker 数可配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 Copilot 能力输出为 OpenAI 兼容的 /v1/chat/completions、/v1/embeddings、/v1/responses 端点
- 支持流式与非流式两种响应模式
- 自动令牌管理与刷新，内置 CORS 与 Bearer Token 鉴权
- 提供本地运行与 Docker 容器两种部署方式

## 适用场景

- 让支持 OpenAI API 格式的客户端调用 GitHub Copilot 的模型能力
- 在已有应用中复用 Copilot 订阅作为 LLM 接口
- 通过统一鉴权端点对外提供 chat/embeddings 服务

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L10: A FastAPI proxy server that seamlessly turns GitHub Copilot's chat completion/embeddings/responses capabilities int
> L117: curl -X POST http://localhost:9191/v1/chat/completions \
> L177: ### POST /v1/chat/completions

## 星数曲线

```mermaid
xychart-beta
    title "yuchanns/copilot-openai-api 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-29 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `12d03da24563` · [字段定义](../../DATASET.md)*
