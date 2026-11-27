# yonatangross/orchestkit

⭐ 309 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/yonatangross/orchestkit) · [官网](https://orchestkit.dev) · 个人维护

**为 Claude Code 等编程 agent 提供 115 技能/36 agent/163 钩子的插件包**

MIT 许可的开源插件集，为 Claude Code、Cursor、Codex 等 8 个编程 agent 宿主提供技能、agent 与钩子。技能覆盖工作流、FastAPI、React 19、测试、安全、数据库设计等，按需加载；agent 为后端架构师、安全审计等角色；钩子跨 32 个生命周期事件实现提交前检查、git 保护、质量门禁。数据写入本地文件，远程同步默认关闭。各宿主能力差异以实测矩阵呈现，部分宿主不支持钩子。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 115 个技能（82 核心 + 33 ork-extras 参考技能），按需加载
- 163 个钩子覆盖 32 个生命周期事件：密钥写入阻断、git 保护、质量门禁
- 8 个宿主宿主支持矩阵，附实测日期与证据文件路径
- 数据仅写本地磁盘文件，远程同步默认关闭且可逐项关闭

## 适用场景

- 让 Claude Code 持久掌握团队技术栈与编码规范，无需每次重复说明
- 在提交前自动执行测试、阻断敏感信息写入等质量门禁
- 通过 /ork:implement 用并行 agent 完成全栈实现

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L17: OrchestKit is free and open source (MIT, no account): skills and agents for Claude Code, Cursor, Codex and five mor
> L107: |** 115 Skills**|82 in core `ork` (workflows, FastAPI, React 19, testing, security, database design) and 33 opt-in
> L170: OrchestKit is a quality-gate plugin, so its hooks are the product rather than an

## 星数曲线

```mermaid
xychart-beta
    title "yonatangross/orchestkit 星数(近 13 点)"
    x-axis ["2026-10-25", "2026-10-29", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-14", "2026-11-15", "2026-11-18", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 297 --> 310
    line [298, 299, 300, 298, 300, 301, 302, 303, 304, 305, 306, 309, 309]
```

2026-10-25 298 → 2026-11-27 309（+11）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `e677cc058fa3` · [字段定义](../../DATASET.md)*
