# sap-tutorials/tutorials-ims

⭐ 15 · JavaScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/sap-tutorials/tutorials-ims) · [官网](https://sap-tutorials.github.io/tutorials-ims/) · 组织维护

**SAP 开发者门户的教程托管平台：构建时拉取 GitHub 教程并静态渲染**

为 developers.sap.com 提供教程托管的平台，替代 Adobe Experience Manager 与旧 Java IMS 后端。构建时从 sap-tutorials GitHub 组织拉取教程 markdown，用 Hugo 配合 SAP Fundamental Styles 渲染静态页面，部署在 SAP BTP Cloud Foundry 上（AppRouter + XSUAA 认证）；CAP Node.js 后端提供进度跟踪、事件管理与内容发布，数据存于 SAP HANA Cloud。面向 SAP 开发者与教程作者，需 Node.js >= 20 与 npm 本地运行，包含从 Java IMS 的数据迁移脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 构建时从 GitHub 拉取教程 markdown 生成 Hugo 静态页
- CAP Node.js 后端提供进度跟踪、事件管理与内容发布
- SAP BTP Cloud Foundry 部署，AppRouter + XSUAA 认证
- 提供 Java IMS → CAP 的数据迁移与对比脚本

## 适用场景

- 浏览和检索 developers.sap.com 上的 SAP 教程
- 作为教程作者托管与发布教程内容
- 运营方执行内容发布、QA 预览与数据迁移

## 场景标签

 · 领域:开发者教育/内容平台

## 证据(README 行号)

> L3: A tutorial hosting platform for developers.sap.com that replaces both Adobe Experience Manager (AEM) and the legacy 
> L5: > **Production system** replacing AEM tutorial hosting, Git-based authoring interface, and Java IMS backend on devel

## 星数曲线

```mermaid
xychart-beta
    title "sap-tutorials/tutorials-ims 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `3b8e75e6421a` · [字段定义](../../DATASET.md)*
