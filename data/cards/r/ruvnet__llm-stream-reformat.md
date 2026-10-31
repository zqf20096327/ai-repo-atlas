# ruvnet/llm-stream-reformat

⭐ 21 · Rust · MIT · 推送 2026-08-17 · [GitHub](https://github.com/ruvnet/llm-stream-reformat) · 个人维护

**对流式 LLM 输出做实时整形：分离思考与回答**

Rust + WASM 实现的流式文本转换库：在 token 仍到达的过程中，将推理模型的思考流与回答分离到不同通道、用 midstream temporal-compare 的 EditDistance 相似度折叠近似重复片段、归一化空白。支持解析 Google Vertex（parts[].thought）、OpenRouter（delta.reasoning）与 meta-llm（OpenAI 兼容 delta.content）三种 SSE 方言，归一为通用 chunk 流。面向 Node、浏览器（WASM）与 Rust 场景，逐 chunk O(1) 处理、不缓冲整段响应；仅做转换，不生成内容，也不处理水印。

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

- 思考/回答双通道分离，可单独展示或隐藏推理
- 基于 EditDistance 相似度折叠近似重复（口吃/循环产物）
- 三种 Provider SSE 方言归一为通用 StreamChunk
- 逐 chunk O(1) 流式处理，Node/浏览器/Rust 三端可用

## 适用场景

- 在 UI 中单独展示或隐藏推理模型的思考过程
- 清理推理模型输出中的重复循环与混乱空白
- 统一多家 Provider 的流式格式便于前端消费

## 场景标签

 · 领域:LLM 基础设施/流处理

## 证据(README 行号)

> L25: Reasoning models (like `gemini-3.7-flash`) **interleave a hidden thought stream with the answer**, stutter into rep

## 星数曲线

```mermaid
xychart-beta
    title "ruvnet/llm-stream-reformat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `856447a958b6` · [字段定义](../../DATASET.md)*
