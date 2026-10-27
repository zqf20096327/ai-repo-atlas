# makerchecker/MakerChecker

⭐ 54 · TypeScript · AGPL-3.0 · 推送 2026-10-05 · [GitHub](https://github.com/makerchecker/MakerChecker) · [官网](https://makerchecker.ai) · 组织维护

**AI agent 安全网关与静态扫描器：权限管控、人工审批、可验审计**

面向 AI agent 的安全层，由三个可独立使用的包组成：`mc scan` 静态扫描 agent 代码中的高危行为（删数据、转账、执行 shell、泄露密钥）并按风险分类；`@makerchecker/embedded` 提供 deny-by-default 的角色权限管控原语，agent 只能运行被授予的技能且不能审批自己的工作；自托管服务器（Fastify + Postgres）提供人工审批收件箱、审查控制台与 Ed25519 签名、哈希链式的防篡改审计日志，可离线验证导出 bundle。提供 LangChain、Claude Agent SDK 连接器与 TS/Python SDK。客户端包为 Apache-2.0，服务器/Web 为 AGPL-3.0，另提供商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- deny-by-default RBAC 管控每次工具调用，未授权调用在执行前被拒
- Ed25519 签名 + SHA-256 哈希链审计日志，导出 bundle 可离线验证
- `mc scan` 静态扫描 agent 高危行为并可用 --fix 生成治理代码
- 人工审批门禁与职责分离：申请者不能作为自己的审批人

## 适用场景

- 对 agent 的删除数据、转账、shell 执行等高危操作加人工审批门禁
- 为合规审计提供防篡改、可独立离线验证的决策记录
- 扫描现有 agent 代码，发现未被管控的高危能力

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L14: Your agents keep running in their existing framework (LangChain, Claude SDK, CrewAI). MakerChecker sits in front of
> L30: Import the controls and wrap any tool. The agent can now only run what its role was granted — a call it isn't allow
> L100: Every decision and tool call commits to a hash-chained log — each event a SHA-256 over the RFC 8785 canonical JSON

## 星数曲线

```mermaid
xychart-beta
    title "makerchecker/MakerChecker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-27 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `70f5058ed411` · [字段定义](../../DATASET.md)*
