# bold84/cot_proxy

⭐ 50 · Python · MIT · 推送 2026-10-31 · [GitHub](https://github.com/bold84/cot_proxy) · 个人维护

**LLM API 代理：按模型定制参数、自动切换思考模式并过滤 think 标签**

位于客户端与 LLM API 之间的代理服务：通过环境变量 LLM_PARAMS 为不同模型（或伪模型名）配置采样参数覆盖、向提示追加 /think 或 /no_think、用流式缓冲过滤 <think> 标签、并用 upstream_model_name 做模型名替换。面向使用 Cline、RooCode 等不支持参数自定义应用的场景，无需修改客户端代码。以 Docker/Docker Compose 部署，Gunicorn 运行，提供健康检查与错误处理，配置经 .env 文件管理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按模型分组覆盖 LLM 采样参数并追加提示文本
- 流式响应中跨 chunk 过滤 <think> 标签
- 伪模型名映射到真实上游模型（upstream_model_name）
- Docker Compose 部署，Gunicorn 4 worker 运行

## 适用场景

- 让 Cline/RooCode 等无法设参的应用使用 Qwen3 思考模式
- 统一多个工具对同一 LLM 的调用参数
- 从模型输出中去除推理内容，只保留最终回答

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: Ever wished you had more control over how your applications interact with Large Language Models (LLMs)? **cot_proxy*
> L34: - **Smart Request Modification**: Automatically adjust parameters and append text to prompts
> L37: - **Streaming Support**: Works with both streaming and non-streaming responses


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 mid · 依据 README sha `1a029a86be87` · [字段定义](../../DATASET.md)*
