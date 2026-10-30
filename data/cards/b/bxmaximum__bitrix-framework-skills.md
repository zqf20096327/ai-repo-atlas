# bxmaximum/bitrix-framework-skills

⭐ 47 · PHP · MIT · 推送 2026-10-12 · [GitHub](https://github.com/bxmaximum/bitrix-framework-skills) · [官网](https://bxmax.ru) · 组织维护

**1С-Битрикс D7 开发的 AI agent 技能库（50 个 SKILL.md）**

面向 1С-Битрикс（D7 内核）与 Битрикс24 开发者的 agent 技能集合：50 个 SKILL.md 技能覆盖 ORM、控制器、缓存、安全、信息块、电商、CRM、REST、MCP 等主题，供 Claude Code、Cursor、Codex 等 agent 读取，使模型按 D7 规范而非旧 API 写代码。通过 npx skills 一条命令安装，技能内容对照内核 main 26.800.0 校验，PHP 示例经 php -l 与自研脚本验证。由 BXMax 社区维护，每月更新。

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

- 50 个 SKILL.md 技能，大技能拆分为 rules/*.md 按需加载，避免占用上下文
- 技能与内核 main 26.800.0 对照校验，PHP 示例经 php -l 和 verify-skills.php 验证
- npx skills add 一条命令安装，兼容读取 .agents/skills/ 的多种 agent
- 含 Битрикс24 REST/MCP 技能，可接入官方 MCP 文档服务器

## 适用场景

- 让 Claude Code/Cursor/Codex 在 Битрикс 项目中按 D7 规范生成代码
- 查找 ORM、安全、信息块、电商等具体主题的开发规则
- 为 Битрикс24 REST/MCP 开发配置 agent 参考资料

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Скиллы для Claude Code, Cursor и Codex, чтобы ИИ писал код на 1С-Битрикс по канону D7, а не legacy. 50 скиллов: ORM,
> L87: Каждый скилл — `skills/<name>/SKILL.md`. Большие скиллы разбиты на темы в `rules/*.md`: агент читает только нужный 

## 星数曲线

```mermaid
xychart-beta
    title "bxmaximum/bitrix-framework-skills 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29", "2026-10-30"]
    y-axis "stars" 44 --> 48
    line [45, 46, 47, 47]
```

2026-10-18 45 → 2026-10-30 47（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e3ca307c7c79` · [字段定义](../../DATASET.md)*
