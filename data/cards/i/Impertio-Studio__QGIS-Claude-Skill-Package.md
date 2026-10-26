# Impertio-Studio/QGIS-Claude-Skill-Package

⭐ 36 · MIT · 推送 2026-07-08 · [GitHub](https://github.com/Impertio-Studio/QGIS-Claude-Skill-Package) · 组织维护

**教 Claude 编写 QGIS/PyQGIS 代码的确定性技能包（19 项）**

面向 Claude Code 的技能包：以 19 个 SKILL.md 格式技能（含 references 中的 API 签名、代码示例与反模式对照）教模型编写生产级 PyQGIS 代码，覆盖核心架构、语法、8 类 GIS 实现工作流（矢量/栅格分析、制图布局、PostGIS、3D、网络分析等）、错误诊断与编排技能。技能以确定性 ALWAYS/NEVER 语言编写，每文件小于 500 行，目标 QGIS 3.44 LTR 并附 4.0 兼容说明；另附 15 个跨技术（BIM/IFC、Docker）伴侣技能与推荐的配套 MCP 服务器清单。通过 claude install-skill 命令或 git clone 手动安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个技能按 Core/Syntax/Implementation/Errors/Agents 五类组织
- 每个技能含 methods/examples/anti-patterns（WRONG/CORRECT 对照）
- 确定性 ALWAYS/NEVER 语言，SKILL.md 均小于 500 行
- 面向 QGIS 3.44 LTR，附 4.0 Qt6 兼容说明与配套 MCP 服务器清单

## 适用场景

- 让 Claude Code 生成符合规范的 PyQGIS 代码与 QGIS 插件
- 规划空间分析工作流或自动生成制图成品
- 调试 QGIS 坐标系与数据加载错误

## 场景标签

`代码生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L13: A skill package that teaches Claude how to write correct, production-quality PyQGIS code. Every skill uses determin
> L98: qgis-{category}-{topic}/
> L99: ├── SKILL.md              # Main skill (<500 lines, YAML frontmatter)

## 星数曲线

```mermaid
xychart-beta
    title "Impertio-Studio/QGIS-Claude-Skill-Package 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2bb7f1c4b1ee` · [字段定义](../../DATASET.md)*
