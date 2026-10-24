# AtomFlow-AI/MoleCode

⭐ 308 · Python · MIT · 推送 2026-06-04 · [GitHub](https://github.com/AtomFlow-AI/MoleCode) · [官网](https://arxiv.org/pdf/2605.16480) · 组织维护 · 中文 README

**面向 LLM 的图显式分子表示语言库，让模型直接读写分子结构**

MoleCode 是一种以 Mermaid 图序列化的分子表示格式：原子与化学键为带持久标识符的类型化节点/边，通过 RDKit 与 SMILES/MOL/PSMILES 确定性无损互转，无需学习模型。以 Python 库形式提供，覆盖小分子、聚合物与 Markush 结构三个模块，并附带系统提示词、OpenAI 兼容客户端与可离线运行的示例脚本。同时打包为 Agent Skill，供 Claude Code、Codex 等编码代理经 CLI 转换、校验与编辑分子图。由 AtomFlow 维护，MIT 许可，附 arXiv 技术报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分子以显式图（节点/边+持久 ID）表示，与 SMILES/MOL 经 RDKit 确定性无损互转
- 统一语法覆盖小分子、聚合物（×n 重复单元）与 Markush 结构（缩写节点）
- 提供 Agent Skill 与 CLI，Claude Code / Codex 可直接使用，无需 MCP 服务器
- 内置 OpenAI 兼容轻量客户端，可配合 OpenAI/DeepSeek/vLLM/Ollama 等任意 LLM

## 适用场景

- 让编码代理在图级别理解、编辑与校验分子结构
- 为分子理解/生成/编辑/推理任务构建 LLM 评测脚本（默认离线打印提示词）
- 在化学 LLM 应用中用显式图表示替代 SMILES 字符串

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L33: **MoleCode makes the structure the language.** Every atom and bond is written as a typed declaration with a persist
> L146: MoleCode is a **drop-in representation for any LLM** — feed the grammar as a system prompt, hand the model a graph
> L219: MoleCode is the open representation layer underneath these products — making

## 星数曲线

```mermaid
xychart-beta
    title "AtomFlow-AI/MoleCode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 305 --> 309
    line [306, 308, 308]
```

2026-10-18 306 → 2026-10-24 308（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `72aa1f723009` · [字段定义](../../DATASET.md)*
