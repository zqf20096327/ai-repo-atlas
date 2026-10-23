# MouseLand/facemap

⭐ 203 · Python · GPL-3.0 · 推送 2026-01-26 · [GitHub](https://github.com/MouseLand/facemap) · [官网](https://facemap.readthedocs.io) · 组织维护

**从小鼠面部动作预测神经活动的框架，含姿态跟踪与视频 SVD**

神经科学研究工具：内置姿态估计模型跟踪小鼠面部关键点（多相机视角），深度神经网络编码模型基于姿态估计或 SVD 特征预测神经活动（或其主成分），并支持对行为视频做运动/静止 SVD 分解（保存前 500 主成分）、瞳孔与眨眼跟踪。以 Python 包提供，含 GUI（python -m facemap），预训练模型首次运行时自动下载；最新 tracker 与神经模型需从 git 源安装。输出仅在 macos-12 及更早版本测试，MATLAB 版 GUI 已停止支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 姿态估计模型跟踪小鼠面部多视角关键点，输出 *.h5 文件
- 深度神经网络编码模型从姿态/SVD 特征预测神经活动
- 单/多相机视频的 motSVD/movSVD 分解，保存前 500 主成分
- 提供 GUI、瞳孔/眨眼跟踪与多格式视频支持（mp4/avi/mj2 等）

## 适用场景

- 跟踪小鼠面部关键点并提取行为特征
- 从行为视频特征预测神经活动或其主成分
- 对行为视频做 SVD 分解提取时空成分

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L12: Facemap is a framework for predicting neural activity from mouse orofacial movements. It includes a pose estimation
> L150: Facemap includes a deep neural network encoding model for predicting neural activity or principal components of ne

## 星数曲线

```mermaid
xychart-beta
    title "MouseLand/facemap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 202 --> 204
    line [203, 203]
```

2026-10-18 203 → 2026-10-23 203（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d6f18c97fc50` · [字段定义](../../DATASET.md)*
