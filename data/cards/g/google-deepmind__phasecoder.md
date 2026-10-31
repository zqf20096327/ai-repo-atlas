# google-deepmind/phasecoder

⭐ 25 · Python · Apache-2.0 · 推送 2026-08-05 · [GitHub](https://github.com/google-deepmind/phasecoder) · 组织维护

**麦克风阵列几何无关的空间音频定位编码器（多模态 LLM 用）**

Google DeepMind 发布的 transformer 空间音频编码器：输入原始多通道音频与麦克风坐标，输出空间嵌入以及声源的方位角、仰角与距离估计，对麦克风阵列几何形状不敏感。仓库提供预训练权重（checkpoints/v1，免单独下载）与 JAX/NNX 的检查点加载与推理工具函数，附 Colab 定位演示笔记本。本地运行需 Python 3.10+，通过 git clone 源码加 pip 安装依赖。

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

- 输入多通道音频与麦克风坐标，输出定位方位角/仰角/距离与空间嵌入
- 对麦克风阵列几何无关（geometry-agnostic）
- 预训练权重内置于仓库，checkpoint_utils.load_model() 自动加载
- 提供 JAX/NNX 推理工具函数与浏览器 Colab 演示

## 适用场景

- 为多模态 LLM 接入空间音频理解能力
- 在任意麦克风阵列布局上做声源定位
- 在浏览器中通过 Colab 试用定位功能

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L9: PhaseCoder is a transformer-only spatial audio encoder that is **agnostic** to
> L11: coordinates as inputs to perform localization and produces robust spatial
> L14: This repository releases the model weight checkpoints and hosts JAX / NNX

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/phasecoder 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28", "2026-10-31"]
    y-axis "stars" 21 --> 26
    line [22, 23, 24, 25]
```

2026-10-18 22 → 2026-10-31 25（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e10f0bcedb9d` · [字段定义](../../DATASET.md)*
