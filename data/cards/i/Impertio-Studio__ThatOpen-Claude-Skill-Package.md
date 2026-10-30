# Impertio-Studio/ThatOpen-Claude-Skill-Package

⭐ 19 · MIT · 推送 2026-07-08 · [GitHub](https://github.com/Impertio-Studio/ThatOpen-Claude-Skill-Package) · 组织维护

**面向 Claude Code 的 ThatOpen BIM 开发技能包（18 个确定性技能）**

为 Claude Code 项目提供的技能集合：包含 18 个覆盖 ThatOpen Engine 3.3.x 生态的确定性技能，内容含 API 签名、可运行代码示例与反模式文档，均溯源自 ThatOpen 官方仓库。技能按核心架构、语法模式、实现流程、错误处理、引导式工作流五类组织，另含 15 个跨技术栈 AEC 集成伴生技能（如 IfcOpenShell↔web-ifc）。安装方式为 git clone 或 git submodule 到项目的 .claude/skills/ 目录。目标版本锁定 @thatopen/components 3.3.x、web-ifc 0.0.77+、three ≥0.175。

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

- 18 个技能覆盖架构、语法、实现、错误处理、Agent 工作流五类
- 每个技能含 API 签名、示例与反模式文档，规则采用 ALWAYS/NEVER 确定性表述
- 版本锁定 ThatOpen 3.3.x / web-ifc 0.0.77+ / three ≥0.175
- 15 个跨技术栈伴生技能（IfcOpenShell↔web-ifc、IFC↔Three.js 等）

## 适用场景

- 让 Claude Code 按 ThatOpen 官方 API 模式开发 BIM 应用
- 从零搭建 BIM 查看器或分析 IFC 模型并生成报告
- 排查 WASM 加载失败、内存泄漏等 ThatOpen 常见错误

## 场景标签

 · 领域:建筑信息模型（BIM）/AI 技能

## 证据(README 行号)

> L13: A collection of **18 deterministic skills** that give Claude Code deep knowledge of the ThatOpen BIM engine ecosyst
> L21: git clone https://github.com/OpenAEC-Foundation/ThatOpen-Claude-Skill-Package.git .claude/skills/thatopen

## 星数曲线

```mermaid
xychart-beta
    title "Impertio-Studio/ThatOpen-Claude-Skill-Package 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0f9124708128` · [字段定义](../../DATASET.md)*
