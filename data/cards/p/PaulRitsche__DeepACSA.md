# PaulRitsche/DeepACSA

⭐ 21 · Python · Apache-2.0 · 推送 2026-03-31 · [GitHub](https://github.com/PaulRitsche/DeepACSA) · [官网](https://deepacsa.readthedocs.io/en/latest/) · 组织维护

**深度学习自动测量超声图像肌肉横截面积的开源工具**

面向肌肉超声图像分析的科研工具：使用深度学习（UNet-VGG16、UNet 3+ 等架构）自动分割并测量肌肉解剖横截面积（ACSA），覆盖股直肌、股二头肌、髌腱、股内侧肌等多个部位，模型在健康人及 ACL 损伤者数据上训练。提供 GUI 界面，支持 pip 安装（v0.3.1）、可执行文件或源码运行；v0.3.2 仅可克隆仓库并以 conda 环境安装。训练模型与数据通过 DOI 提供，需引用对应论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 深度学习自动分割肌肉超声图像并测量 ACSA
- 覆盖髌腱、股内侧肌、腘绳肌等多个部位模型
- 提供 GUI，支持 pip、可执行文件与源码三种运行方式
- 训练模型、数据与示例文件经 DOI 公开

## 适用场景

- 科研中批量测量肌肉横截面积替代手动分割
- 运动医学与康复研究中的肌肉形态量化
- 对比不同模型架构在超声分割上的表现

## 场景标签

`科研工具` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L8: DeepACSA is an open-source tool to evaluate the anatomical cross-sectional area of muscles in ultrasound images usin
> L66: We provide a model for the automatic segmentation of the patellar tendon anatomical cross-sectional area (ACSA) at 
> L90: DeepACSA workflow. a) Original ultrasound image of the m. rectus femoris (RF) at 50% of femur length that serves as

## 星数曲线

```mermaid
xychart-beta
    title "PaulRitsche/DeepACSA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ff562f420c4f` · [字段定义](../../DATASET.md)*
