# x1zzdev/Xazz

⭐ 20 · Rust · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/x1zzdev/Xazz) · 个人维护 · 中文 README

**Rust 编写的 AI 管线治理 DSL：编译期类型安全与安全护栏**

面向需要管线级治理的 AI 开发者：以单一 .xzz 脚本覆盖从 CSV 到模型训练的全流程。解析器、静态类型检查、Typed IR 与 DL 编译均用 Rust 从零实现；后端执行用 Polars 做预处理、Burn 做深度学习训练，Arrow 缓冲直通张量。内建策略即代码护栏（PII/密钥暴露检查）、差分隐私预算与 SHA-256 审计日志，错误在编译期以 line:col 报告。提供 CLI、Visual IDE 与 REST API；GPU/ONNX 为可选 Cargo feature，进程隔离为子进程超时而非 OS 沙箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编译期 null/类型安全（Option<T>），错误以 line:col 诊断输出
- 策略即代码护栏 + 差分隐私（Laplace, epsilon 预算）+ SHA-256 审计日志
- Polars 预处理与 Burn 训练统一在一个 .xzz 脚本，Arrow 缓冲直通张量
- 提供预编译二进制、源码构建与 Docker Compose 本地 IDE 演示三种途径

## 适用场景

- 在带类型/空值检查的单脚本中完成数据预处理到模型训练
- 对管线施加 PII/密钥暴露与差分隐私预算的静态治理
- 生成带 SHA-256 代码哈希的运行审计记录以满足合规要求

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L12: **A Rust-based AI pipeline governance layer — safe fine-tuning data preparation, inference gates, and static securi
> L41: Xazz is not a wrapper around existing libraries. The parser, AST, static type checker, typed IR, lowering, and DL c
> L169: Xazz workspace stack: developer surface (Visual IDE, CLI, REST API) → toolchain (xazz-core, xazz-compiler, xazz-ex

## 星数曲线

```mermaid
xychart-beta
    title "x1zzdev/Xazz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `47044dec29ee` · [字段定义](../../DATASET.md)*
