# Vvkmnn/claude-emporium

⭐ 80 · JavaScript · 推送 2026-03-05 · [GitHub](https://github.com/Vvkmnn/claude-emporium) · 个人维护

**面向 Claude Code 的插件市场：六个包装 MCP 服务器的自动化插件**

为 Claude Code 提供的插件市场（marketplace），含六个插件：praetorian（上下文压缩前保存/恢复）、historian（搜索历史会话，9 个搜索工具）、oracle（并行搜索 17 个来源推荐技能/插件/MCP）、gladiator（观察工具失败并沉淀模式）、vigil（危险操作前保存检查点与恢复）、orator（按 Anthropic 实践对提示词打分与重构，无 LLM 调用）。架构上插件不含业务逻辑，通过 hooks 触发各插件自带的 MCP 服务器执行工作；插件间通过读取 settings.json 自动检测兄弟插件并协同。安装即自动注册 MCP、hooks、commands 与 skills。要求 Claude Code，除 Node.js 外无其他依赖，插件存储在项目本地 .claude/ 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六个插件各包装一个独立 MCP 服务器，hooks 触发、MCP 执行
- 插件间自动检测兄弟插件并产生协同行为
- orator 无 LLM 调用、无网络、纯内存地评分与重构提示词
- 无外部 API 调用、无后台进程、无数据库，依赖仅 Node.js

## 适用场景

- 在压缩（compaction）前后保存与恢复 Claude Code 会话上下文
- 复用历史会话中的解决方案，避免重复研究/调试
- 在执行危险命令前自动保存文件检查点并可恢复
- 按 Anthropic 最佳实践评分与优化子代理提示词

## 场景标签

`提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L4:  a (roman) plugin marketplace for claude code
> L27: Six plugins that wrap standalone MCP servers with automation hooks, commands, and skills. No code duplication: plug
> L219: Each plugin is a thin wrapper. hooks inject prompts that trigger MCP tools at high-impact moments. plugins contain

## 星数曲线

```mermaid
xychart-beta
    title "Vvkmnn/claude-emporium 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 79 --> 82
    line [80, 81, 80]
```

2026-10-18 80 → 2026-10-31 80（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `550f3fe05a09` · [字段定义](../../DATASET.md)*
