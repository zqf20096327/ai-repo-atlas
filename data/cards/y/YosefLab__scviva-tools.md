# YosefLab/scviva-tools

⭐ 15 · Python · BSD-3-Clause · 推送 2026-10-28 · [GitHub](https://github.com/YosefLab/scviva-tools) · [官网](https://yoseflab.github.io/scviva-tools/) · 组织维护

**空间转录组分析统一工具包：整合七个空间模型与下游分析**

基于 scvi-tools 构建的空间转录组学分析工具包，将 scVIVA、DestVI、ResolVI、GIMVI、Stereoscope、Tangram、Harreman 七个模型作为一等公民统一收录，覆盖表征学习、细胞类型去卷积、噪声校正、基因插补、空间映射与代谢交换推断。提供仿 scanpy 的 scviva.tl/scviva.pl 接口与惰性导入机制，GIMVI 等外部模型置于 scviva.external 命名空间。以 pip 安装的 Python 库形式提供，附文档与教程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 七个空间转录组模型统一收录（scVIVA/DestVI/ResolVI/GIMVI/Stereoscope/Tangram/Harreman）
- 仿 scanpy 的 scviva.tl/scviva.pl 接口，可选依赖惰性导入
- Harreman 支持整合 DestVI/ResolVI/SCVIVA 输出做代谢交换与细胞通信分析
- 提供用户指南、API 参考与各模型教程

## 适用场景

- 对空间转录组数据做细胞类型去卷积
- 配对 scRNA-seq 与空间数据的基因插补和映射
- 推断空间数据中的代谢交换与细胞间通信

## 场景标签

 · 领域:生物信息学/空间转录组学

## 证据(README 行号)

> L3: Consolidated spatial transcriptomics analysis toolkit based on scvi-tools.
> L5: Provides seven spatial transcriptomics models and tools as first-class citizens:

## 星数曲线

```mermaid
xychart-beta
    title "YosefLab/scviva-tools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6c638ff3319f` · [字段定义](../../DATASET.md)*
