# NKI-AI/direct

⭐ 320 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/NKI-AI/direct) · [官网](https://docs.aiforoncology.nl/direct)

**面向加速 MRI 重建的 PyTorch 深度学习工具包**

DIRECT 是 NKI-AI（荷兰癌症研究所）维护的 PyTorch 工具包，处理加速磁共振成像重建全流程：读取欠采样多线圈 k-space 数据，提供采样掩码库（Cartesian/radial/spiral/Poisson 等）、十余种重建模型（vSHARP、RecurrentVarNet、RIM、VarNet、U-Net 等）、全监督/自监督 SSDU/JSSL 训练范式、分布式多 GPU 训练与 MRI 指标评估，经 direct train/predict 命令运行。预训练权重托管在 Hugging Face。声明不用于临床，Apache 2.0 许可。

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

- 端到端流水线：采样、重建、可选配准、指标与预训练基线
- 内置 vSHARP、RecurrentVarNet、RIM 等挑战赛获胜模型
- 全监督 / SSDU / JSSL 训练范式，支持分布式多 GPU 与混合精度
- Hugging Face 模型库提供 .yaml/.pt 预训练权重，direct predict 直接推理

## 适用场景

- 科研人员训练与评测 MRI 重建深度学习模型
- 用预训练模型对欠采样 k-space 数据做重建推理
- 复现 fastMRI、CMRxRecon 等挑战赛实验配置

## 场景标签

`科研工具` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L21: ``DIRECT`` is a PyTorch toolkit for accelerated MRI reconstruction.
> L43: * **Reconstruction models.** vSHARP, RecurrentVarNet, VarNet, RIM / CIRIM,

## 星数曲线

```mermaid
xychart-beta
    title "NKI-AI/direct 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 319 --> 321
    line [320, 320]
```

2026-10-18 320 → 2026-10-28 320（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `584953dad9d3` · [字段定义](../../DATASET.md)*
