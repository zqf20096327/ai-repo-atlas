# houseworthe/house-agents

⭐ 42 · MIT · 推送 2025-11-03 · [GitHub](https://github.com/houseworthe/house-agents) · 个人维护

**Claude Code 专用子代理集合：隔离高开销操作，保持主对话上下文**

面向 Claude Code 用户的四个专用子代理（house-research 搜索、house-git 差异分析、house-bash 命令执行、house-mcp MCP 配置），各自在独立上下文窗口中运行，处理后返回压缩结果。子代理默认使用 Claude Haiku 4.5 模型，可改为继承主会话模型；代理以带 YAML frontmatter 的 .md 文件形式提供，可安装到项目级或用户级 .claude/agents/ 目录。限制包括：每次调用增加约 2-5 秒延迟、代理间无共享内存、MCP 工具访问存在部分限制。

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

- 四个专用子代理各自在独立上下文窗口运行并返回压缩结果
- 子代理默认使用 Claude Haiku 4.5，可编辑配置改为继承主模型
- 代理文件为带 YAML frontmatter 的 .md，支持自定义工具、行为与输出格式
- 支持项目级与用户级两种安装方式

## 适用场景

- 在大型代码库搜索时避免主对话上下文被污染
- 审阅大型 git diff 并获取按影响分级的变更摘要
- 运行测试/构建并获取解析后的摘要而非原始日志
- 生成 MCP 服务器最小可用配置

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: Specialized Claude Code sub-agents for context-efficient workflows. Keep your main conversation clean while delegati
> L25: **House Agents** are specialized Claude Code sub-agents that run in their own context windows. Each agent handles s

## 星数曲线

```mermaid
xychart-beta
    title "houseworthe/house-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `564fea4c6864` · [字段定义](../../DATASET.md)*
