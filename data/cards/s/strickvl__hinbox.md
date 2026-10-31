# strickvl/hinbox

⭐ 16 · Python · 推送 2026-10-25 · [GitHub](https://github.com/strickvl/hinbox) · 个人维护

**面向历史学者的领域可配置实体抽取系统**

处理历史文献、学术论文、新闻与图书章节，抽取人物、组织、地点、事件的结构化信息并构建带引用的实体档案。通过配置文件定义研究领域（无需编码），支持云端模型（Gemini/OpenAI/Anthropic/OpenRouter）与本地 Ollama。机制包括 RapidFuzz+嵌入的实体去重、二次 LLM 仲裁、五层规范名选择、档案版本追踪与引用核验、抽取缓存与并行流水线。提供 FastHTML Web 界面与模型评测记分板。数据需为 Parquet 格式；安装依赖 Python 3.12+、uv 与 just。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 配置文件定义研究领域，无需 Python 编码
- RapidFuzz 词法分块 + 嵌入相似度的实体去重与 LLM 仲裁
- 带引用核验的档案版本追踪与确定性 QC 自动重试
- 模型评测记分板（relevance/merge/profile-update）

## 适用场景

- 从历史文献批量抽取人物/组织/地点/事件并去重合并
- 为研究主题构建可溯源的实体档案库
- 对比云端与本地模型在自己标注数据上的表现

## 场景标签

`科研工具` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: `hinbox` is a flexible, domain-configurable entity extraction system designed
> L17: - **Entity Extraction**: Automatically extract people, organizations, locations, and events

## 星数曲线

```mermaid
xychart-beta
    title "strickvl/hinbox 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9a92113d8259` · [字段定义](../../DATASET.md)*
