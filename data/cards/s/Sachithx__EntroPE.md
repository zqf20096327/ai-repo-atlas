# Sachithx/EntroPE

⭐ 50 · Python · 推送 2026-10-22 · [GitHub](https://github.com/Sachithx/EntroPE) · [官网](https://arxiv.org/pdf/2509.26157) · 个人维护

**NeurIPS 2026 论文官方实现：熵引导的时序 patch 分割预测**

EntroPE 论文（NeurIPS 2026）的参考实现：用冻结的预训练因果 GPT 熵模型在高熵位置放置 patch 边界，再以 patch 编码器/全局 transformer/融合解码器骨干做长期时序预测。仓库复现 ETTh1/ETTh2/ETTm1/ETTm2/Weather/ECL/Traffic/Solar 八个基准（L=96，horizon 96-720）的结果：可评估自带的 checkpoint（含每格一模型），也可从零训练。熵模型 checkpoint 随仓库分发，数据集与预测 checkpoint 需从 HuggingFace Hub 下载。单 GPU（CUDA 12.x）即可运行。注意：当前 arXiv 版本评估协议与仓库实现不同。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 冻结 GPT 熵模型在高熵位置放置 patch 边界
- 复现 8 个基准数据集、4 个 horizon 的长期预测结果
- 支持评估自带 checkpoint 或从零训练（每格最优配置写入脚本）
- 熵模型 checkpoint 随仓库分发，无需额外下载

## 适用场景

- 复现论文的长期时序预测结果
- 在标准基准上从零训练 EntroPE 模型
- 基于熵引导 patch 分割开展时序预测研究

## 场景标签

 · 领域:时间序列机器学习研究

## 证据(README 行号)

> L6: Reference implementation for the NeurIPS 2026 paper. EntroPE places patch
> L7: boundaries at high-entropy positions using a frozen, pre-trained causal GPT
> L8: entropy model, then forecasts with a patch encoder / global transformer /

## 星数曲线

```mermaid
xychart-beta
    title "Sachithx/EntroPE 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-28 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `dfd57ac582b7` · [字段定义](../../DATASET.md)*
