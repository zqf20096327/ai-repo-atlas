# muaaz9329/cheap-ag

⭐ 189 · TypeScript · MIT · 推送 2026-10-31 · [GitHub](https://github.com/muaaz9329/cheap-ag) · [官网](https://cheapag.com) · 个人维护

**Claude Code 插件：让廉价模型代写代码以减少 Opus 用量**

面向 Claude Code 用户的 MCP 服务器/插件：Opus 负责规划任务，廉价模型（经 OpenRouter/DeepSeek 等提供，约半美分每任务）在项目的私有 git worktree 副本中写代码，必须先写失败测试再修复使其通过，工具自行运行测试，仅通过的工作以未提交方式落地，Opus 读取简短结果汇报。README 给出 SWE-bench Verified 上的对比数据（Opus token 减少约 55-63%），并说明限制：最难的 bug 上解决数低于纯 Opus，微小任务无节省。需要 Claude Code、Node.js 20+ 与一家提供商的 API key；macOS/Linux 支持，Windows 为 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 廉价模型在 git worktree 副本中工作，测试通过才落地且不自动提交
- 支持 OpenRouter/DeepSeek/OpenCode Go/Command Code 四类提供商
- 提供 /cheapag:allow、status、hook on、clean 四个命令与 cheapag.json 配置
- README 公开 SWE-bench Verified 测试数据与失败案例

## 适用场景

- 让 $20/$100 Claude 订阅计划覆盖更多编码任务
- 把日常功能与修复类任务交给廉价模型执行以省 token
- 通过测试门槛约束廉价模型产出并保留 diff 审查

## 场景标签

 · 领域:开发工具/AI 编程代理

## 证据(README 行号)

> L26: **Cheap Agent fixes the org chart.** Opus plans and decides. A model that costs half a cent per task does the typin
> L6:  For Claude Code
> L110: - **Every change is proven.** The cheap model must write a test that fails before its fix and passes after. Cheap 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 high · 依据 README sha `e1bb717911f9` · [字段定义](../../DATASET.md)*
