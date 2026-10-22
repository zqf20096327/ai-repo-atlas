# OTT-Cybersecurity-LLC/lyrie-ai

⭐ 327 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/OTT-Cybersecurity-LLC/lyrie-ai) · [官网](https://lyrie.ai) · 组织维护

**自主 AI 网络安全 agent：自动渗透测试与 LLM 红队**

由 OTT Cybersecurity LLC 构建的自主安全 agent，提供 25 个 CLI 命令：7 阶段自主渗透测试（lyrie hack）、URL/代码漏洞扫描、对 LLM 端点的 5 种红队攻击策略（crescendo/TAP/PAIR/GCG/AutoDAN）、静态二进制分析（Omega），以及持续威胁监测守护进程。附 Agent Trust Protocol（ATP）——基于 Ed25519 签名的 AI agent 身份开放密码学标准，含证书签发/验证 SDK。双语言安装：Python 包 lyrie-omega（pip）与 TypeScript 包 @lyrie/atp（npm），GCG/AutoDAN 完整模式需 GPU（GCG 需 H200）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 阶段自主渗透测试管线，输出 SARIF 供 GitHub Code Scanning
- LLM 端点红队：crescendo/TAP/PAIR/GCG/AutoDAN 5 种攻击策略
- Agent Trust Protocol：Ed25519 签名的 AI agent 身份标准（npm SDK）
- 守护进程持续威胁检测、自改进（lyrie evolve）与治理合规（NIST AI RMF）

## 适用场景

- 对 Web 应用或本地源码做自动化渗透测试
- 红队测试自家的 LLM 端点抗攻击能力
- 为 AI agent 签发与验证加密身份证书
- 持续监测部署目标的威胁与安全配置

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L36: Lyrie is an autonomous security agent built by OTT Cybersecurity LLC. It runs end-to-end pentests, red-teams LLM en
> L79: lyrie redteam <endpoint>         # AI red-team an LLM endpoint

## 星数曲线

```mermaid
xychart-beta
    title "OTT-Cybersecurity-LLC/lyrie-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 325 --> 328
    line [326, 327, 327]
```

2026-10-18 326 → 2026-10-22 327（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b2bc129ffa71` · [字段定义](../../DATASET.md)*
