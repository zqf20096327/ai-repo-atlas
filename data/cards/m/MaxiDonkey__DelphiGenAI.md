# MaxiDonkey/DelphiGenAI

⭐ 86 · Pascal · MIT · 推送 2026-06-10 · [GitHub](https://github.com/MaxiDonkey/DelphiGenAI) · 个人维护

**Delphi 的 OpenAI API 封装库：同步/异步调用全套端点**

非官方的 Delphi OpenAI API 封装（wrapper），按一对一映射原则覆盖 OpenAI 平台端点：chat/completions、responses、音频、图像生成、embeddings、batch、fine-tuning、vector stores、realtime、skills 等。提供同步/异步/promise 三种执行模型、SSE 流式回调、函数调用与内置工具（web search、code interpreter、远程 MCP 等）。同一 IGenAI 客户端可指向 OpenAI、本地 LM Studio 服务器、Google Gemini 或任何 OpenAI 兼容端点。用 Delphi 12 编写，MIT 许可，附 FMX 演示应用（Pythia UI）。限制：不引入厂商特定扩展；Assistants API 与 Sora video 已在 2.0.0 移除。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 OpenAI 多数端点的一对一映射，含 responses/skills/containers
- 同步、异步、promise 三种执行模型与 SSE 流式回调
- 同一客户端可切换 OpenAI、LM Studio、Gemini 及 OpenAI 兼容端点
- 附带 FMX 功能演示（含上下文重建、RAG、Whisper 语音输入）

## 适用场景

- 在 Delphi 应用中接入 OpenAI 的对话、视觉与音频能力
- 通过本地 LM Studio 服务器运行模型而复用同一套代码
- 构建带函数调用与内置工具的 agentic 工作流
- 用 OpenAI 兼容端点对接 Gemini 等其他厂商

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L67: **DelphiGenAI** is a full OpenAI wrapper for Delphi, covering the entire platform: text, vision, audio, image gener
> L85: DelphiGenAI is, by design, a **strict one-to-one mapping of the OpenAI API**: it does not introduce provider-specif

## 星数曲线

```mermaid
xychart-beta
    title "MaxiDonkey/DelphiGenAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-27 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e8f56ef9cdca` · [字段定义](../../DATASET.md)*
