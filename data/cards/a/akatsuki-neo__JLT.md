# akatsuki-neo/JLT

⭐ 52 · Python · MIT · 推送 2026-09-28 · [GitHub](https://github.com/akatsuki-neo/JLT) · [官网](https://akatsuki-neo.github.io/JLT) · 个人维护

**潜在扩散 Transformer 训练框架：以干净潜变量预测替代速度预测**

论文配套代码库 JLT：一类潜在 Transformer（B/L/H 三档，130.5M–951.3M 参数），网络预测干净的 VAE 端点并通过固定仿射读出转换为速度供 ODE 求解器使用。在 ImageNet 256×256 类条件生成、冻结 FLUX.2 VAE 的设定下，与直接速度预测做匹配对比，报告 FID-50K 从 6.56 降至 2.84（Base）。提供数据预处理（VAE 预编码）、训练脚本与 FID 评测流程，checkpoint 托管在 HuggingFace。面向扩散模型研究人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 干净潜变量预测 + 固定仿射读出转速度的架构
- B/L/H 三档规模（130.5M–951.3M 参数）
- 提供 ImageNet 预编码、训练脚本与 FID-50K 评测流程
- 与 DiT/SiT/REPA 等参考模型的 FID/IS 对比表

## 适用场景

- 复现论文中的干净预测 vs 速度预测对比实验
- 在 ImageNet 256×256 上训练类条件潜在扩散 Transformer
- 基于 checkpoint 做 FID-50K 评测

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: JLT is a latent Transformer that predicts the clean VAE endpoint and converts it to velocity with a fixed affine rea
> L45: The checked-in launcher trains JLT-B/1 (clean latent, patch 1 on the 16×16 FLUX grid):

## 星数曲线

```mermaid
xychart-beta
    title "akatsuki-neo/JLT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `32c39fceb243` · [字段定义](../../DATASET.md)*
