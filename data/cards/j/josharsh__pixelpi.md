# josharsh/pixelpi

⭐ 19 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/josharsh/pixelpi) · [官网](https://www.npmjs.com/package/pixelpi) · 个人维护

**面向 agent 的轻量浏览器工具：6 个原语，低 token 占用，可录播回放**

为 AI agent 提供浏览器的 harness：以 6 个工具原语（look/act/fill/nav/eval/store）暴露页面，工具定义共 1,196 tokens，页面表示基于无障碍树与扁平引用。支持以 MCP server 接入 Claude Code/Cursor，或经 CLI 驱动，任意模型与任意 provider 均可。内置域名围栏、dry-run/confirm 门、token 预算等护栏；任务可录制成 trace，之后无模型回放、按 CSV 数据集并行执行并支持漂移自修复（--heal）。基于原生 CDP，不依赖 Playwright。

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

- 6 个工具原语，工具定义 1,196 tokens，页面 2,100–4,900 tokens（bench 脚本可复现）
- 一行配置作为 MCP server 接入 Claude Code / Cursor，无需 API key
- trace 录制后可 0 token 回放、按 CSV 并行 fan-out，--heal 漂移自修复
- 护栏置于 harness 内：域名围栏、dry-run/confirm、fail-closed BLOCKED

## 适用场景

- 给已挂多个 MCP server 的 agent 配一个省上下文的浏览器
- 录制一次任务后批量执行表单提交、抓取、价格/库存检查
- 夜间定时门户导出等重复流程的无模型回放
- 另一段程序通过 SDK 与 --json NDJSON 契约驱动浏览器操作

## 场景标签

`浏览器自动化` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L22: It's a browser for agents that have other things to do with their context window. Drop it into Claude Code or Curso
> L31: - **An MCP server in one line of config.** `npx -y pixelpi@latest mcp`, and your existing Claude Code or Cursor sub
> L48: ## Use it as an MCP server

## 星数曲线

```mermaid
xychart-beta
    title "josharsh/pixelpi 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `27bd765bc5a6` · [字段定义](../../DATASET.md)*
