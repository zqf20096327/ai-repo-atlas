# XiaoxuYangLab/DeepMosaic

⭐ 58 · Python · NOASSERTION · 推送 2026-05-21 · [GitHub](https://github.com/XiaoxuYangLab/DeepMosaic) · [官网](https://www.nature.com/articles/s41587-022-01559-w) · 组织维护

**深度学习嵌合 SNV 分类工具：无需配对对照即可判读体细胞/生殖系嵌合变异**

面向人类遗传学与生物信息研究者的嵌合单核苷酸变异（SNV）可视化和分类工具。核心机制：将比对到变异位点的 reads 编码为 RGB 图像（红色通道碱基、绿色碱基质量、蓝色链方向），用深度卷积网络提取特征，并融合实验、基因组和群体频率信息做分类；在 10 个模型基准中选定 EfficientNet-b4 为默认模型。可视化模块可独立用于候选变异的人工检查。需要 Python 3.7、BEDTools、ANNOVAR、PyTorch 等环境，也提供 Docker 与 Singularity 镜像；图像表示在 500x 测序深度内无损，更深会随机降采样。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 BAM pileup 编码为 RGB 图像供 CNN 分类
- 无需配对对照信息即可分类嵌合 SNV
- 默认模型为基准测试中表现最好的 EfficientNet-b4
- 提供 Docker 与 Singularity 镜像运行方式

## 适用场景

- 对非癌症样本的候选嵌合 SNV 做计算分类
- 以图像形式可视化检查候选嵌合变异位点
- 研究嵌合突变时替代依赖配对对照的分析流程

## 场景标签

 · 领域:生物信息学/人类遗传学

## 证据(README 行号)

> L3: Visualization and control-independent classification tool of noncancer (somatic or germline) mosaic single nucleotid
> L15: * DeepMosaic Classification Module: Workflow from variant to result (10 models were compared and Efficientnet b4 wa
> L17: Workflow of DeepMosaic on best-performed deep convolutional neural network model after benchmarking. Variants were 

## 星数曲线

```mermaid
xychart-beta
    title "XiaoxuYangLab/DeepMosaic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-26 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c4c8a19642ee` · [字段定义](../../DATASET.md)*
