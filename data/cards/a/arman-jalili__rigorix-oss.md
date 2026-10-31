# arman-jalili/rigorix-oss

⭐ 18 · Rust · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/arman-jalili/rigorix-oss) · [官网](https://rigorix.eu) · 个人维护

**AI coding agent 的确定性执行边界：计划审批与审计**

Rust 实现的 agent 执行治理层：将意图编译为可审查的执行计划，在派发时执行预算/风险门控、绑定意图的单次审批（HMAC 校验，失配即 HALT）、有序步骤序列规则与派发前置条件检查，并将决策记录到分层的防篡改审计链（本地缓存 + 外部锚定账本）。执行路径不含 LLM；Claude Code、Cursor、Copilot、Aider、Codex 等编码 agent 通过 MCP 运行于其内。面向安全、平台与风险团队；明确声明非工作流引擎、非领域系统，验证器以 crates.io/npm/PyPI 开源发布。

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

- 审批绑定意图：HMAC-SHA256 单次限时记录，派发前重推导失配即 HALT
- 有序步骤序列规则与派发前置条件，检测组合性越权（plan-time + 运行时前缀门控）
- 三层审计证据（账本/投影/缓存），导出凭据经再推导核验而非信任签名
- 执行路径无 LLM；预算按执行计数并在每次工具调用前评估

## 适用场景

- 对会执行支付、迁移或改代码的 agent 施加派发级控制
- 要求人工审批绑定具体意图并留下可审计证据
- 拦截单个合规但组合起来越权的操作序列
- 以离线开源验证器向审计方证明 agent 实际做了什么

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L13: Rigorix is the deterministic execution boundary underneath your agents: it
> L25: chat with, and it is not a faster autocomplete: `Claude Code`, `Cursor`,
> L59: The LLM decides *what to generate*. The plan — not the model — decides *what is

## 星数曲线

```mermaid
xychart-beta
    title "arman-jalili/rigorix-oss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6760a00bcc63` · [字段定义](../../DATASET.md)*
