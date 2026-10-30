# Jianningli/autoimplant

⭐ 28 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/Jianningli/autoimplant) · [官网](https://autoimplant.grand-challenge.org/) · 个人维护

**自动颅骨植入体设计的深度学习基线方法（MICCAI 2020 挑战赛）**

MICCAI 2020 AutoImplant 颅内植入体设计挑战赛的基线方法代码库：提供 n1 模型，支持直接植入体预测与降采样模式下的颅骨形状补全两种方式，并比较两者在泛化性与后处理需求上的差异；预测结果可用 Dice 相似性分数与 Hausdorff 距离做定量评估。训练/测试数据来自挑战赛网站（100 对训练、100 对测试、10 个鲁棒性测试）。运行环境为 Python 3.6.8 + TensorFlow 1.4.0，无 GPU 时需设置 CUDA_VISIBLE_DEVICES=-1，附带输出还原与去噪后处理脚本。

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

- n1 模型同时支持直接植入体预测与颅骨形状补全
- 提供 Dice 相似性分数与 Hausdorff 距离的定量形状评估
- 附带 pred_2_org.py 维度还原与 pre_post_processing.py 自动去噪脚本

## 适用场景

- 复现或改进 AutoImplant 挑战赛的颅骨植入体设计基线
- 研究生成式形状补全在颅骨重建中的应用
- 对比直接预测与形状补全两种问题建模方式

## 场景标签

 · 领域:医学影像/计算医学

## 证据(README 行号)

> L11: This GitHub repository contains codes for the automatic cranial implant design methods described in:
> L16: The `n1` model is trained for both direct implant prediction and skull shape completion (in a down-sampled mode). T

## 星数曲线

```mermaid
xychart-beta
    title "Jianningli/autoimplant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `93c060c1e8bd` · [字段定义](../../DATASET.md)*
