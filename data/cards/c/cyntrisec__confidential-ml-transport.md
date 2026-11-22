# cyntrisec/confidential-ml-transport

⭐ 10 · Rust · Apache-2.0 · 推送 2026-11-19 · [GitHub](https://github.com/cyntrisec/confidential-ml-transport) · 个人维护

**为机密推理提供证明绑定加密张量传输的 Rust 库**

Rust 库，在 TEE enclave 与客户端之间提供二进制分帧的加密通信：13 字节帧头线协议、X25519+ChaCha20Poly1305 AEAD 加密、3 消息证明握手，会话密钥由证明文档派生以绑定 TEE 身份。支持张量帧（dtype/shape 子头）、重放防护、测量寄存器校验、指数退避重试与透明代理（免改代码包裹既有 TCP 服务）。传输与证明均可插拔：TCP/VSock 后端，mock/Nitro/SEV-SNP/Azure/TDX 证明实现，通过 feature flag 启用。当前处于开发阶段，作者声明未达生产就绪。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 3 消息证明握手，会话密钥由证明文档经 HKDF-SHA256 派生
- 张量帧支持 F32/F64/F16/BF16/I32/I64/U8/U32，8 字节对齐
- 透明代理可在不改代码的情况下加密既有 TCP 服务
- 支持 AWS Nitro/AMD SEV-SNP/Azure CVM/Intel TDX 多平台证明实现

## 适用场景

- 在 TEE enclave 内运行推理时加密传输模型激活张量
- 为现有明文 TCP 服务加装传输加密而不修改服务代码
- 在机密 AI 推理管线中校验 enclave 测量值后再传数据

## 场景标签

 · 领域:安全基础设施/机密计算

## 证据(README 行号)

> L8: Attestation-bound encrypted tensor transport for confidential ML inference over VSock and TCP.
> L48: `confidential-ml-transport` is a Rust library that provides secure, binary-framed communication between TEE (Truste
> L57: - **Pluggable attestation** — trait-based attestation provider/verifier, with mock, Nitro, SEV-SNP, Azure SEV-SNP, 

## 星数曲线

```mermaid
xychart-beta
    title "cyntrisec/confidential-ml-transport 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `dbb733984a78` · [字段定义](../../DATASET.md)*
