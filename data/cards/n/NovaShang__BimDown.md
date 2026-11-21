# NovaShang/BimDown

⭐ 18 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/NovaShang/BimDown) · [官网](https://bim.jouledown.com) · 个人维护 · 中文 README

**给建筑师与 AI agent 用的纯文本 BIM 文件格式及配套工具**

BimDown 定义一种开放纯文本 BIM 格式：一栋建筑是按楼层组织的文件夹，含 CSV 属性表与 GeoJSON/SVG 几何，人和脚本、AI agent 均可直接读写、diff 与 SQL 查询（内置 DuckDB）。仓库提供 bimdown CLI（validate/render/query/IFC 导入）、浏览器 2D/3D 编辑器、Revit 2025+ 双向同步插件，以及面向 Claude Code、Codex、Cursor 等 agent 的技能文件。格式约 LOD 200 粒度，面向早期设计与既有建筑；施工级细节仍需 Revit 等完整 BIM 工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 建筑模型为 CSV + GeoJSON/SVG 文本文件，Git 行级 diff 与合并
- bimdown query 将模型载入 DuckDB 用标准 SQL 查询
- 提供 Revit 2025+ 插件双向同步及 IFC2x3/IFC4 导入导出
- 提供 agent skill，供 Claude Code/Codex/Cursor 等生成与校验模型

## 适用场景

- 让编码 agent 直接读写建筑模型并渲染平面图验证
- 对建筑数据做 SQL 查询和 Git 版本管理
- 在 Revit 与轻量文本模型之间往返编辑
- 从照片或文字描述生成可编辑的早期设计模型

## 场景标签

 · 领域:建筑/工程/AEC

## 证据(README 行号)

> L11: **BimDown is an open, plain-text BIM format: a building is a folder of CSV attribute tables and GeoJSON (or SVG) ge
> L21: - **Let an AI agent build or edit the model**: install the agent skill and ask Claude Code, Codex, Cursor or Gemini
> L230: BimDown is a **LOD 200 lightweight format**, aimed at early design and documenting existing buildings. It captures


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ac419aabadc2` · [字段定义](../../DATASET.md)*
