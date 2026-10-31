# sandner-art/ArtAgents

⭐ 17 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/sandner-art/ArtAgents) · 个人维护

**面向艺术创作者的 LLM 提示工程与图像描述生成工具**

基于 Gradio 5 的原型框架，供艺术家、设计师实验 LLM 提示工程与创意内容生成：通过预定义或自定义 Agent 与多 Agent 'Teams' 工作流生成提示词、描述和图像字幕，依赖本地运行的 Ollama 实例提供文本与多模态模型（Python 3.11+，从源码克隆运行）。支持图像生成（ComfyUI/Forge/A1111/SD.Next 后端）、批量字幕导出 metadata.jsonl/csv、跨多个 Team 与模型的实验 Sweep。版本处于 alpha 阶段，部分功能（如 Ollama 图像生成后端）标注实验性或待上游恢复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 预定义/自定义 Agent 与多 Agent Teams 顺序工作流（多种结果组装策略）
- 图像字幕批量生成并可导出 metadata.jsonl/csv 供训练工具使用
- 实验 Sweep：跨多个 Team 与模型系统运行基础提示并保存 JSON 协议
- 图像生成支持 ComfyUI / Forge / A1111 / SD.Next 后端

## 适用场景

- 为艺术创作迭代和生成详细提示词
- 为图像数据集批量生成和编辑字幕
- 系统对比不同 Agent 组合与模型的提示产出

## 场景标签

`提示工程` `图像生成` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: ArtAgents is a prototype framework designed for artists, designers, and creators to experiment with LLM-based prompt
> L11: Select predefined agents, load custom agents, or utilize multi-agent "Teams" to generate detailed prompts, descript
> L63: * **Image Captioning:** Dedicated tab to load images from a folder, view/edit associated `.txt` caption files, save

## 星数曲线

```mermaid
xychart-beta
    title "sandner-art/ArtAgents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `78dc60089279` · [字段定义](../../DATASET.md)*
