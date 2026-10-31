# Supahands/llm-comparison-backend

⭐ 23 · Python · Apache-2.0 · 推送 2026-01-13 · [GitHub](https://github.com/Supahands/llm-comparison-backend) · [官网](https://eval.supa.so) · 组织维护

**LLM 对比平台后端：运行 Ollama 与 LiteLLM 服务供前端对比模型**

LLM 对比平台的后端部分，通过 Modal serverless GPU 部署两个组件：Ollama API 服务器与 LiteLLM 服务器，供前端连接并获取不同模型做同提示词的头对头对比。附带 GGUF 转换器，可将 Hugging Face 模型经 llama.cpp 两步转换（FP16→量化），支持并行下载、进度跟踪、>10GB 大模型与 Modal 卷持久化，转换结果可上传至 Hugging Face 或 Ollama。需 Modal 账号登录，官方站点暂不支持 Anthropic 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条 modal deploy 命令同时拉起 Ollama API 服务器与 LiteLLM 服务器
- GGUF 转换器：FP16→多档量化（Q4_K_M/Q5_K_M 等），支持重要性矩阵与大模型分片
- 8 连接并行下载与 ETA 进度跟踪，Modal 卷持久化支持 >10GB 模型
- 量化模型可回传 Hugging Face 或 Ollama

## 适用场景

- 为 LLM 对比平台前端提供多模型接入服务
- 把 Hugging Face 模型转换并量化为 GGUF 供本地运行时使用
- 在 Modal serverless GPU 上托管模型服务

## 场景标签

`模型网关` `模型量化` · 领域:Agent 开发

## 证据(README 行号)

> L11:  This is an opensource project allowing you to compare two LLM's head to head with a given prompt, this section wil
> L51: There are two components to this project, the `ollama` api server as well as the `litellm` server which will be wha

## 星数曲线

```mermaid
xychart-beta
    title "Supahands/llm-comparison-backend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `67c8d49faa79` · [字段定义](../../DATASET.md)*
