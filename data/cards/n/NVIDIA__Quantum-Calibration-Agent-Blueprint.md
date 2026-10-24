# NVIDIA/Quantum-Calibration-Agent-Blueprint

⭐ 73 · TypeScript · Apache-2.0 · 推送 2026-09-23 · [GitHub](https://github.com/NVIDIA/Quantum-Calibration-Agent-Blueprint) · 组织维护

**面向量子器件校准实验的 AI agent 参考蓝图**

NVIDIA Ising 项目下的量子器件校准 agent 蓝图：通过自然语言或结构化工作流发现、执行和分析量子校准实验，内置验证的多步工作流引擎、基于 VLM 的图表视觉分析、HDF5 与 SQLite 数据管理。提供 TUI、Web UI 聊天界面与 CLI 三种交互方式，支持 NVIDIA、Anthropic、OpenAI 多家 LLM 提供商。运行需 Python 3.11+，Web UI 另需 Node.js 18+ 与 npm 9+。采用 Apache 2.0 许可。

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

- 自然语言驱动实验发现、执行与多步工作流自动化
- VLM 视觉分析实验图表与数据
- HDF5/SQLite 实验结果存储与历史追踪
- 提供 TUI、Web UI、CLI 三种交互界面

## 适用场景

- 用对话方式查找并运行量子校准实验
- 编排带状态跟踪的多步校准工作流
- 让 VLM 检查校准实验产出的图表数据

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6: Part of NVIDIA Ising. This is a reference agent blueprint for AI-powered quantum device calibration. It provides an 
> L20: - **Visual Analysis**: Inspect plots and data using vision language models (VLMs)

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/Quantum-Calibration-Agent-Blueprint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 72 --> 74
    line [73, 73]
```

2026-10-18 73 → 2026-10-24 73（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5d4ae0bbbfef` · [字段定义](../../DATASET.md)*
