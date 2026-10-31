# a1st-dev/aix

⭐ 21 · TypeScript · 推送 2026-10-05 · [GitHub](https://github.com/a1st-dev/aix) · [官网](https://aix.a1st.dev) · 个人维护

**AI 编辑器配置的统一管理工具：一份 ai.json 用于多家编辑器**

以 ai.json 为单一配置源，集中定义 skills、agents、prompts、rules、hooks、plugins、marketplaces 与 MCP server 配置，再分发到 claude-code、cursor、copilot、windsurf、codex 等 9 种编辑器。提供 npm 全局安装的 CLI：init/add/install/sync/validate 等命令；aix sync 通过规范化中间格式在编辑器间迁移配置。支持可选 ai.lock.json 锁文件（SHA-512/SHA-256 哈希检测配置漂移），原子写入并自动备份回滚。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 ai.json 定义全部 agent 配置，分发到 9 种受支持编辑器
- aix sync 在编辑器间迁移配置，无需两两转换器
- 可选 ai.lock.json 锁文件以哈希检测配置漂移
- aix search 发现并添加 MCP server 与 skill；支持从 GitHub/GitLab/npm extends 远程配置

## 适用场景

- 团队统一并版本管理各成员的 AI 编辑器配置
- 更换编辑器时迁移已有 skills/MCP 配置
- 在多编辑器环境消除重复配置

## 场景标签

 · 领域:开发工具/配置管理

## 证据(README 行号)

> L8: `aix` is like NPM + package.json for your AI agent editor configuration.
> L33: `aix` gives you one source of truth for your skills, agents, prompts, rules, hooks, plugins, marketplaces,

## 星数曲线

```mermaid
xychart-beta
    title "a1st-dev/aix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `75ac12722449` · [字段定义](../../DATASET.md)*
