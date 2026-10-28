# bkuan001/halo-record

⭐ 85 · Python · Apache-2.0 · 推送 2026-10-03 · [GitHub](https://github.com/bkuan001/halo-record) · [官网](https://pypi.org/project/halo-record/) · 个人维护

**给 AI agent 运维者：哈希链防篡改审计日志与可自验报告**

面向部署 AI agent 的团队：以零依赖的 Python 包（另有 TypeScript 包）在工具调用、模型调用、数据访问等边界处捕获动作，生成追加式哈希链 Runtime Record（JSONL），并渲染为 Runtime Report HTML 页面——读者浏览器内重算哈希链验证，也可用 halo verify 命令独立核验。记录格式开放，本包为参考实现，含 recorder、verifier、witness client 与 report server。提供 LangChain/LangGraph、MCP、OpenTelemetry GenAI、Claude Code/Codex hook、网关日志等多条接入路径。限制（LIMITS.md 自述）：链本身仅对操作者以外各方防篡改，需外部 checkpoint 才能证明记录未被删除，且不能证明全部动作均被捕获。

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

- 零运行时依赖，pip 仅安装一个包，约 8,700 行代码
- 哈希链记录 + 浏览器内重验的 Runtime Report + halo verify 独立核验
- 可选外部 witness checkpoint、RFC 3161 时间戳等四个 opt-in 网络调用
- 记录级 verification 块可封存 guardrail/policy 判定（allowed/blocked/modified/unverified）

## 适用场景

- 向客户安全团队提供可自行验证的 agent 行为报告
- 满足 ISO 42001、EU AI Act 记录保留类的审计合规要求
- 对 Claude Code / Codex 等编码 agent 的每次工具调用留痕

## 场景标签

`网络安全` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: Tamper-evident **audit trails for AI agents** — hash-chained Runtime Records, rendered as a Runtime Report your cust
> L9: The record format is open and free to implement. This package is the reference implementation: recorder, verifier, w
> L122: |Native recorder (`from halo_record import trace`)|OpenTelemetry GenAI spans|

## 星数曲线

```mermaid
xychart-beta
    title "bkuan001/halo-record 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 83 --> 86
    line [84, 85, 85]
```

2026-10-18 84 → 2026-10-28 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0554b7eb39ae` · [字段定义](../../DATASET.md)*
