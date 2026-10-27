# Pulkit-Khandelwal/purple-mri

⭐ 26 · Python · 推送 2026-10-22 · [GitHub](https://github.com/Pulkit-Khandelwal/purple-mri) · [官网](https://purple-mri.readthedocs.io) · 组织维护

**离体人脑 MRI 分割、皮层重建与解剖分区的科研工具链**

面向神经影像研究者的高分辨率离体（postmortem）人脑 MRI 处理框架，提供深度学习分割、拓扑校正、皮层表面重建、图谱分区与形态测量，以及配准、模板构建和组分析等研究工作流。运行途径包括 ITK-SNAP 远程 DSS 服务、Python CLI 启动 Docker、直接 Docker 与 Singularity SIF；镜像内含训练模型、FreeSurfer、Convert3D 与图谱资源，表面处理需提供 FreeSurfer 许可证。深度学习阶段需 NVIDIA GPU，表面阶段可 CPU 运行。由宾夕法尼亚大学 PATCH/PICSL 实验室出身的研究者维护，附带多条相关论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度学习分割（含 Task2732 皮下核团模型）、拓扑校正、皮层重建与图谱分区一体化的容器化流水线
- 四种运行途径：ITK-SNAP 远程 DSS、Python CLI+Docker、直接 Docker、Singularity SIF
- Docker 镜像内置训练模型、FreeSurfer、Convert3D、atlas 资源与自定义 pial 可执行文件
- 覆盖离体-在体配准、人群模板、组分析、婴儿脑重建等扩展研究工作流

## 适用场景

- 对离体人脑 MRI 批量做分割与皮层表面重建
- 阿尔茨海默病等神经退行性研究的皮层分区与形态测量
- 构建研究用模板并做 ROI/顶点级组分析

## 场景标签

`科研工具` `图像视频处理` · 领域:学习与行业

## 证据(README 行号)

> L5: `purple-mri` provides segmentation, cortical surface reconstruction, anatomical
> L6: parcellation, registration, and morphometric analysis of high-resolution

## 星数曲线

```mermaid
xychart-beta
    title "Pulkit-Khandelwal/purple-mri 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e01fdf133268` · [字段定义](../../DATASET.md)*
