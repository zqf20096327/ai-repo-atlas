# david-xinyuwei/david-share

⭐ 450 · Jupyter Notebook · MIT · 推送 2026-11-24 · [GitHub](https://github.com/david-xinyuwei/david-share) · 个人维护 · 中文 README

**面向工程师的 Azure AI Agents 与深度学习实操项目与基准合集**

微软 AI 系统工程师 Xinyu Wei 的个人实践仓库，按 AI Agents、深度学习、算法解析、多模态四个领域组织自包含项目：在 Microsoft Foundry 与 Azure 上构建、托管与运营 agent，涵盖微调与强化学习、推理优化（vLLM、投机解码、KV cache）、FP8/FP4 量化、NVIDIA/AMD GPU 选型基准，每项目含 README、脚本、原始结果与 CI 检查。仓库整体超过 3 GB，提供 sparse-checkout 按需克隆单个项目，大文件经 Git LFS 存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按领域组织的自包含项目，每个文件夹含独立 README
- 多数项目附带产出数据的脚本、原始结果与 CI 检查
- vLLM/SGLang/量化/GPU 基准（H100、H200、MI300X）实测内容
- 提供 git sparse-checkout 命令按需下载单个项目文件夹

## 适用场景

- 在 Microsoft Foundry 与 Azure 上部署和运营 agent 时找参考实现
- 在 NVIDIA/AMD GPU 上做推理优化与精度量化实验前查基准数据
- 学习大模型微调、分布式训练与多模态评测的实操流程

## 场景标签

`模型评测` `微调` `模型量化` `推理引擎` · 领域:评测与运维

## 证据(README 行号)

> L11: This repository collects the hands-on work of **Xinyu Wei (魏新宇)**, Microsoft AI Lead Senior System Engineer, in two
> L14: - **Deep learning**: fine-tuning and reinforcement learning, inference optimization, precision and quantization, GP
> L40: |🔬 DL Algorithm Insights|One algorithm or systems topic per folder, explained in depth with experiments|

## 星数曲线

```mermaid
xychart-beta
    title "david-xinyuwei/david-share 星数(近 6 点)"
    x-axis ["2026-11-14", "2026-11-15", "2026-11-19", "2026-11-21", "2026-11-23", "2026-11-26"]
    y-axis "stars" 448 --> 452
    line [450, 451, 450, 449, 450, 450]
```

2026-11-14 450 → 2026-11-26 450（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `561ca4433aae` · [字段定义](../../DATASET.md)*
