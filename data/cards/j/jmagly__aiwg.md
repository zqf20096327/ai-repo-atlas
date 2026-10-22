# jmagly/aiwg

⭐ 225 · TypeScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/jmagly/aiwg) · [官网](https://aiwg.io) · 个人维护

**为多种 AI 编码工具提供可复用上下文与工作流的部署框架**

AIWG 将 agents、skills、rules、templates 与工作流工具打包为 Markdown+YAML 源文件，通过 `aiwg use` 命令部署到各 AI 提供商读取的路径，使单一事实源跨 18 个具名提供商集成（claude、codex、copilot、cursor 等）工作，另有第十九个 generic 适配器输出可移植文件。围绕核心提供持久化工件记忆（.aiwg/）、后台编排、自主循环、工件索引、成本遥测与 Jev 决策支持（将有界 LLM 决策卸载以节省 token）。支持项目/用户/全局三种部署范围与多项目工作区。可选安装 AIWG Cockpit 与自托管 Agentic Sandbox 执行器（Docker 或 KVM/libvirt）。README 明确说明：角色定义不是独立模型，书面规则不构成约束已执行的证明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- `aiwg use` 将 markdown/YAML 资产部署到各提供商路径，单一事实源跨 18 个具名提供商集成
- 持久化工件记忆（.aiwg/）与跨会话决策记录
- Jev 决策支持将有界 LLM 决策卸载以节省 token
- 可选自托管 Agentic Sandbox 隔离执行器（Docker/KVM-libvirt）

## 适用场景

- 让 Claude Code、Copilot、Cursor 等工具共享同一套项目上下文和工作流
- 在架构评审、安全审查等任务中让多角色 agent 协作并留痕
- 跨会话保存项目决策与工件，避免从对话碎片重建

## 场景标签

`多智能体` `提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L157: AIWG gives your AI assistant reusable project context and specialist workflows. Its deployment layer connects thos
> L158: instructions to your provider: `aiwg use` copies markdown and YAML source files into the paths each provider reads
> L159: one source of truth works across 18 named provider integrations. A nineteenth `generic` adapter emits portable fil

## 星数曲线

```mermaid
xychart-beta
    title "jmagly/aiwg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 223 --> 225
    line [224, 224]
```

2026-10-18 224 → 2026-10-21 224（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `17ac291c1560` · [字段定义](../../DATASET.md)*
