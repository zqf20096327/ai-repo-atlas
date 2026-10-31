# DanielPFlorian/ComfyUI-WorkflowGenerator

⭐ 42 · Python · GPL-3.0 · 推送 2025-11-22 · [GitHub](https://github.com/DanielPFlorian/ComfyUI-WorkflowGenerator) · 个人维护

**用自然语言生成 ComfyUI 工作流的自定义节点套件**

ComfyUI 自定义节点，基于 ComfyGPT 研究的独立实现：用户以自然语言描述目标（如“创建一个 SDXL 文生图工作流”），经三阶段流水线——Generator 生成逻辑图 JSON、Validator 基于本地节点目录或语义嵌入校验节点名、Builder 编译为可执行的 ComfyUI 工作流 JSON。使用 Qwen2.5-14B 微调模型（GGUF q8_0 量化）、MiniLM 嵌入模型与 Qwen2.5-7B 校验模型（可选）。限制：模型知识受训练数据截止约束，无法识别之后发布的自定义节点，建议人工监督。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段流水线：生成→校验→构建，各阶段可单独干预
- Qwen2.5-14B 微调工作流生成模型，GGUF 量化本地推理
- NodeValidator 支持语义搜索与 LLM 修正两种模式
- UpdateNodeCatalog 扫描并编目本地全部节点（原生与自定义）

## 适用场景

- 用一句话描述需求自动搭出 ComfyUI 工作流
- 快速搭建 SDXL 文生图等标准工作流
- 校验生成工作流中的节点名与本地安装匹配

## 场景标签

`工作流自动化` `图像生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: Generate ComfyUI workflows from natural language descriptions using Large Language Models (LLMs).
> L24: This implementation uses a specialized LLM fine-tuned on workflow data to execute a three-stage pipeline:
> L25: 1. **Generator:** Interprets the natural language prompt to generate a logical graph structure (JSON).

## 星数曲线

```mermaid
xychart-beta
    title "DanielPFlorian/ComfyUI-WorkflowGenerator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `cf3ace7c26f5` · [字段定义](../../DATASET.md)*
