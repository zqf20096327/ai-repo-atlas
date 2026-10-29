# Aetheris-Labs/Aegis

⭐ 24 · TypeScript · MIT · 推送 2026-06-22 · [GitHub](https://github.com/Aetheris-Labs/Aegis) · 组织维护

**基于 TEE 密钥托管的 Solana 自动交易 agent**

以 TypeScript 编写、基于 Claude Agent SDK 的 Solana 自动交易 agent：决策循环运行于可信执行环境（Intel TDX / AMD SEV-SNP / 软件模式），Ed25519 签名密钥在 enclave 内生成并用 AES-256-GCM 封存；每笔交易生成远程证明 quote 并写入 JSONL 审计日志，出站连接使用 RA-TLS。通过 MCP 工具接入 Helius、Meteora、Drift、Jupiter 等数据源。内置风险引擎（回撤熔断、置信度门槛、>$500 人工审批），默认纸面交易。需配置 ANTHROPIC_API_KEY 等 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 决策循环运行于 TEE，密钥在 enclave 内生成并封存，宿主机与运营者不可读取
- 每笔交易生成可外部验证的远程证明 quote（TDX RTMR / SEV-SNP VCEK 链）
- MCP 工具面接入 Helius/Meteora/Drift/Jupiter 行情与交易数据
- 风险引擎：全局回撤 -15% 暂停、置信度 ≥0.65、>$500 交易需人工审批

## 适用场景

- 在 TEE 中运行 Solana 自动交易，私钥不出 enclave
- 对外提供可验证的交易执行证明与审计日志
- 通过 MCP 数据源与置信度门槛控制交易决策

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: **Autonomous Solana trading agent with in-enclave key custody and attested execution.**
> L13: `Aegis` runs its entire decision loop inside a **Trusted Execution Environment**.
> L62:     B --> C{Claude Agent SDK\nReasoning Loop}

## 星数曲线

```mermaid
xychart-beta
    title "Aetheris-Labs/Aegis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `96fc873187ec` · [字段定义](../../DATASET.md)*
