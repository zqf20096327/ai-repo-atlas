# mohitagw15856/pm-claude-skills

⭐ 1,612 · JavaScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/mohitagw15856/pm-claude-skills) · [官网](https://mohitagw15856.github.io/pm-claude-skills/) · 个人维护 · 中文 README

**面向专业工作场景的 1,390 个 Agent 技能 markdown 库**

开源的 Agent Skills 库，由纯 markdown SKILL.md 文件组成，每个技能包含工作框架、输出模板、质量检查与反模式，用于教 AI 助手完成 PRD、事后复盘、合同解读、周报等专业任务。通过 npx 安装器、Claude Code 插件目录、MCP 服务器或 REST API 分发，兼容 Claude、ChatGPT、Gemini、Cursor、Codex 等工具；含 21 个面向常驻 agent（如 Claude Duet）的技能，带审批门与注入演练沙盒。MIT 许可，73 个技能有简体中文版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,390 个纯 markdown 技能文件，安装/卸载即复制/删除文本文件
- 通过 npx 安装器、MCP 服务器与只读 REST API 三种途径分发技能
- 21 个面向常驻 agent 的 Duet-ready 技能，含审批门与 12 条注入演练指令
- 73 个技能提供简体中文版，含周报、考公、劳动合同等中文场景技能包

## 适用场景

- 让 AI 助手按专业标准产出 PRD、风险清单与干系人更新
- 解读租约、账单、合同等文件中的金额条款
- 为常驻 agent 配置晨报、审批策略与终止开关
- 用中文生成周报、述职等职场文档

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L61: PM Skills is an open-source library of 1390 Agent Skills — plain-markdown SKILL.md files that teach an AI assistant
> L131: A skill is one plain-markdown SKILL.md file: a description that tells your assistant when to load it, plus the wor
> L172: Install any bundle: `/plugin install pm-decoders@pm-claude-skills`, or `npx pm-claude-skills add --bundle pm-decod

## 星数曲线

```mermaid
xychart-beta
    title "mohitagw15856/pm-claude-skills 星数(近 26 点)"
    x-axis ["2026-10-19", "2026-10-23", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 1457 --> 1626
    line [1471, 1478, 1488, 1489, 1494, 1499, 1503, 1505, 1532, 1539, 1540, 1542, 1546, 1549, 1553, 1563, 1570, 1573, 1578, 1581, 1584, 1589, 1595, 1603, 1608, 1612]
```

2026-10-19 1,471 → 2026-11-28 1,612（+141）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `2e0cb9bcc73a` · [字段定义](../../DATASET.md)*
