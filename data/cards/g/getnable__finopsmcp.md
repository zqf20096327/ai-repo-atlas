# getnable/finopsmcp

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/getnable/finopsmcp) · [官网](https://getnable.com) · 组织维护

**本地 FinOps 工具：在 AI 代理执行云命令前定价与拦截**

开源（Apache-2.0）的本地 FinOps 工具，以终端命令和 MCP 服务器两种形式运行在 Claude、Cursor、VS Code 内。核心机制：通过 hook 检查编码代理（Claude Code、Cursor、Codex CLI、Copilot、Gemini CLI、Cline）即将执行的云命令，按刊例价预先定价，超过阈值或不可逆操作（destroy/terminate/承诺购买）先询问人工，判定写入本地哈希链账本。另提供 AWS 只读扫描找浪费、AI 编码代理花费预算（按人/团队/组织，budgets.yaml 配置）。无需云账户或 API key 即可定价，扫描需本机已有 AWS 凭证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 代理命令执行前按刊例价定价，超阈值或单向门操作先问人工
- 判定写入本地哈希链账本，含速率上限与循环检测
- AWS 只读扫描找浪费（闲置服务器、超配数据库等），修复以 PR 形式提出
- AI 代理花费按模型定价，支持按人/团队/组织的预算与封顶

## 适用场景

- 在 Claude Code/Cursor 中拦截代理的高成本或不可逆云操作
- 扫描 AWS 账户找出浪费并按金额排序
- 为团队和个人设置 AI 编码代理的月度预算

## 场景标签

 · 领域:云成本管理/DevOps

## 证据(README 行号)

> L11: nable puts a check in front of the commands a coding agent is about to run, in Claude Code, Cursor, Codex CLI, GitH
> L13: nable is also an open-source (Apache-2.0), local-first FinOps tool for cloud and AI cost: a read-only scan that fin
> L73: `uvx nable` runs as a local MCP server inside Claude, Cursor, and VS Code, on your existing Claude or Cursor member

## 星数曲线

```mermaid
xychart-beta
    title "getnable/finopsmcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4e0c260f399f` · [字段定义](../../DATASET.md)*
