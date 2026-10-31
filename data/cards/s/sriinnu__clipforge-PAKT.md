# sriinnu/clipforge-PAKT

⭐ 20 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/sriinnu/clipforge-PAKT) · 个人维护

**面向 LLM 输入的确定性无损 token 压缩库（JSON/YAML/CSV/Markdown）**

将 JSON、YAML、CSV、Markdown 与文本转为管道分隔的紧凑形式以减少 BPE token 数：不运行模型、无推理开销、结果确定。L1–L3 三层为无损（decompress 逐字节还原），L4 语义层可选且有损。重复性/表格数据收益明显（实测 JSON 省 27–33%），深层嵌套小配置可能反而膨胀 +25%，prose 直接透传。提供库、CLI、MCP server、桌面应用与浏览器扩展；另有面向 agent 循环的上下文引擎（跨轮去重、共享字典、缓存前缀稳定）。核心库稳定发布，桌面/扩展端未充分验证，Python wrapper 未上 PyPI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- L1–L3 无损压缩，decompress 逐字节还原原始输入
- 基于真实 BPE tokenizer（gpt-tokenizer）的 tokenizer 感知打包
- MCP server 暴露 pakt_compress/pakt_auto 等 7 个工具
- 上下文引擎支持跨轮去重、共享 @dict 与 prompt-cache 前缀稳定

## 适用场景

- 降低发送给 LLM 的 JSON/日志/CSV 数据的 token 成本
- 在 agent 循环中压缩工具输出并跨轮去重
- 发送前用 pakt_inspect 判断载荷是否值得压缩

## 场景标签

 · 领域:LLM 基础设施/文本压缩

## 证据(README 行号)

> L5:  Lossless-first, model-free token compression for structured data sent to LLMs.
> L13: **PAKT** (Pipe-Aligned Kompact Text) converts JSON, YAML, CSV, Markdown, and text into a compact pipe-delimited for

## 星数曲线

```mermaid
xychart-beta
    title "sriinnu/clipforge-PAKT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `88fcb9f100f1` · [字段定义](../../DATASET.md)*
