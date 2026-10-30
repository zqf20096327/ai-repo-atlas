# axone-protocol/axoned

⭐ 177 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/axone-protocol/axoned) · [官网](https://axone.xyz) · 组织维护

**面向 AI 资源共享与编排的 Cosmos SDK 公链节点实现**

axoned 是 AXONE 网络（dPoS layer 1）的节点软件，基于 Cosmos SDK 与 CometBFT 共识构建，用 Go 编写。该网络定位为连接、共享与货币化 AI 技术栈中的各类资源（数据、算法、模型、存储、算力、API，链上或链下均可）。用户可运行节点、成为验证人（需质押 $AXONE）、通过链上规则定义资源共享策略并构建应用。支持 Darwin/Linux amd64/arm64，Windows 不支持；提供二进制发布、源码 make install 与 Docker 镜像三种安装方式，附带 SBOM 与 SLSA 签名验证。开发环境使用 Nix + direnv，可一键启动单验证人本地网络。

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

- 基于 Cosmos SDK + CometBFT 的 dPoS layer 1 节点，Go 编写
- 支持链上规则定义与链下 AI 资源（数据/模型/算力/API）共享与货币化
- 发布产物附带 SPDX SBOM 与 SLSA provenance 签名可验证
- make chain-init/chain-start 一键启动本地单验证人网络

## 适用场景

- 运行 AXONE 网络节点或成为验证人参与出块
- 在链上定义规则并共享 AI 数据、模型与算力资源
- 基于该协议构建协作式 AI 工作流应用
- 本地起测试网进行开发调试

## 场景标签

 · 领域:区块链/去中心化 AI 基础设施

## 证据(README 行号)

> L23: > `Axone` is a public dPoS layer 1 specifically designed for connecting, sharing, and monetizing any resources in t
> L27: `axoned` is the node of the AXONE network built on the [Cosmos SDK] 💫 & [CometBFT] consensus, which allows companie

## 星数曲线

```mermaid
xychart-beta
    title "axone-protocol/axoned 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 176 --> 178
    line [177, 177]
```

2026-10-18 177 → 2026-10-30 177（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `f6e8ebcf8a35` · [字段定义](../../DATASET.md)*
