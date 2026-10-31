# amahi2001/python-token-killer

⭐ 14 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/amahi2001/python-token-killer) · 个人维护

**零依赖 Python 库：压缩任意 Python 对象以减少 LLM token**

ptk 接收任意 Python 对象，自动检测内容类型（dict/list/code/log/diff/text）并应用对应压缩策略：递归剥离 null/空容器、折叠重复日志行、提取代码签名、缩写冗长词汇等，实测节省 10-90% token。零必需依赖（stdlib 实现），tiktoken 可选用于精确计数；设计上不抛异常、不变异输入、线程安全。面向在 RAG、agent 工作流中压缩送入 LLM 上下文的开发者。

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

- 自动类型检测，单次调用压缩任意 Python 对象
- dict/code/log/diff/text 五类策略，实测节省 10-90% token
- 零必需依赖、不抛异常、不变异输入、线程安全
- 提供 minimize/stats API 与模块可调用简写，361 个测试

## 适用场景

- RAG 检索文档进入 prompt 前压缩上下文
- LangGraph/LangChain agent 循环中压缩工具输出
- 万行 CI 日志折叠为错误与堆栈后再交给 LLM 分析

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L80: ### RAG pipeline: compress retrieved docs before they hit the prompt
> L93: ### LangGraph / LangChain: compress tool outputs between nodes
> L4:  One call. Any Python object. Fewer tokens.

## 星数曲线

```mermaid
xychart-beta
    title "amahi2001/python-token-killer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `697989690c1e` · [字段定义](../../DATASET.md)*
