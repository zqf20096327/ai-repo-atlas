# LambertLeong/Pseudo-DXA

⭐ 19 · Python · GPL-3.0 · 推送 2026-07-10 · [GitHub](https://github.com/LambertLeong/Pseudo-DXA) · 组织维护

**生成式模型：从 3D 体表扫描生成 DXA 影像与体成分**

深度学习生成模型，读取 3D 体表扫描网格（需先用 Meshcapade API 拟合为 T-pose、110K 点，默认采样 22,061 点），生成定性 DXA 扫描预览图与 6 通道原始预测，用于研究脂肪、瘦体与骨量等体成分评估流程。面向 Linux + CUDA GPU 运行，CPU 可执行但更慢。通过 pip -e 安装，提供 python 脚本与 CLI 两种运行方式；模型权重与测试网格需向实验室索取，NPY 转 DXA 专有格式的代码不公开。

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

- 3D 体表网格输入生成 DXA 定性与定量结果
- 输出 6 通道预测 NPY 与单通道处理预览图
- 支持 GPU 与 CPU（-1 强制 CPU）执行

## 适用场景

- 研究者用 3D 体扫描替代 DXA 设备获取体成分估计
- 体型外观推断体内脂肪/瘦体/骨分布的研究流程

## 场景标签

`图像生成` `科研工具` · 领域:内容生成

## 证据(README 行号)

> L3: Pseudo-DXA is a generative deep learning model that produces qualitative and quantitative dual-energy X-ray absorpti
> L5: This model was developed by Lambert T Leong,PhD advised by John A Shepherd as a part of the Shepherd Research Lab (S

## 星数曲线

```mermaid
xychart-beta
    title "LambertLeong/Pseudo-DXA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b3247e7c7c01` · [字段定义](../../DATASET.md)*
