# NRAD-UKAachen/InterACT

⭐ 4 · Python · NOASSERTION · 推送 2026-11-16 · [GitHub](https://github.com/NRAD-UKAachen/InterACT) · [官网](https://www.ukaachen.de/en/kliniken-institute/klinik-fuer-diagnostische-und-interventionelle-neuroradiologie/forschung/ki-dateninfrastruktur/interact/) · 组织维护

**神经放射影像研究平台：DICOM 归档+Web 查看+分割处理管线**

由 RWTH Aachen 大学医院神经放射诊断与介入科开发的研究影像平台，整合 dcm4chee-arc（PACS）、OHIF（查看器）、Keycloak（单点登录）、iRODS（数据管理）与 Airflow（编排）等开源组件。基础模块提供 DICOM 归档、Web 查看器、批量处理与 PHI 访问审计；可选模块包括 SAM2 交互式分割、低剂量 CT 模拟与多站点联邦学习，处理结果以 DICOM 写回归档。通过 Docker Compose 部署，GPU 工具需 NVIDIA Container Toolkit，部分工具依赖 FSL/FreeSurfer 主机安装及许可。README 声明其非医疗器械、输出非临床读片。

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

- 集成 dcm4chee-arc、OHIF、Keycloak、iRODS、Airflow 的一体化部署
- 批量处理：对整个队列运行分割/形态测量/配准等工具并导出 ZIP
- SAM2 点击式交互分割，结果存为 DICOM-SEG
- Airflow 编排的多站点联邦学习模块

## 适用场景

- 为科研搭建科室内的 DICOM 归档与 Web 查看环境
- 对影像队列批量运行分割与神经影像处理工具
- 多中心场景下组织联邦学习训练

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4: is a research imaging platform developed at the Department of Diagnostic and
> L7: segmentation pipelines that run against studies in the archive and write their
> L75: |SAMinRAD|`saminrad`|Interactive Segmentation|SAM2 interactive segmentation|

## 星数曲线

```mermaid
xychart-beta
    title "NRAD-UKAachen/InterACT 星数(近 3 点)"
    x-axis ["2026-11-19", "2026-11-25", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-19 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `e1d786b128c4` · [字段定义](../../DATASET.md)*
