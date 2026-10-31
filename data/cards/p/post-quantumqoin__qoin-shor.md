# post-quantumqoin/qoin-shor

⭐ 16 · Go · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/post-quantumqoin/qoin-shor) · [官网](https://PostQuantumQoin.org) · 组织维护

**去中心化抗量子 AI 算力网络（区块链节点软件 Shor）**

qoin-shor 是一个自称“去中心化抗量子 AI 超算网络”的区块链项目，README 提供的内容限于节点软件 Shor 的构建与安装：列出 Ubuntu/Debian 与 Fedora 的系统依赖（OpenCL、hwloc、clang 等），要求 Go 1.22.2 及以上，通过 git clone、git checkout 发布标签、make clean all && sudo make install 完成编译安装，随后运行 shor daemon 同步链加入主网。README 未说明 AI 算力部分的具体机制、接口或使用方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从源码编译安装节点软件 Shor 并运行 daemon 加入主网
- 给出 Ubuntu/Debian 与 Fedora 两套系统依赖安装命令
- 要求 Go 1.22.2+ 及 OpenCL/hwloc 等系统依赖
- 声明 MIT + Apache 2.0 双许可

## 适用场景

- 搭建并运行 qoin-shor 区块链网络节点
- 参与该抗量子区块链网络的链同步

## 场景标签

 · 领域:区块链/分布式算力网络

## 证据(README 行号)

> L4: **qoin-shor** is a Decentralized Quantum-resistant AI Supercomputing Network.
> L64:    shor daemon

## 星数曲线

```mermaid
xychart-beta
    title "post-quantumqoin/qoin-shor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 low · 依据 README sha `25576f016d66` · [字段定义](../../DATASET.md)*
