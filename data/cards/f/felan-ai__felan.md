# felan-ai/felan

⭐ 19 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/felan-ai/felan) · 组织维护

**面向开发者的本地终端编程 Agent，注重成本与可验证任务**

开源、可跨模型选用的终端编程 Agent（npm 包 @felan-ai/felan），以任务正确性为约束、API 等效成本为优化目标。提供模型路由（Prewalk 从强规划模型切换到实现模型）、渐进式嵌套上下文、RTK 命令重写与工具输出压缩、依赖感知任务图、异步子代理、本地 Markdown 项目记忆、受限网页/MCP 访问等扩展。基准测试报告各扩展在质量门通过前提下的成本下降。本地运行需 Node.js 22.19+，以用户文件系统与进程权限运行，非沙箱；另有同核心的 Felan 云托管平台。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Prewalk 同会话内从规划模型切换到实现模型的路由机制
- 渐进式嵌套 AGENTS.md/CLAUDE.md 上下文与受限子代理
- RTK 命令重写与工具输出压缩，保留失败信息与完整 JSON
- `/savings`、`felan savings` 报告各优化项的 API 等效节省估算

## 适用场景

- 在终端用自然语言指派代码检查、修改等软件工程任务
- 通过模型路由与输出压缩控制 AI 编程的 API 成本
- 用任务图和异步子代理拆解并跟踪多步骤开发工作

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L4:  An open-source, model-portable coding agent built for cost-efficient,
> L13: Felan Code is built around one rule: an optimization only counts when the task still
> L62: Connect a provider inside the TUI with `/login`, then start working:

## 星数曲线

```mermaid
xychart-beta
    title "felan-ai/felan 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6b198c89df42` · [字段定义](../../DATASET.md)*
