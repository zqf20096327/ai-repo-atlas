# censgate/redact

⭐ 23 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/censgate/redact) · [官网](https://censgate.com) · 组织维护

**Rust 实现的 PII/密钥检测与脱敏引擎，含网关与证据链**

单一 Rust 引擎提供四类交付形态：CLI（61 种编译内置实体类型，确定性模式匹配，默认不用 NER、不联网）、只读 Postgres PII 扫描器（仅输出位置与计数，样本值不离机）、OpenAI 兼容网关（发往模型提供商前脱敏提示词）、WASM 与 redact-core 嵌入库。配套 redact-verify 做离线第三方验证：哈希链、Merkle+Rekor 锚定、Ed25519 签名检查。README 明确声明合规 YAML 非认证、基准 32× 仅为延迟测量非质量分。面向需在 CI、数据库与 LLM 流量中管控敏感信息的团队。

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

- 61 种内置实体类型的确定性模式引擎，默认无 NER、无网络
- OpenAI 兼容网关在提示词发往提供商前脱敏
- 哈希链 + Rekor 锚定的证据包可由第三方离线验证（redact-verify）
- 只读 Postgres PII 扫描，样本值不离机

## 适用场景

- CI 与 pre-commit 中拦截密钥与 PII 泄漏
- 盘点 Postgres 数据库中 PII 分布作为 GDPR Art. 30 输入
- LLM 网关出口脱敏并生成可审计证据包

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: For teams that gate secrets in CI, inventory PII in Postgres, or send prompts
> L24: - **Prove what left** — gateway + ledger + `redact-verify`. The gateway is the delivery mechanism. The evidence pac
> L101: The gateway redacts prompts on the way to a provider. The ledger pack is what

## 星数曲线

```mermaid
xychart-beta
    title "censgate/redact 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-27 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `58b369d07b6b` · [字段定义](../../DATASET.md)*
