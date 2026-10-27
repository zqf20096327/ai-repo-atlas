# ashaychangwani/imprint

⭐ 24 · TypeScript · MIT · 推送 2026-10-14 · [GitHub](https://github.com/ashaychangwani/imprint) · [官网](https://github.com/ashaychangwani/imprint) · 个人维护

**录制浏览器操作一次，编译成 AI agent 可调用的确定性 MCP 工具**

面向开发 MCP 工具链的命令行工具：用 `imprint teach` 录制一次真实浏览器会话，记录网络请求与 DOM 交互，由多 agent 编译流水线逆向 API 工作流并生成类型化 MCP 工具，供 Claude Code/Claude Desktop/Codex 等 MCP 客户端调用；DOM playbook 作为兜底路径。运行时零 token，录制即执行体。支持 `imprint install` 注册、`refine` 隔离环境修复工具、`audit --strict` 严格审计。限制：自动 PII/token 脱敏默认关闭，录制文件不宜公开分享。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 录制一次浏览器会话即编译为确定性 MCP 工具，运行时零 token
- 多 agent 流水线（master/planner/compiler）逆向 API 工作流并逐工具验证
- `imprint install` 支持 claude-desktop/claude-code/codex/openclaw/hermes 等平台注册
- `imprint refine` 隔离修复与 `imprint audit --strict` 严格审计

## 适用场景

- 为 AI agent 教会某个网站的固定工作流并生成可复用工具
- 避免 agent 在网站上反复探索消耗 token 或点错按钮
- 将录制的航班/酒店查询等流程作为 MCP server 接入 Claude 类客户端

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L24: A browser opens. You drive the workflows and narrate what you're doing. Imprint records every request and interacti
> L72:  3. Use
> L73:  A typed MCP tool your agent calls like any other tool. Works with Claude Code, Codex, Claude Desktop, and any MCP 

## 星数曲线

```mermaid
xychart-beta
    title "ashaychangwani/imprint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cd9cb7e675b7` · [字段定义](../../DATASET.md)*
