# rsanchezgarc/deepEMhancer

⭐ 62 · Python · Apache-2.0 · 推送 2026-09-25 · [GitHub](https://github.com/rsanchezgarc/deepEMhancer) · 个人维护

**cryo-EM 密度图深度学习后处理包：锐化与去噪**

Python 命令行工具，对冷冻电镜密度图做非线性后处理，主要产生局部锐化与自动掩膜去噪效果。模型在实验体积与原子模型校正体积的配对数据上训练，首选输入为未处理的半图（half-maps），也可接受 RELION 或 cryoSPARC 输出的完整图。提供 tightTarget/wideTarget/highRes 三种模型选择，支持多 GPU 与 CPU 推理，默认经 pip 从 GitHub 安装并下载预训练模型。训练集未含翻译后修饰与配体，相关区域结果可能不准确；已在 Linux（含 WSL2）上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 cryo-EM 图做局部锐化与自动掩膜去噪
- 三种预训练模型（tightTarget/wideTarget/highRes）可选
- 支持多 GPU 与 CPU-only 推理，batch_size 可调
- 可通过 SBGrid 安装使用

## 适用场景

- cryo-EM 图后处理以提升密度图可解释性
- 对优于 4 Å 分辨率图尝试 highRes 模型增强
- 对异质或低分辨率图选择合适模型处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L2: **DeepEMhancer** is a Python package for post-processing cryo-EM maps, as described in
> L10: DeepEMhancer performs nonlinear post-processing with two main effects:
> L6: DeepEMhancer was trained on pairs of experimental volumes and atomic model-corrected volumes. Its preferred inputs a

## 星数曲线

```mermaid
xychart-beta
    title "rsanchezgarc/deepEMhancer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-28 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `46b38baa5011` · [字段定义](../../DATASET.md)*
