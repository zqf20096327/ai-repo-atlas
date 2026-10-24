# savannah-i-g/TSUKUYOMI

⭐ 95 · NOASSERTION · 推送 2026-04-28 · [GitHub](https://github.com/savannah-i-g/TSUKUYOMI) · 个人维护

**面向 LLM 的情报分析提示工程框架（JSON 模块化）**

一个以 .tsukuyomi JSON 模块组成的提示工程框架，设计用于加载到 Claude、GPT、Gemini 等大模型中，提供按情报界标准（ICD 203/206）组织的 OSINT、经济、战略等多域分析工作流：含核心编排引擎定义、人格核（默认 AMATERASU）、会话状态导入导出与幻觉检测声明。安装方式为 git clone 后在 Claude Code 中激活，或作为项目知识库上传到各 AI 平台；作者在开头声明此为早期实验且『已经非常老旧』，伪代码方法可能仅偶然生效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- JSON 模块化组件架构，含依赖管理与版本兼容
- 覆盖 OSINT/经济/战略等多域分析的模块目录（E 系列、S 系列）
- 声明兼容 Claude Code、GPT、Gemini、Copilot Studio 等平台的加载方法
- 会话状态导出/导入与分析连续性支持

## 适用场景

- 把框架文件作为知识库载入 Claude/Gemini/ChatGPT 执行结构化情报分析
- 在 Claude Code 中通过 git 集成运行模块化分析工作流
- 企业内经 Copilot Studio 部署带该知识库的自定义 agent

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L21: The system is designed as a prompt engineering framework optimized for large language models, providing structured 
> L38: - **LLM-Optimized**: Native integration with Claude Code, GPT, Gemini, and other AI platforms

## 星数曲线

```mermaid
xychart-beta
    title "savannah-i-g/TSUKUYOMI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-24 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f0638bd5eeca` · [字段定义](../../DATASET.md)*
