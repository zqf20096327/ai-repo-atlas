# mitre-atlas/atlas-data

⭐ 210 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/mitre-atlas/atlas-data) · [官网](https://atlas.mitre.org) · 组织维护

**MITRE ATLAS 数据仓库：AI 系统对抗 TTP 知识库的权威数据与工具**

分发 MITRE ATLAS（面向 AI 系统的对抗威胁知识库）的 YAML 数据文件，作为权威数据源按月发布，含内容版本与格式版本双轨版本制。附带 Python 包提供 Pydantic schema 与 REST API，用于导入 YAML 到数据库、经 API 编辑、导出 YAML 供评审；CLI 工具可为每个案例研究生成 STIX 2.1 Attack Flow，并产出 STIX、Navigator layer、Excel 等分发格式。面向安全研究人员与 AI 系统威胁建模者。安装依赖 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按月更新的 ATLAS YAML 数据，内容/格式双版本并附 manifest 映射
- REST API 支持导入-编辑-导出 YAML 的数据维护流程
- 生成 STIX 2.1 Attack Flow，保留案例的 leads-to 图结构
- Pydantic schema 与 pytest 校验发布数据的技术成熟度门槛

## 适用场景

- 检索针对 AI 系统的攻击战术、技术与真实案例研究
- 为 AI 安全评估生成 Attack Flow 与 Navigator 层可视化
- 参与 ATLAS 数据的贡献评审与校验流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository distributes data for MITRE ATLAS&trade; (Adversarial Threat Landscape for AI Systems), a public know
> L5: It includes the supporting tooling for parsing, validating, and managing ATLAS data.
> L7: The ATLAS YAML files in this repository are the authoritative source of ATLAS data. The database and REST API suppor

## 星数曲线

```mermaid
xychart-beta
    title "mitre-atlas/atlas-data 星数(近 8 点)"
    x-axis ["2026-10-26", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-19", "2026-11-27", "2026-11-28"]
    y-axis "stars" 202 --> 211
    line [203, 206, 207, 208, 207, 208, 209, 210]
```

2026-10-26 203 → 2026-11-28 210（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `9e0212c488e4` · [字段定义](../../DATASET.md)*
