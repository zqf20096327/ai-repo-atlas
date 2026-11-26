# jmagly/aiwg

⭐ 233 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/jmagly/aiwg) · [官网](https://aiwg.io) · 个人维护

**为 Claude Code/Codex/Copilot 等 AI 工具提供可复用项目上下文与工作流**

AIWG 通过部署层将 Markdown/YAML 格式的 agents、skills、rules、templates 复制到各 AI 工具读取的路径，实现一份源文件适配 19 个命名 provider 集成。提供项目/用户/全局三种部署作用域、持久化工件记忆（.aiwg/）、安装修复与 aiwg doctor 健康诊断；可选 Jev 决策卸载、Cockpit 沙箱执行器（Docker/KVM）需显式 opt-in。面向使用编码助手的开发者，MIT 许可，npm 全局安装。

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

- 一份源文件部署到 19 个命名 provider 集成路径，另有 generic 适配器
- 项目/用户镜像/全局三种作用域的部署模式
- 持久化工件记忆 .aiwg/ 与安装器修复、aiwg doctor 诊断
- 可选自托管 Agentic Sandbox（Docker/KVM/libvirt）隔离执行器

## 适用场景

- 为多个 AI 编码工具统一维护一套项目指令与角色工作流
- 在团队仓库中沉淀跨会话的项目决策与工件
- 需要审计的隔离环境中运行长时 agent 任务

## 场景标签

`编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L6: **Reusable project context and specialist workflows for the AI tools you already use.**
> L163: AIWG gives your AI assistant reusable project context and specialist workflows. Its deployment layer connects thos
> L164: instructions to your provider: `aiwg use` copies markdown and YAML source files into the paths each provider reads

## 星数曲线

```mermaid
xychart-beta
    title "jmagly/aiwg 星数(近 9 点)"
    x-axis ["2026-10-24", "2026-10-30", "2026-10-31", "2026-11-06", "2026-11-08", "2026-11-15", "2026-11-21", "2026-11-22", "2026-11-26"]
    y-axis "stars" 224 --> 234
    line [225, 226, 227, 225, 229, 230, 232, 233, 233]
```

2026-10-24 225 → 2026-11-26 233（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `2c0c2584d656` · [字段定义](../../DATASET.md)*
