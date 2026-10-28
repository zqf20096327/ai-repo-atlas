# nadeemlab/DoseRTX

⭐ 52 · Python · 推送 2026-10-23 · [GitHub](https://github.com/nadeemlab/DoseRTX) · 组织维护

**面向放疗的 3D 剂量预测：基于矩损失函数的深度学习模型**

PMB'22 论文的官方代码：训练 UNet 式 3D CNN，输入 CT、PTV 与危及器官轮廓，输出体素级 3D 剂量分布，用于常规肺癌 IMRT 计划。核心机制是凸且可微的矩（Moments）损失函数，将 DVH 临床领域知识融入训练，可与 MAE、MAE+DVH 损失对比。数据为 MSKCC 360 例肺癌患者（训练 240/验证 50/测试 70），数据本身不随仓库发布，提供示例患者数据。安装经 pip requirements 与 pytorch3d，支持 Docker、GPU 与 Google CoLab 运行，并提供三种预训练模型下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 矩损失函数：凸、可微，将 DVH 领域知识融入任意深度学习框架且无额外计算开销
- UNet 式 3D CNN：CT+PTV+OAR 输入，输出 128³ 体素级剂量分布
- 提供 MAE、MAE+DVH、MAE+Moment 三种损失训练的预训练模型
- Docker 镜像（含示例数据与预训练模型）与 Google CoLab 环境

## 适用场景

- 放疗计划研究中预测肺部 IMRT 计划的 3D 剂量分布
- 复现论文中三种损失函数的对比实验
- 在自有 DICOM 数据上训练或测试剂量预测模型

## 场景标签

 · 领域:医疗 AI/放射治疗

## 证据(README 行号)

> L15: *We propose a novel moment-based loss function for predicting 3D dose distribution for the challenging conventional
> L24: architecure_image*We train a Unet like CNN architecture to output the voxel-wise 3D dose prediction corresponding t
> L18: We used 360 randomly selected lung cancer patients treated with conventional IMRT with 60Gy in 30 fractions at Memo

## 星数曲线

```mermaid
xychart-beta
    title "nadeemlab/DoseRTX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-28 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6eeb196897d4` · [字段定义](../../DATASET.md)*
