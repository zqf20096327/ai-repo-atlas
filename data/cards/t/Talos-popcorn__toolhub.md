# Talos-popcorn/toolhub

⭐ 17 · TypeScript · AGPL-3.0 · 推送 2026-09-07 · [GitHub](https://github.com/Talos-popcorn/toolhub) · 个人维护 · 中文 README

**自托管 AI agent 工具执行平台：任意脚本文本即变工具**

用 Bun 编写的自托管开源平台，面向为 AI agent 提供、编排与安全执行工具的开发者：任意语言脚本（Bun/Python/Go/Bash 等）经 Runner 在隔离临时工作区执行（注入代码与依赖、运行、输出、清理），以文件树结构经 listTools()/callTool() 按需导航，避免在系统提示中硬编码函数。支持多实例无限嵌套联邦（REMOTE 节点）、双模式 MCP 引擎（Stdio 与 Stateful Pool）及 MCP Promote 转原生工具，另有 Sublime Text IDE Bridge 与 .toolpack 导入导出。无需 Docker，AGPL-3.0 许可另有商业授权通道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任意语言脚本（Bun/Python/Go/Bash/PHP/Deno/C++）即时转为 agent 工具
- 工具以层级文件树组织，listTools()/callTool() 按需导航，减少上下文占用
- 无限嵌套联邦（hub→hub→hub），带路径规范化与循环保护
- 双模式 MCP 引擎（Stdio 无状态 + Stateful Pool）与 MCP Promote 转换

## 适用场景

- 把现有命令行脚本快速挂载给 AI agent 调用
- 多个 ToolHub 实例组成联邦统一暴露工具路径
- 为 Puppeteer/SSH 等有状态会话维护 MCP 进程池

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **TOOL HUB** is a high-performance, self-hosted, open-source platform for creating, orchestrating, federating, and s
> L7: Stop hardcoding functions into system prompts and overloading model context windows with hundreds of API schemas. **

## 星数曲线

```mermaid
xychart-beta
    title "Talos-popcorn/toolhub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `6dd2ee2e797b` · [字段定义](../../DATASET.md)*
