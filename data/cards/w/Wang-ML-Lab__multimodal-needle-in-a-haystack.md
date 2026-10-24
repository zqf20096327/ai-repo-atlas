# Wang-ML-Lab/multimodal-needle-in-a-haystack

⭐ 57 · Python · MIT · 推送 2026-04-22 · [GitHub](https://github.com/Wang-ML-Lab/multimodal-needle-in-a-haystack) · [官网](https://mmneedle.github.io/) · 组织维护

**多模态大海捞针基准：评测多模态 LLM 的长上下文能力**

NAACL 2025 Oral 论文的代码与数据仓库：在由多张拼接子图组成的长视觉上下文中埋入目标子图，要求多模态大模型根据文本描述定位目标子图的索引、行、列位置，以此评测长上下文能力。数据集经 Hugging Face 与 Google Drive 提供，支持从 MS COCO 自行构建数据，并通过环境变量配置模型提供方、序列数与针数后运行测试脚本收集准确率。评测结果涵盖 GPT-4o、Gemini、Claude 等 API 模型与开源模型。

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

- 在拼接子图的长视觉上下文中定位目标子图的定位式评测任务
- 数据集托管于 Hugging Face，支持 datasets.load_dataset 直接加载
- 提供从 MS COCO 采样图像、针与拼接图的完整构建脚本
- 支持配置模型提供方、序列数与针数的测试与评测脚本

## 适用场景

- 评测多模态大模型在长视觉上下文中的检索定位能力
- 对比不同 MLLM 在不同图像数与拼接尺寸设置下的准确率
- 基于 MS COCO 构建自定义版本的大海捞针数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: **Multimodal Needle in a Haystack: Benchmarking Long-Context Capability of Multimodal LLMs**
> L74: ## Step 3: Testing a Specific Model in Different Settings

## 星数曲线

```mermaid
xychart-beta
    title "Wang-ML-Lab/multimodal-needle-in-a-haystack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-24 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2dff2bd79ab5` · [字段定义](../../DATASET.md)*
