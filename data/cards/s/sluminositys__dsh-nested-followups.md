# sluminositys/dsh-nested-followups

⭐ 49 · TypeScript · MIT · 推送 2026-09-30 · [GitHub](https://github.com/sluminositys/dsh-nested-followups) · 个人维护 · 中文 README

**DeepSeek Harness 插件：任意回答处递归分叉追问且不污染主任务**

面向 DeepSeek Harness（DSH）0.1.x 的 Web profile 插件：在 Tree View 中从任意已完成的助手回答发起隔离追问分支，每个分支是真实的 DSH 会话，继承且仅继承其祖先路径，可无限递归分叉，主任务历史不受影响。分支执行时工具按只读策略检查，写入与未知工具默认拒绝；请求前缀与父会话字节一致以复用提供商前缀缓存。提供树状视图、搜索、折叠与级联删除。要求 Node.js 22.19+ 与 pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 任意深度递归分叉，每层为真实隔离的 DSH 会话
- 分支仅继承祖先路径，主任务历史不含分支消息
- 分支工具执行时强制只读，写操作与未知工具默认拒绝
- 请求前缀与父会话字节兼容以复用提供商前缀缓存

## 适用场景

- 在主线任务中随时岔出侧问而不污染主对话
- 对某个回答连续多层追问并保持上下文隔离
- 在大树中搜索、折叠并级联删除分支

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: A DeepSeek Harness plugin
> L30: - **Keep the main task clean.** Nothing asked or answered in a branch flows back
> L98: - Every branch, including a branch created inside another branch, is a real

## 星数曲线

```mermaid
xychart-beta
    title "sluminositys/dsh-nested-followups 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-24 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e03704ac56d4` · [字段定义](../../DATASET.md)*
