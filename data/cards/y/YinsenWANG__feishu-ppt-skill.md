# YinsenWANG/feishu-ppt-skill

⭐ 25 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/YinsenWANG/feishu-ppt-skill) · 个人维护 · 中文 README

**AI agent 技能包：通过 51 套 XML 模板生成飞书原生幻灯片**

面向 AI agent 的 Feishu/Lark 幻灯片构建技能，入口为 SKILL.md。提供 51 套 960×540 原生 SML 布局模板（覆盖封面、目录、数据图表、流程架构等类别），通过显式 bindings 字段填充内容，脚本生成 XML、本地 SVG 近似预览与自动化校验（schema/布局/主题），再经 lark-cli 执行截图与创建等实际飞书操作。含三方对比脚本用于既有演示文稿编辑。要求 Python 3.10+，Lark CLI 仅在执行真实飞书操作时需要（测试至 CLI 1.0.86）。不处理通用海报或 .pptx 导出；代码 MIT 许可，品牌素材除外。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 51 套原生 SML XML 布局模板，按 10 类场景组织
- 显式 bindings 内容绑定与未完成字段草稿流程
- schema/布局/主题统一校验与本地 SVG 近似预览
- 三方快照对比脚本支持既有演示文稿编辑

## 适用场景

- AI agent 按品牌规范自动生成飞书演示文稿
- 开发者以命令行从模板批量产出幻灯片 XML
- 编辑已发布飞书演示文稿前做冲突检查

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: Create and edit native **Lark / Feishu slides** using 51 reusable XML layouts, explicit content bindings, local prev
> L11: Requires Python **3.10+**. Install into your agent's skill directory using its normal installation workflow, or clo
> L22: Lark CLI is only needed for actual Feishu operations and official screenshots. Commands below were checked against 

## 星数曲线

```mermaid
xychart-beta
    title "YinsenWANG/feishu-ppt-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [26, 25, 25]
```

2026-10-18 26 → 2026-10-29 25（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `10e89c8d8270` · [字段定义](../../DATASET.md)*
