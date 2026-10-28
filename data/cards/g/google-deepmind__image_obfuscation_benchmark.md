# google-deepmind/image_obfuscation_benchmark

⭐ 27 · Python · Apache-2.0 · 推送 2026-05-20 · [GitHub](https://github.com/google-deepmind/image_obfuscation_benchmark) · 组织维护

**对抗性图像混淆的模型鲁棒性评测基准与数据集**

DeepMind 发布的图像混淆基准配套代码与数据集：对 ILSVRC2012 每张图像应用 22 种混淆变换（19 训练用、3 留出），提供验证与训练集 tar 包下载，可通过 TensorFlow Datasets API 加载。评测流程为：对指定混淆分割运行预测脚本（模型经 TF-Hub 路径加载），再汇总计算指标输出 metrics.csv。不提供训练代码；出于伦理考虑未发布生成混淆的代码，仅提供预计算数据集与评测代码。

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

- 22 种图像混淆变换应用于 ILSVRC2012 全量图像
- 数据集经 TensorFlow Datasets API 加载，按混淆类型分 split
- 预测→汇总两步评测流程，输出 CSV 预测与指标
- 训练集总规模达每混淆 9.5–55 GB tar 包

## 适用场景

- 评测图像分类模型对对抗性混淆的鲁棒性
- 以混淆数据集训练更稳健的分类模型（需自行搭建训练管线）
- 复现论文 Benchmarking Robustness to Adversarial Image Obfuscations 的结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the code to evaluate models on the image obfuscation benchmark, first presented in
> L115: python3 -m image_obfuscation_benchmark.eval.predict \
> L127: python3 -m image_obfuscation_benchmark.eval.gather_results \

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/image_obfuscation_benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2b47010e3633` · [字段定义](../../DATASET.md)*
