# OSU-NLP-Group/Explorer

⭐ 28 · Python · MIT · 推送 2026-02-17 · [GitHub](https://github.com/OSU-NLP-Group/Explorer) · [官网](https://osu-nlp-group.github.io/Explorer/) · 组织维护

**为多模态 Web Agent 合成探索式训练轨迹并训练评测的代码库**

ACL 2025 Findings 论文 Explorer 的官方代码库，由俄亥俄州立大学与微软研究院合作。核心机制是探索驱动的网页操作轨迹合成（Trajectory Synthesis），用合成的轨迹训练 Qwen2-VL 等多模态模型成为 Web Agent；支持在 Mind2Web-Live、Multimodal-Mind2Web、In-domain、MiniWoB++ 四个基准上评测，轨迹合成与部分评测依赖 OPENAI_API_KEY 与 Xvfb 虚拟显示环境。训练通过 torchrun 多卡启动，评测经 conda 环境加 pip 安装依赖完成。

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

- 探索驱动的网页操作轨迹合成流程
- 基于 torchrun 的 Qwen2-VL 多卡训练脚本
- 覆盖 Mind2Web-Live / Multimodal-Mind2Web / In-domain / MiniWoB++ 四套评测
- 提供 DeBERTa 候选生成分数文件的下载接入

## 适用场景

- 我要合成网页操作轨迹数据来训练 Web Agent 模型
- 我要在 Mind2Web 系基准上评测自己训练的多模态 Agent
- 我要复现论文的训练与评测流程

## 场景标签

`模型评测` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: This is the official codebase for **Explorer: Scaling Exploration-driven Web Trajectory Synthesis for Multimodal Web
> L12: ## 📦 Training
> L118: ## 🚀 Trajectory Synthesis

## 星数曲线

```mermaid
xychart-beta
    title "OSU-NLP-Group/Explorer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 27 --> 30
    line [29, 28, 28]
```

2026-10-18 29 → 2026-10-31 28（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7b836f224db7` · [字段定义](../../DATASET.md)*
