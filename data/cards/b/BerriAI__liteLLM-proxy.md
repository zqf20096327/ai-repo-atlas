# BerriAI/liteLLM-proxy

⭐ 288 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/BerriAI/liteLLM-proxy) · 组织维护

**统一代理服务：用 OpenAI 格式调用 50+ 个 LLM 模型接口**

一个本地或云端部署的 LLM 代理服务器：将 /chat/completions 请求转发到 Azure、OpenAI、Anthropic、Replicate、Hugging Face 等 50+ 模型 API，统一输入输出为 OpenAI 格式，提供模型回退的错误处理、语义缓存、流式与异步响应、token 用量与花费统计，并可把请求/响应/错误日志写入 Supabase、Posthog、Sentry 等多种日志服务。面向需要统一管理多模型接入的开发者；README 声明项目已迁移至 LiteLLM 主仓库，本仓库为旧地址。

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

- 以 OpenAI 格式（completion(model, messages)）统一调用 50+ 模型
- 模型回退错误处理（如 GPT-4 失败自动尝试 llama2）
- 语义缓存与流式/异步支持
- 日志接入 Supabase/Posthog/Mixpanel/Sentry/Helicone 等多种服务

## 适用场景

- 为应用提供统一的多模型 API 网关
- 按模型统计 token 用量与花费
- 通过模型回退提高请求成功率

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L1: # liteLLM Proxy Server: 50+ LLM Models, Error Handling, Caching
> L36: - Make `/chat/completions` requests for 50+ LLM models **Azure, OpenAI, Replicate, Anthropic, Hugging Face**
> L48:  - Call all models using the OpenAI format - `completion(model, messages)`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `1992eaea8d44` · [字段定义](../../DATASET.md)*
