# Sinapsis-AI/sinapsis-langchain

⭐ 27 · Python · AGPL-3.0 · 推送 2026-04-23 · [GitHub](https://github.com/Sinapsis-AI/sinapsis-langchain) · 组织维护

**Sinapsis 框架的 LangChain 数据加载与文本切分模板包**

为 Sinapsis AI 框架提供 LangChain 集成的模块，将 LangChain community 数据加载器与文本切分器封装为 Sinapsis 模板，可在 Sinapsis Agent 的 YAML 配置中使用。拆分为 sinapsis-langchain-readers 与 sinapsis-langchain-splitters 两个子包，通过 uv/pip 从官方 PyPI 镜像源安装。每个加载器模板支持 add_document_as_text_packet 属性，其余属性经初始化字典动态分配。部分需额外配置的加载器（如 Twitter、Discord、AssemblyAI）被排除，留待后续版本。面向使用 Sinapsis 构建流水线的开发者，许可证为 AGPLv3 并另提供商业许可渠道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 LangChain community 数据加载器与文本切分器为 Sinapsis 模板
- 拆分 readers 与 splitters 两个子包，支持 pip/uv 安装
- CLI 命令列出模板名并生成示例 Agent 配置
- 列举了 11 个暂被排除的加载器（含 Oracle、Twitter、Discord 等）

## 适用场景

- 在 Sinapsis Agent 中加载 Wikipedia、PDF、CSV 等文档
- 在 Sinapsis 流水线里复用 LangChain 的文本切分能力
- 通过 YAML 配置组合文档加载与后续处理步骤

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L18: The `sinapsis-langchain` module adds support for the Langchain framework, in particular, Langchain community data l
> L67: The **Sinapsis Langchain** module provides wrapper templates for **Langchain's community data loaders**, making the

## 星数曲线

```mermaid
xychart-beta
    title "Sinapsis-AI/sinapsis-langchain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5cf5cbb3f8a0` · [字段定义](../../DATASET.md)*
