# cloud-apim/otoroshi-llm-extension

⭐ 19 · Scala · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/cloud-apim/otoroshi-llm-extension) · [官网](https://cloud-apim.github.io/otoroshi-llm-extension/) · 组织维护

**Otoroshi 的 LLM 网关扩展：统一/兼容 OpenAI 的 API 管理多模型**

一组 Otoroshi 插件与资源，通过统一且兼容 OpenAI 的 API 接入、配置、保护和管理 LLM：支持 50+ 提供商，提供负载均衡、自动故障切换与重试、语义缓存、按消费者的配额管理、API key 密钥库、请求审计与导出、细粒度授权、提示词与响应的护栏校验、提示词模板库，并支持多模态模型（TTS/STT/图像/视频生成）、嵌入计算、向量存储检索、持久化会话记忆与基于工作流的 agentic 编排。运行要求 JDK17+，面向使用 Otoroshi 的开发与运维团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 50+ LLM 提供商接入，统一/兼容 OpenAI 的 API
- 负载均衡、故障切换、自动重试与语义缓存
- 按消费者的配额管理、审计导出与细粒度授权
- 支持多模态（TTS/STT/图像/视频）、嵌入、向量存储与 agentic 工作流

## 适用场景

- 用统一 API 网关接入多家 LLM 提供商
- 对内部消费者的 LLM 调用做配额、审计与授权管控
- 在故障时自动切换模型并缓存重复请求以降低成本

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Connect, setup, secure and seamlessly manage LLM models using an Universal/OpenAI compatible API**
> L25: Otoroshi LLM Extension is set of Otoroshi plugins and resources to interact with LLMs. To know more about it, go to

## 星数曲线

```mermaid
xychart-beta
    title "cloud-apim/otoroshi-llm-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5e396719a2b9` · [字段定义](../../DATASET.md)*
