# sharpdeveye/maestro

⭐ 591 · TypeScript · MIT · 推送 2026-04-29 · [GitHub](https://github.com/sharpdeveye/maestro) · [官网](https://maestroskills.dev) · 个人维护

**面向 AI 编程 agent 的工作流技能包：25 命令+记忆层+审计**

以技能（skill）形式装入 AI 编程 agent（Cursor、Claude Code、Gemini CLI、Codex 等 10 种工具）的工作流改进工具集：1 个核心 agent-workflow 技能配 7 个领域参考文件（提示工程、上下文管理、工具编排、多 agent 架构、反馈循环、知识系统、安全护栏），25 个命令用于诊断、精炼、加固、加速等工作流操作。v2 增加跨会话持久记忆层（决策日志、审计日志、会话摘要）与命令调用的成本/时长记录，也可作为 MCP 服务器运行（stdio/HTTP），暴露 25 个 prompt、10 个工具、8 个资源。通过 npx 安装或手动复制目录。

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

- 25 个命令覆盖分析/修复/增强/工具四类工作流操作
- 7 个领域参考文件 + 反模式清单
- 跨会话记忆层：决策日志、审计日志（含成本估算 ±20%）、会话摘要
- 支持 10 种 AI 编程工具，并可作 MCP 服务器（stdio/HTTP）运行

## 适用场景

- 让我的 Cursor/Claude Code 等 agent 按规范工作流处理任务
- 审计并改进已有 agent 工作流的质量与成本
- 跨会话保留 agent 的决策记录与会话历史

## 场景标签

 · 领域:开发者工具/AI agent 工作流

## 证据(README 行号)

> L16: ## What is Maestro?
> L32: npx skills add sharpdeveye/maestro
> L177: |Cursor|`.cursor/skills/`|

## 星数曲线

```mermaid
xychart-beta
    title "sharpdeveye/maestro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 590 --> 592
    line [591, 591]
```

2026-10-18 591 → 2026-10-22 591（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0eba6b122f0f` · [字段定义](../../DATASET.md)*
