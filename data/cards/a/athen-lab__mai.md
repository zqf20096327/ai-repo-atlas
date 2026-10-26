# athen-lab/mai

⭐ 34 · Python · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/athen-lab/mai) · 组织维护

**AI 生成图像鉴伪研究的数据集构建与管理工作台**

MAI 研究真实照片与全生成照片的表示几何，仓库本身作为数据集控制平面：提供构建、验证、发布数据集的 workbench 与测试代码，图像与发布元数据存放于 Hugging Face 数据集仓库。构建流程确定性采样固定数据源，用本地固定的 Moondream 为真实照片生成描述，生成合成对应图，由固定 CLIP QA 自动筛选，最终嵌入 Parquet 并保留完整血缘审计文件。需 ImageMagick 7，不配置付费生成 API；resnet/moondream 目录为历史检测实验，非当前协议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性数据集构建：固定采样、Moondream 描述、CLIP QA 筛选
- 嵌入分析与元数据到 Parquet 并保留完整血缘审计
- 支持初始化 spec、验证包、发布 release 与从固定 HF 修订下载分组
- 提供 Nix 固定开发环境与离线单元测试

## 适用场景

- 构建可复现的真实/合成配对照片数据集
- 发布带血缘审计的数据集到 Hugging Face
- 研究不同编码器、层、生成器家族下的嵌入几何

## 场景标签

 · 领域:机器学习/数据集与合成图像鉴伪研究

## 证据(README 行号)

> L8: This Git repository is the dataset **control plane**: it contains the workbench,
> L10: metadata are the **data plane** and belong in a Hugging Face dataset repository.

## 星数曲线

```mermaid
xychart-beta
    title "athen-lab/mai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-26 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6a37570bd386` · [字段定义](../../DATASET.md)*
