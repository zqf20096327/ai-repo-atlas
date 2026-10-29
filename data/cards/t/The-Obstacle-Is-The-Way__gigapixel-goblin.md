# The-Obstacle-Is-The-Way/gigapixel-goblin

⭐ 17 · Python · Apache-2.0 · 推送 2026-04-01 · [GitHub](https://github.com/The-Obstacle-Is-The-Way/gigapixel-goblin) · [官网](https://the-obstacle-is-the-way.github.io/gigapixel-goblin/) · 组织维护

**千兆像素病理图像的 LLM 导航环境与 MultiPathQA 评测框架**

GIANT 风格的全切片病理图像（WSI）导航环境加评测运行器：LLM agent 以缩略图为起点，迭代平移、缩放并推理（最多 20 步）直至回答诊断问题，系统记录轨迹并计算准确率。评测集 MultiPathQA 含 934 题、862 张全切片图像，覆盖 GTEx 器官分类、ExpertVQA、SlideBench、TCGA、PANDA 五个基准。支持接入 OpenAI 与 Anthropic 模型（Gemini 列为计划中），数据集需另行下载约 500 GiB。面向病理计算领域的研究者与开发者复现论文结果、评测 VLM 在千兆像素医学图像上的能力。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM agent 迭代平移/缩放导航千兆像素 WSI，最多 20 步
- MultiPathQA 评测：934 题、862 张全切片、5 个基准
- 支持记录轨迹、断点续跑、成本追踪与轨迹可视化
- 可接入 OpenAI（默认）与 Anthropic 模型

## 适用场景

- 复现论文并评测 VLM 在千兆像素病理图像上的导航推理能力
- 在 MultiPathQA 基准上运行不同模型的诊断问答实验
- 分析 agent 在多个缩放级别下的证据累积轨迹

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L11: **The Solution**: GIANT lets LLMs navigate gigapixel images like pathologists do—iteratively pan, zoom, and reason 
> L39: Evaluated on MultiPathQA—934 questions across 862 unique whole-slide images.
> L83: **For Researchers**: A reproducible benchmark (MultiPathQA) and framework for evaluating LLM capabilities on gigapi

## 星数曲线

```mermaid
xychart-beta
    title "The-Obstacle-Is-The-Way/gigapixel-goblin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `295eb1df5b94` · [字段定义](../../DATASET.md)*
