# digitalocean/langchain-gradient

⭐ 16 · Python · MIT · 推送 2026-08-14 · [GitHub](https://github.com/digitalocean/langchain-gradient) · [官网](https://pypi.org/project/langchain-gradient/) · 组织维护

**LangChain 接入 DigitalOcean Gradient 推理的集成包**

提供 ChatGradient 聊天模型类，使 LangChain 应用可调用 DigitalOcean Gradient Serverless Inference 上托管的模型（示例使用 llama3.3-70b-instruct），支持 invoke 与流式输出，通过 DIGITALOCEAN_INFERENCE_KEY 环境变量配置访问凭据。1.0.0 版本以 pydo 替换已弃用的 gradient SDK（Gradient SDK 将于 2026-08-15 退役），timeout 参数改为 HTTP 连接/读取空闲超时（正整数，默认 120）。面向使用 Python 与 LangChain 的开发者，经 pip 安装。

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

- ChatGradient 模型类接入 DigitalOcean Gradient Serverless Inference
- 支持 invoke 调用与流式输出
- 1.0.0 迁移至 pydo SDK（原 gradient SDK 弃用）

## 适用场景

- 在 LangChain 应用中调用 DigitalOcean 托管的聊天模型
- 为已有 LangChain 代码接入云端推理服务

## 场景标签

 · 领域:LLM 基础设施/集成库

## 证据(README 行号)

> L4: This package contains the LangChain integration with DigitalOcean Gradient Serverless Inference.
> L37: from langchain_gradient import ChatGradient

## 星数曲线

```mermaid
xychart-beta
    title "digitalocean/langchain-gradient 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `828741fa3983` · [字段定义](../../DATASET.md)*
