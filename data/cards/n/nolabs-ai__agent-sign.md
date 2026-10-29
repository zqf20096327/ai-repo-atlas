# nolabs-ai/agent-sign

⭐ 27 · Shell · Apache-2.0 · 推送 2026-06-28 · [GitHub](https://github.com/nolabs-ai/agent-sign) · [官网](https://nono.sh) · 组织维护

**给 CI 工程师：用 Sigstore 密钥签名 AI agent 指令文件**

一个 GitHub Action（nolabs-ai/agent-sign），在 CI 中对 SKILLS.md、CLAUDE.md 等 AI agent 指令文件及 nono 包进行 Sigstore 密钥签名与发布。机制：从 GitHub Actions OIDC 身份派生签名身份，经 Fulcio 签发短期证书、写入 Rekor 透明日志，产出含 DSSE in-toto 声明的离线可验证 bundle。支持多文件联合签名或逐文件签名、发布 nono 包到 registry；运行时由 nono 沙箱在 agent 读取前强制核验。需要 id-token: write 权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 GitHub Actions OIDC 的 Sigstore 密钥签名（Fulcio 证书 + Rekor 透明日志）
- 多文件联合签名（multi-subject）或逐文件（per-file）两种 bundle 模式
- 支持发布签名后的 nono 包到 registry
- 运行时由 nono 沙箱在文件被读取前强制验证（seccomp/Seatbelt）

## 适用场景

- 在 CI 中为 agent 指令文件与配置建立加密信任链
- 发布带签名与发布者身份证明的 nono 包
- 让 agent 消费方用 trust-policy.json 验证文件来源

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L4:  Sign SKILLS.md, CLAUDE.md and related artifacts with Sigstore and Nono keyless attestation, or publish full nono pa
> L15: AI agents read instruction files to determine what they can do. If those files are tampered with, the agent follows
> L52: 1. Installs the nono CLI from GitHub releases

## 星数曲线

```mermaid
xychart-beta
    title "nolabs-ai/agent-sign 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3b31faf52a2b` · [字段定义](../../DATASET.md)*
