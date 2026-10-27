# silviutroscot/CodeSLAM

⭐ 209 · Python · 推送 2026-03-26 · [GitHub](https://github.com/silviutroscot/CodeSLAM) · 个人维护

**CodeSLAM 论文 PyTorch 实现：紧凑深度表示的单目稠密 SLAM**

复现 CVPR 2018 论文 CodeSLAM 的完整算法管线：图像条件化的深度 VAE 将稠密深度压缩为 128 维可优化隐码，解码器对隐码保持线性以支持 Jacobian 预计算；在此基础上实现两帧联合位姿/隐码优化、由粗到精跟踪、Schur 补边缘化的滑窗单目 SLAM。提供训练、深度评估、单图推理与序列 SLAM 的命令行入口，数据加载面向 SceneNet 风格 RGB-D 目录。README 声明论文数值复现与实时性尚需训练权重与实测验证。面向计算机视觉/机器人方向的研究者与复现者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 条件化深度 VAE：128 维隐码 + 混合 proximity 参数化 + 学习的不确定性
- 对隐码线性的解码器路径与 Jacobian 预计算
- 稠密光度/几何残差的 Levenberg-Marquardt 联合位姿-隐码优化
- 滑窗单目 SLAM：Schur 补边缘化为线性先验

## 适用场景

- 复现论文的两帧初始化与单目 SLAM 流程
- 在 SceneNet 风格 RGB-D 数据上训练条件化深度模型
- 对单张图像输出稠密深度先验与不确定性图

## 场景标签

 · 领域:计算机视觉/SLAM

## 证据(README 行号)

> L3: PyTorch implementation of CodeSLAM: Learning a Compact, Optimisable Representation for Dense Visual SLAM.
> L7: - A conditioned depth autoencoder with a compact latent code
> L56: - `scripts/run_slam.py`

## 星数曲线

```mermaid
xychart-beta
    title "silviutroscot/CodeSLAM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 208 --> 210
    line [209, 209]
```

2026-10-18 209 → 2026-10-27 209（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4353299ed940` · [字段定义](../../DATASET.md)*
