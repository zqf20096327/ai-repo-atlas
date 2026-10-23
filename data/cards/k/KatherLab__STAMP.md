# KatherLab/STAMP

⭐ 132 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/KatherLab/STAMP) · 组织维护

**病理全切片图像到生物标志物预测的弱监督深度学习流程**

面向计算病理学研究的端到端弱监督深度学习流水线：从千兆像素 H&E 全切片图像出发，无需像素级标注，通过瓦片化、特征提取（支持 20+ 病理基础模型如 Virchow-v2、UNI-v2、TITAN）与 Transformer 聚合的 MIL 训练，完成分类、多标签、回归与 Cox 生存分析等任务，并生成热图用于模型审计。提供零代码 CLI 与 YAML 配置，可在本地或 HPC（SLURM）运行；附 MCP 模块可接入 agentic 工作流。协议发表于 Nature Protocols。安装依赖 uv（GPU 流程必须），GPU 扩展仅有 Linux 预编译 wheel，macOS/Windows 仅支持 CPU 版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 弱监督端到端 MIL 流程，无需像素级标注
- 开箱支持 20+ 病理基础模型（瓦片级/切片级）
- 统一框架支持分类、多标签、回归与 Cox 生存分析
- 内置热图与 top-tile 导出，及 MCP 模块支持

## 适用场景

- 临床研究者从 H&E 切片预测分子标志物或患者生存
- ML 工程师在多中心队列上做可复现的生物标志物建模
- 对外部验证队列部署已训练模型并生成解释热图

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: STAMP is an **end‑to‑end, weakly‑supervised deep‑learning pipeline** that helps discover and evaluate candidate ima
> L18: * 🧩 **Model‑rich**: Out‑of‑the‑box support for **+20 foundation models** at tile level (e.g., *Virchow‑v2*, *UNI‑v2
> L20: * 🧮 **Multi-task learning**: Unified framework for **classification**, **multi-target classification**, **regressio

## 星数曲线

```mermaid
xychart-beta
    title "KatherLab/STAMP 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 130 --> 133
    line [131, 132, 132]
```

2026-10-18 131 → 2026-10-23 132（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `ea667848f405` · [字段定义](../../DATASET.md)*
