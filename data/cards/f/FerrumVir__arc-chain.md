# FerrumVir/arc-chain

⭐ 23 · Rust · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/FerrumVir/arc-chain) · [官网](https://arc.ai) · 个人维护

**Rust L1 区块链：多节点共识验证可复现的链上 AI 推理**

用 Rust 实现的 Layer 1 区块链候选版本，目标是将 AI 推理做成可复现、可被验证者独立重算并通过共识比对 32 字节承诺的结果。生产 CPU 引擎使用整数算术（I8/I16），在 ARM/x86 上有 KAT 测试，GPU 与完整 7B GGUF 路径尚未覆盖。worker 目标模型为 Llama-2-7B Q4_K_M（约 4GB），奖励需五/六多重授权与 2-of-3 范围仲裁。源码冻结快照显示公共种子网络存在区块/状态分歧且未部署该候选版本；交易采用 ML-DSA-65 与 Falcon-512 后量子签名，并附带 Circle STARK zkML 电路实验。面向节点运营者与开发者，提供 CLI 二进制与桌面安装包计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 验证者重算推理并比对 32 字节承诺的共识路径
- CPU I8/I16 整数算术引擎在 ARM/x86 上的整模型与三分片 KAT
- ML-DSA-65 / Falcon-512 后量子交易签名与 falcon512_verify 预编译 0x08
- 证明 Llama-2-7B 稠密层的 Circle STARK AIR 电路及拒绝伪造输出的测试

## 适用场景

- 以 SSH 服务器运行社区节点参与推理与奖励流程
- 在链上提交并验证可复现的 AI 推理结果
- 研究后量子签名与确定性推理验证的结合

## 场景标签

 · 领域:区块链/可验证 AI 推理

## 证据(README 行号)

> L87: ARC's release candidate makes inference reproducible enough for validators to
> L104: Five things, in one runtime. Every row is checkable, and the commands are in
> L70: |What should a worker run?|A router needs no model or GPU. The current full-worker target is Llama-2-7B Q4_K_M (abo

## 星数曲线

```mermaid
xychart-beta
    title "FerrumVir/arc-chain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `55cefcce590b` · [字段定义](../../DATASET.md)*
