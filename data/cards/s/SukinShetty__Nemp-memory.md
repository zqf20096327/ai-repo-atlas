# SukinShetty/Nemp-memory

⭐ 139 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/SukinShetty/Nemp-memory) · [官网](https://www.nemp.dev/) · 个人维护

**给 Claude Code 的本地记忆插件：保存并检索决策与上下文**

面向 Claude Code 的记忆插件：通过 Markdown 命令让宿主 agent 读写本地 JSON 文件（项目级 .nemp/ 与全局 ~/.nemp/），实现决策、偏好与项目上下文的保存、检索、更新与删除。检索基于关键词扩展，不依赖嵌入服务、数据库或独立记忆服务器；支持 CLAUDE.md 导入导出与可选自动同步。v0.3.0 为 MIT 许可的开源版本，Pro 版付费功能尚未实现。

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

- 本地 JSON 存储，无需数据库、嵌入服务或记忆服务器
- 关键词扩展检索，支持项目级与全局两级记忆
- CLAUDE.md 导出、可选自动同步与漂移审查（/nemp:sync）
- 访问日志查看与 80 项诊断清单（/nemp:log、/nemp:health）

## 适用场景

- 跨会话保留项目决策、约定与已知坑点
- 跨项目复用个人偏好（/nemp:save-global）
- 把可信上下文同步进 CLAUDE.md 供后续会话使用

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Nemp Open v0.3.0** is the free, MIT-licensed foundation: agent-guided commands, keyword-based retrieval and `CLAU
> L100: Nemp's Markdown commands describe how the host agent reads and writes files. The Claude Code plugin supplies the c
> L115: Your saved memory files stay in your project or home directory. Nemp Open does not add a hosted memory backend or 

## 星数曲线

```mermaid
xychart-beta
    title "SukinShetty/Nemp-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 138 --> 140
    line [139, 139]
```

2026-10-18 139 → 2026-10-31 139（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `787238d7ac6a` · [字段定义](../../DATASET.md)*
