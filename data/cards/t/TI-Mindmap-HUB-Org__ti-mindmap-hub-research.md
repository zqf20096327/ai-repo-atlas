# TI-Mindmap-HUB-Org/ti-mindmap-hub-research

⭐ 20 · JavaScript · NOASSERTION · 推送 2026-10-25 · [GitHub](https://github.com/TI-Mindmap-HUB-Org/ti-mindmap-hub-research) · [官网](https://ti-mindmap-hub.com/landingpage) · 个人维护

**威胁情报 AI 平台的公开研究文档：方法、STIX 示例与集成指南**

为 TI Mindmap HUB 平台提供的公开研究资料库：该平台自动监控 OSINT 来源，用 LLM 生成摘要、思维导图与结构化报告，抽取 IOC（IP/域名/哈希/CVE）、映射 MITRE ATT&CK、导出 STIX 2.1，并暴露含 27 个工具的 MCP 服务器供 AI 助手接入。本仓库仅含文档（MkDocs）、方法论、schema 与集成指南，核心代码在私有仓库维护，学术合作部分含大学项目。

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

- 平台功能：LLM 分析、IOC 抽取、MITRE ATT&CK 映射、STIX 2.1 导出
- MCP 服务器提供 27 个工具，支持 Claude/VS Code Copilot 等客户端
- 知识图谱（Beta）可视化威胁关系
- 与大学合作的 STIX 2.1 Generator 项目（UNISA）

## 适用场景

- 查阅 AI 威胁情报处理流水线的方法论与 STIX 数据模型
- 通过 MCP 客户端查询最新勒索报告或 CVE 影响
- 将 STIX 输出导入 SIEM/SOAR/TIP 平台

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: TI Mindmap HUB is an **independent research project** exploring the application of Generative AI to Cyber Threat In
> L78: > **Note**: The core application code is maintained in private repositories. This public repository focuses on docu

## 星数曲线

```mermaid
xychart-beta
    title "TI-Mindmap-HUB-Org/ti-mindmap-hub-research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a342ab780e66` · [字段定义](../../DATASET.md)*
