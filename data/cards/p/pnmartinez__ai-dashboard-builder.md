# pnmartinez/ai-dashboard-builder

⭐ 24 · Python · NOASSERTION · 推送 2026-03-01 · [GitHub](https://github.com/pnmartinez/ai-dashboard-builder) · 组织维护

**上传数据由 LLM 自动生成可视化仪表盘的 Web 应用**

本地或自托管的数据可视化 Web 应用：用户通过导入向导上传数据集（可按行/列预览与过滤），由 LLM 推断相关过滤器、按 KPI 优先级生成图表与仪表盘；支持本地 Ollama 模型或第三方 API（OpenAI/Anthropic/Groq）。每个仪表盘输出可复用的 viz_spec JSON，各图表含可复现代码标签页。提供 Docker Compose、含 Ollama 的一体化部署与手动运行三种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 根据 KPI 提示动态推断过滤器并生成仪表盘
- 通过 Ollama 使用本地 LLM 处理私有数据
- 数据导入向导支持按行/列预览与过滤
- 每个仪表盘生成可复用的 viz_spec JSON，图表附可复现代码

## 适用场景

- 把 CSV 等数据集交给 AI 快速生成交互式仪表盘
- 私有数据场景下用本地 Ollama 模型生成可视化
- 复用历史 viz_spec 规格重建图表并在他处复现代码

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L12:  - KPI-directed: Prompt the LLMs to prioritize your KPIs in the dataset,
> L14:  - Dynamic filters: the LLM infers the most relevant filters for your dataset dynamically,

## 星数曲线

```mermaid
xychart-beta
    title "pnmartinez/ai-dashboard-builder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4fbd2e8bde5b` · [字段定义](../../DATASET.md)*
