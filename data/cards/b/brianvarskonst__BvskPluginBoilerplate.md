# brianvarskonst/BvskPluginBoilerplate

⭐ 16 · PHP · MIT · 推送 2026-10-19 · [GitHub](https://github.com/brianvarskonst/BvskPluginBoilerplate) · 个人维护

**面向编码代理的 Shopware 6 插件开发样板（AI-first）**

Shopware 6.7 插件开发模板，定位为供编码代理使用：开发者向 agent 描述需求，agent 通过 rename-plugin 与 verify-plugin 两个 Agent Skills 完成样板改名、功能构建与验证。内置 AGENTS.md（路径/编码风格/验收标准，Claude Code 经 CLAUDE.md 加载）、CI 工作流（PHP 8.2/8.5）。包含命令、控制器、DAL 实体、迁移、计划任务、订阅者等组件示例。README 声明当前处于开发模式、未覆盖全部示例场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AGENTS.md + Agent Skills + CI 的 agent 开发配置
- rename-plugin / verify-plugin 两个技能（后者用 Docker 搭临时 Shopware 验证）
- Shopware 6.7 兼容，要求 PHP >= 8.2 / Composer / PHPUnit >= 11.5

## 适用场景

- 让编码代理从样板生成自定义 Shopware 6 插件
- 参考各类插件组件（控制器/实体/迁移/计划任务等）的写法
- 通过 CI 与 verify-plugin 技能在拉取请求中自动检查插件

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: This boilerplate is made for coding agents. You describe the plugin you want, the agent does the programming. Nobody
> L12: * .agents/skills: step by step skills in the Agent Skills format. `rename-plugin` turns the boilerplate into your o

## 星数曲线

```mermaid
xychart-beta
    title "brianvarskonst/BvskPluginBoilerplate 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-19 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `709e4e6580c8` · [字段定义](../../DATASET.md)*
