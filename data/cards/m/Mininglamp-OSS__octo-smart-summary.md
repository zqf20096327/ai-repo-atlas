# Mininglamp-OSS/octo-smart-summary

⭐ 34 · Go · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/Mininglamp-OSS/octo-smart-summary) · [官网](https://github.com/Mininglamp-OSS) · 组织维护 · 中文 README

**OCTO 协作平台的 LLM 对话摘要微服务**

用 Go 编写的小型服务，封装 OpenAI 兼容 LLM 端点，面向 OCTO 生态：给定会话 ID（channel/thread/meeting），从 octo-server 获取转录文本，经分块、提示、结构化解析、元数据增强的流水线，产出含关键决策、待答问题与跟进候选的严格 JSON 摘要，可移交 octo-matter 生成待办草稿。提供 4 个端点（含流式），LLM 端点通过 LLM_API_URL 配置，支持 vLLM/Ollama/商业 API 等后端，无用户状态。

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

- 4 个端点的窄接口（/summarise、/summarise/stream、/healthz、/metrics）
- LLM_API_URL 可指向任意 OpenAI 兼容端点（vLLM/Ollama/Claude 网关/商业 API）
- 结构化 JSON 输出：要点、决策、待答问题、候选行动
- 摘要流水线：取转录→分块→提示（brief/standard/decision-log 三模式）→解析校验→元数据增强

## 适用场景

- 把 OCTO 群聊、长线程或会议转录自动变成可扫读的简报
- 从对话中提取关键决策与跟进事项并转为待办草稿
- 以自托管 LLM 后端为团队提供对话摘要服务

## 场景标签

 · 领域:LLM 应用/协作工具

## 证据(README 行号)

> L21: `octo-smart-summary` is a small Go service that wraps an OpenAI-compatible
> L30: - **Bring your own LLM.** The LLM URL is a configurable `LLM_API_URL`; point it at any OpenAI-compatible endpoint (

## 星数曲线

```mermaid
xychart-beta
    title "Mininglamp-OSS/octo-smart-summary 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `55a0c0bf42d3` · [字段定义](../../DATASET.md)*
