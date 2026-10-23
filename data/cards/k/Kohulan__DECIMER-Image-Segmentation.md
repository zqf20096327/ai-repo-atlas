# Kohulan/DECIMER-Image-Segmentation

⭐ 156 · Jupyter Notebook · MIT · 推送 2026-02-25 · [GitHub](https://github.com/Kohulan/DECIMER-Image-Segmentation) · [官网](https://decimer.ai) · 组织维护

**从科学文献中检测并切分化学结构图的深度学习工具**

基于 Mask R-CNN 的开源实例分割工具，自动检测科学出版物（含现代 PDF 与扫描历史文献）中的化学结构图并切分为独立结构图像。工作流分两阶段：模型生成结构掩码，后处理算法扩展掩码以捕获完整结构。提供 Python API、命令行脚本与 Jupyter 教程，支持 CPU 与 CUDA GPU 两种模式，Windows 下处理 PDF 需额外安装 Poppler。由耶拿大学 Steinbeck 化学信息学组维护，是 DECIMER 化学结构识别流水线的分段组件，另有 decimer.ai 在线应用。预训练模型通过 DOI 公开发布，配套论文发表于 J Cheminform（2021）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Mask R-CNN 实例分割检测化学结构图
- 支持现代 PDF 与扫描历史文献
- 掩码扩展后处理捕获完整结构
- 提供 Python API、CLI 与预训练模型

## 适用场景

- 批量从期刊 PDF 中提取化学结构图用于 OCSR 流程
- 数字化扫描的历史化学文献中的结构图
- 作为 DECIMER 结构识别流水线的第一步

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L27: > Chemistry has accumulated vast amounts of knowledge about chemical compounds, structures, and properties across c
> L36: - 🔍 **Detect** chemical structure depictions in scientific publications
> L44:  Built on Mask R-CNN architecture for state-of-the-art detection accuracy

## 星数曲线

```mermaid
xychart-beta
    title "Kohulan/DECIMER-Image-Segmentation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 155 --> 157
    line [156, 156]
```

2026-10-18 156 → 2026-10-23 156（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6a140cae9f17` · [字段定义](../../DATASET.md)*
