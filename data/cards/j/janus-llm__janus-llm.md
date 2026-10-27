# janus-llm/janus-llm

⭐ 42 · Python · Apache-2.0 · 推送 2026-03-03 · [GitHub](https://github.com/janus-llm/janus-llm) · [官网](https://janus-llm.github.io/janus-llm/) · 组织维护

**用 LLM 辅助遗留 IT 系统现代化的代码翻译与分析工具**

MITRE 维护的 Python 包与 CLI 工具（janus），用 LLM 辅助遗留系统现代化：将 100+ 种语言的代码分块放入 Chroma 向量数据库；用 LLM 逐文件做编程语言间翻译；经 Ghidra 反编译将二进制文件翻译为编程语言；从源码生成需求、UML 图、注释与摘要；并支持对生成产物做评估。提供 pip 安装与源码（poetry）安装两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 100+ 种编程语言做适配模型上下文窗口的代码分块并入库 Chroma
- 基于 LLM 的文件级编程语言间翻译
- 经 Ghidra 反编译实现二进制到编程语言的翻译
- 从源码生成需求、UML 图、注释与摘要，并可评估生成产物

## 适用场景

- 将遗留系统代码翻译到现代编程语言
- 为存量代码补齐需求文档、UML 图与注释
- 对二进制产物经反编译后做语言翻译

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L19: Janus (`janus-llm`) uses LLMs to aid in the modernization of legacy IT systems. The repository can currently do the
> L21: 1. Chunk code of over 100 programming languages to fit within different model context windows and add to a Chroma v
> L22: 2. Translate from one programming language to another on a file-by-file basis using an LLM.

## 星数曲线

```mermaid
xychart-beta
    title "janus-llm/janus-llm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `84d80e42f244` · [字段定义](../../DATASET.md)*
