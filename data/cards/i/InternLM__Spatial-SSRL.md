# InternLM/Spatial-SSRL

⭐ 141 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/InternLM/Spatial-SSRL) · [官网](https://arxiv.org/abs/2510.27606) · 组织维护 · 中文 README

**自监督强化学习框架，提升大型视觉语言模型的空间理解能力**

CVPR 2026 论文的官方代码发布：提出 Spatial-SSRL 训练范式，用普通 RGB / RGB-D 图像构造无需人工标注的五个前置任务，以 RLVR 方式训练 Qwen2.5-VL、Qwen3-VL 等模型，提升图像与视频场景下的空间理解表现。发布 7B / 3B / 4B 三个模型权重与 81k 数据集，提供推理代码片段、训练与评测流程（基于 EasyR1 / LLaMA-Factory 构建，评测依赖 VLMEvalKit）。数据与代码仅限研究用途许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自监督 RL 训练范式，五个前置任务仅需 RGB / RGB-D 图像，无需人工标注与外部工具
- 在七个图像与视频空间理解基准上进行评测
- 提供 7B / 3B / 4B 三个模型权重与 Spatial-SSRL-81k 数据集
- 提供训练与评测代码及 Hugging Face Space 在线试用

## 适用场景

- 研究者在 LVLM 上复现自监督强化学习空间理解训练
- 下载已训练模型做图像/视频空间理解推理
- 扩展新的自监督前置任务参与贡献

## 场景标签

`强化学习` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L41: We are thrilled to introduce Spatial-SSRL , a novel self-supervised RL paradigm aimed at enhancing LVLM spatial und
> L46: Spatial-SSRL is a lightweight tool-free framework that is natually compatible with the RLVR training paradigm and e
> L115: **Usage and License Notices**: The data and code are intended and licensed for research use only.

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/Spatial-SSRL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 140 --> 142
    line [141, 141]
```

2026-10-18 141 → 2026-10-23 141（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `bd7d232d8e83` · [字段定义](../../DATASET.md)*
