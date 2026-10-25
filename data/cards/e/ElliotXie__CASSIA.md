# ElliotXie/CASSIA

⭐ 109 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/ElliotXie/CASSIA) · [官网](https://elliotxie.github.io/CASSIA/) · 组织维护 · 中文 README

**多智能体 LLM 单细胞细胞类型注释框架，供生信研究者使用**

CASSIA 用多智能体大语言模型对单细胞 RNA 测序数据做细胞类型注释：读取 Seurat FindAllMarkers 输出的 marker 数据，通过注释、质量评分与 AnnotationBoost（针对难注释簇）等智能体生成注释结果，并支持批量运行、聚类级别自动合并与自动基准评测。提供 Python 包（pip/CLI）、R 包（GitHub 安装）与在线 Web UI 三种使用方式。API 密钥仅需一个（推荐 OpenRouter），支持 OpenAI 兼容端点与 Ollama/LM Studio 本地模型；CLI 另可接入 Codex、Claude Code 等本地编码智能体后端。论文发表于 Nature Communications。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多智能体 LLM 注释流程，含质量评分与 AnnotationBoost 难簇优化
- 同时提供 R 包、Python 包/CLI 与 Web UI（cassia.bio）
- 支持 OpenRouter/OpenAI/Anthropic/DeepSeek 及 Ollama/LM Studio 本地模型
- 自动单细胞注释基准评测平台（准确率与成本）

## 适用场景

- 我用 Seurat 做完聚类后，让 LLM 智能体自动注释细胞类型
- 对多个聚类/子聚类批量注释并合并不同层级的结果
- 数据隐私敏感或无 API 预算时，用本地 Ollama 模型跑注释
- 比较不同 LLM 在单细胞注释任务上的表现与成本

## 场景标签

`多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: **CASSIA** (Collaborative Agent System for Single-cell Interpretable Annotation) is a tool that enhances cell type a
> L141: runCASSIA_batch(

## 星数曲线

```mermaid
xychart-beta
    title "ElliotXie/CASSIA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-25 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `313d0d33488d` · [字段定义](../../DATASET.md)*
