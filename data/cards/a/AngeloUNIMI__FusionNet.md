# AngeloUNIMI/FusionNet

⭐ 18 · MATLAB · GPL-3.0 · 推送 2026-05-31 · [GitHub](https://github.com/AngeloUNIMI/FusionNet) · [官网](http://iebil.di.unimi.it/fusionnet/index.htm) · 组织维护

**非接触掌纹与指内侧纹理识别的深度特征融合代码（MATLAB）**

IEEE CIVEMSA 2019 论文的 MATLAB 源码：从单次非接触手掌图像中提取掌纹与指内侧纹理（IFT）的 ROI，用 PCANet 架构的深度流水线对各生物特征提取特征并在特征级融合，最后输出生物识别性能评估。实验基于 REST 手部数据库，用户需自行下载数据集，克隆仓库后在 MATLAB 中运行 main_FusionNet 脚本。另在独立仓库提供基于摄像头的演示版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单次非接触手掌采集同时获取掌纹与指内侧纹理
- PCANet 架构深度特征提取
- 掌纹与 IFT 的特征级融合
- 在 REST 手部数据库上进行生物识别评估

## 适用场景

- 复现论文中的非接触掌纹/指纹理融合识别实验
- 研究非接触、弱约束场景下的生物识别方法
- 在其基础上开发或改进掌纹识别流水线

## 场景标签

 · 领域:生物识别/计算机视觉

## 证据(README 行号)

> L16: **FusionNet** is a MATLAB implementation of a touchless biometric recognition pipeline that combines two complement
> L28: - 🧬 Deep feature extraction with a PCANet-inspired architecture

## 星数曲线

```mermaid
xychart-beta
    title "AngeloUNIMI/FusionNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `42c5edda6d55` · [字段定义](../../DATASET.md)*
