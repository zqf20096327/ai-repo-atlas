# Impertio-Studio/Speckle-Claude-Skill-Package

⭐ 14 · TypeScript · MIT · 推送 2026-07-08 · [GitHub](https://github.com/Impertio-Studio/Speckle-Claude-Skill-Package) · 组织维护

**面向 Speckle 数据平台的 25 个确定性 Claude 技能包**

为 Claude 提供关于 Speckle 数据平台（AEC 领域开源数据基础设施）的确定性技能包：25 个 SKILL.md 技能按 core/syntax/impl/errors/agents 五类组织，覆盖对象模型、GraphQL API、Python/C# SDK、Revit/Rhino/Blender/AutoCAD/Tekla 等连接器、viewer 与数据联邦。技能基于 Agent Skills 开放标准，按上下文自动激活；另附带提供 13 个工具的自定义 MCP server 用于直接调用 Speckle API，及 9 个跨技术集成技能。通过 git clone、submodule 或上传 SKILL.md 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25 个确定性技能，覆盖 Speckle 对象模型、SDK、连接器与联邦
- 附带 13 工具的 MCP server 直接交互 Speckle API
- 技能按上下文自动激活（发送数据、GraphQL 查询、调试错误等场景）
- 9 个跨技术集成技能（Speckle↔Blender/Revit/n8n/Docker）

## 适用场景

- 让 Claude 生成正确的 SpecklePy/Speckle.Sdk 代码模式
- 查询 Speckle 流、模型与版本数据
- 诊断 Speckle 传输、转换与认证错误
- 搭建跨 Revit/Blender 等工具的 BIM 数据工作流

## 场景标签

`提示工程` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L12: **25 deterministic Claude AI skills for Speckle Data Platform — the open-source data infrastructure for AEC (Archit
> L14: Built on the Agent Skills open standard.
> L25: With this skill package, Claude produces correct Speckle patterns:

## 星数曲线

```mermaid
xychart-beta
    title "Impertio-Studio/Speckle-Claude-Skill-Package 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `42426e3c5528` · [字段定义](../../DATASET.md)*
