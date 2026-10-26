# node9-ai/node9-proxy

⭐ 219 · TypeScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/node9-ai/node9-proxy) · [官网](https://node9.ai/) · 组织维护

**AI 编码代理的访问控制网关：审批危险操作并留痕**

面向使用 Claude Code、Codex CLI、Cursor 等 12 种编码代理及任意 MCP 服务器的开发者与团队。node9 以 hook 形式运行在代理与工具调用之间：默认封禁 ~/.ssh、~/.aws、.env 等凭证读取，拦截破坏性 git、无 WHERE 的 SQL、curl|bash 等命令并等待人工批准；命令按 shell AST 解析而非文本匹配。提供 MCP 网关、出站白名单、沙箱、姿态评分、仓库扫描与 Canary 凭证等功能，可通过 npm 或 brew 安装，也可作为 MCP 服务器运行。另有 Pro 版提供 SSO 与中央审计导出。

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

- 默认凭证牢笼封禁 ~/.ssh、~/.aws、.env 与私钥读取
- 命令按 shell AST 解析，绕过包装仍判定为敏感读取
- 支持 12 种代理与任意 MCP 服务器的统一策略与审计记录
- MCP 工具定义固定（pinning）与 SHA-256 技能校验

## 适用场景

- 在 AI 代理执行删除文件或危险 SQL 前要求我批准
- 防止被劫持的代理读取 SSH 密钥与云凭证
- 团队通过共享仪表盘统一策略并审批挂起操作

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L2:  Access control for AI agents
> L91: files. node9's gate is not one of those flags: it runs in the hook, and an action it holds stays
> L96: node9 sits between the agent and every tool it calls. The credential jail (`~/.ssh`, `~/.aws`,

## 星数曲线

```mermaid
xychart-beta
    title "node9-ai/node9-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 218 --> 220
    line [219, 219]
```

2026-10-18 219 → 2026-10-26 219（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c0cc61949618` · [字段定义](../../DATASET.md)*
