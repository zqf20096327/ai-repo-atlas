# BioMedIA-MBZUAI/EchoAlign

⭐ 10 · Python · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/BioMedIA-MBZUAI/EchoAlign) · [官网](https://biomedia-mbzuai.github.io/EchoAlign/) · 组织维护

**超声心动图视觉-语言基础模型：检测、分级、测量与分割**

基于 159 个临床中心 287 万段超声心动图视频与图像训练的视觉-语言基础模型，在视频、心脏结构、检查三个层级与报告文本对齐，并用可见性矩阵限制监督到实际显示该结构的视图。单个模型覆盖 62 项临床发现的检测、严重程度分级、测量估计与心腔结构分割。仓库提供 240.7M 参数的权重文件（Hugging Face 下载）、冻结编码器下的 zero-shot/线性探针/分割三种评估流程，以及与五个已发表模型的基准对比代码。依赖 Conda、Python 3.10、PyTorch 2.6.0 与 ffmpeg；许可为 CC BY-NC 4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视频/结构/检查三层级报告对齐，可见性矩阵限制监督范围
- 单模型支持 62 项发现的检测、分级、测量与心腔分割
- 提供 zero-shot、线性探针、分割三种冻结编码器评估流程
- 权重文件与基准模型 Git 子模块一并开放

## 适用场景

- 对超声心动图视频做临床发现的 zero-shot 打分
- 在公开数据集上复现论文中的分类与分级指标
- 用自己的数据拟合 832 维表示上的线性探针
- 在 CAMUS、EchoNet 等数据集上评估心腔分割

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L11: Echocardiography assesses the structure and function of the heart. Cardiologists read each study across several sta
> L88: - **Zero-shot:** each model scores each finding with its own method, with no training on the evaluation labels.
> L93: - **Segmentation:** a linear head and a small decoder are trained on the feature map of EchoAlign, EchoPrime, PanEc


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `9020243327c0` · [字段定义](../../DATASET.md)*
