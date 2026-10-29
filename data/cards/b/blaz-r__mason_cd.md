# blaz-r/mason_cd

⭐ 23 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/blaz-r/mason_cd) · 组织维护

**无需标注变化掩膜的无监督遥感变化检测方法（IEEE TGRS 2026）**

卢布尔雅那大学团队发表的遥感变化检测研究代码：MaSoN 在冻结的 DINOv3 ViT-L/16 基础模型潜空间中，用按目标域特征统计校准的高斯扰动合成相关变化与无关变异，以合成掩膜监督训练解码器，推理时直接比对真实图像对特征，从而免除人工标注。提供训练/评测代码、五个基准（OSCD/LEVIR/SYSU/CLCD/GVLM）预训练检查点与浏览器 demo。限制：依赖 backbone 访问授权，性能受编码器表征影响，新域或新模态可能需适配。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 冻结 DINOv3 编码器潜空间中的数据自适应扰动合成训练信号，无需标注变化掩膜
- 提供 oscd96/levir/sysu/clcd/gvlm 五个基准的预训练检查点
- 支持 Hugging Face 自动下载与本地目录/HDF5 数据集训练评测
- 提供 Hugging Face Spaces 浏览器 demo

## 适用场景

- 在没有人工标注变化掩膜的数据上训练遥感变化检测器
- 在 OSCD/LEVIR 等标准基准上复现论文评测结果
- 对单对图像快速试用变化检测效果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L19: Train a remote sensing change detector without annotated change masks. MaSoN synthesises relevant changes and irrel
> L167: 1. Extract features with a frozen encoder.
> L169: 3. Train a decoder to detect changes from feature differences. At inference, compare the features of the actual im

## 星数曲线

```mermaid
xychart-beta
    title "blaz-r/mason_cd 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-29 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `376d5aaf0806` · [字段定义](../../DATASET.md)*
