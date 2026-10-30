# Ovid/ananta

⭐ 26 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/Ovid/ananta) · 个人维护

**让 AI 主动读代码库/文档集并给出带引用回答的工具**

面向需要对大型文档集合或代码库做深度问答的用户：基于 Recursive Language Models 技术，让 LLM 在 Docker 沙箱中编写 Python 代码主动读取、搜索、交叉引用文档，迭代直至给出带引用的回答，规避上下文窗口限制。支持通过 LiteLLM 接入 100+ LLM 提供商（含本地 Ollama），提供 Python 库、CLI/TUI、Document Explorer 与 arXiv Explorer 网页界面。自述为 Alpha 阶段，相比 RAG 更慢、消耗更多 token；执行需 Python 3.12+ 与 Docker 沙箱容器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 在 Docker 沙箱中写 Python 代码迭代探索文档直至给出带引用回答
- 支持 100+ LLM 提供商（LiteLLM），可用本地 Ollama 免 API key
- 可摄取整个 git 仓库做代码分析，输出 file:line 级引用
- 提供 Document Explorer/arXiv Explorer 网页界面与 CLI/TUI

## 适用场景

- 跨大量文档做多文档推理问答并获得可验证引用
- 对整个代码仓库做深度分析并追踪跨文件逻辑
- 本地用 Ollama 私密查询自己的文档集合

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L7: Ananta lets AI explore your documents, even large codebases, the way a researcher would: reading, searching, cross-r
> L234: 2. **Query**: Your question is sent to the LLM with a sandboxed Python REPL
> L236: 4. **Execute**: Code runs in an isolated Docker container

## 星数曲线

```mermaid
xychart-beta
    title "Ovid/ananta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ad2750033820` · [字段定义](../../DATASET.md)*
