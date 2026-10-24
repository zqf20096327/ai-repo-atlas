# apple-aiml-research/ml-upscale

⭐ 74 · Jupyter Notebook · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/apple-aiml-research/ml-upscale) · [官网](https://upscale.aaalv.in) · 组织维护

**无约束通道剪枝的掩码与导出工具，面向 PyTorch 模型压缩**

Apple 研究团队发布的 ICML 2023 论文 UPSCALE 配套库：对训练后模型做通道掩码与剪枝，提供 Magnitude(L1/L2)、LAMP、FPGM、HRank 等剪枝启发式，可配置剪枝比例并导出无约束剪枝后的模型；论文报告平均提升 ImageNet 精度 2.1 点、推理速度最高 2 倍。以 pip 包提供，附带论文复现代码（支持 torchvision.models 命名空间内任意模型）与测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Magnitude/LAMP/FPGM/HRank 多种内置剪枝启发式，可自定义掩码方法
- PruningManager 导出无约束剪枝模型，可访问网络分段构建自定义剪枝算法
- 附带论文复现入口 python paper/main.py，支持 torchvision 任意模型

## 适用场景

- 我对训练后的 CNN 做通道剪枝压缩以提升推理速度
- 我复现 ICML 2023 UPSCALE 论文实验结果
- 我需要自定义剪枝启发式并导出剪枝后模型

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L5: **UPSCALE: Unconstrained Channel Pruning** @ ICML 2023
> L8: By removing constraints from existing pruners, we improve ImageNet accuracy for post-training pruned models by 2.1 p

## 星数曲线

```mermaid
xychart-beta
    title "apple-aiml-research/ml-upscale 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 73 --> 75
    line [74, 74]
```

2026-10-18 74 → 2026-10-24 74（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `be6b93aae14f` · [字段定义](../../DATASET.md)*
