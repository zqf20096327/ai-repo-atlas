# manifest-cyber/aibom

⭐ 47 · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/manifest-cyber/aibom) · [官网](https://www.manifestcyber.com) · 组织维护

**AI/ML 模型物料清单（AIBOM）的社区 wiki 与规范提案**

由 Manifest 维护的社区仓库，围绕 AI/ML 模型物料清单（AIBOM/MLBOM）构建知识库：提出一份建议的 AIBOM 最小字段模型，覆盖模型详情（名称/版本/许可证/依赖库/来源）、架构（数据集、架构家族、父模型/基座模型、输入输出）、使用范围、伦理与环境影响考量和数字签名认证等章节；/examples 目录提供 CycloneDX 等现有格式及基于 CycloneDX 扩展的自定义格式示例。面向 BOM（SBOM/AIBOM）实践者与供应链透明度相关人员，通过 Slack 社区协作，附带白皮书说明研究发现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提出分章节的 AIBOM 最小字段模型（模型详情/架构/使用/考量/认证）
- /examples 目录含 CycloneDX 现有格式与自定义扩展格式示例
- 基于全球 AI/ML 专家访谈的白皮书记录用例与差距
- 维护 BOM 实践者社区（Slack）

## 适用场景

- 为自研或第三方 AI 模型编写 AIBOM 时参考字段清单
- 了解现有 SBOM 格式（CycloneDX/SPDX）在 AI 模型透明度上的缺口
- 参与 BOM 供应链透明度的社区协作与最佳实践分享

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: This is where we hope to build community around AI bills of material (AIBOMs). In this repository, we have and maint
> L4:  (1) A proposed minimum - or highly suggested - elements for AIBOMs (below)
> L5:  (2) Examples of AIBOMs in the `/examples` folder, which contain both AIBOM samples in existing formats (such as Cyc

## 星数曲线

```mermaid
xychart-beta
    title "manifest-cyber/aibom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-28 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0096a9467c3f` · [字段定义](../../DATASET.md)*
