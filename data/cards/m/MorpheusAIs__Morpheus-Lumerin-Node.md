# MorpheusAIs/Morpheus-Lumerin-Node

⭐ 24 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/MorpheusAIs/Morpheus-Lumerin-Node) · [官网](https://mor.org) · 组织维护

**接入 Morpheus 去中心化 LLM 网络的桌面聊天客户端与代理路由节点**

面向 Morpheus 网络（BASE 链）的节点软件：proxy-router 后台进程监听区块链合约事件，在消费者与提供者之间建立会话并路由提示词与推理请求；提供 Electron 桌面聊天应用（MorpheusUI）、CLI 客户端与 headless 路由二进制。桌面应用首次启动时下载 proxy-router、本地 llama.cpp+tinyllama 演示模型和 IPFS 节点。v7 引入两跳 TEE 信任链（Intel TDX、NVIDIA NRAS GPU 远程证明）。使用需质押 MOR 代币并支付 BASE 链 gas。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- proxy-router 监听链上事件并在消费者/提供者间路由推理
- Electron 桌面聊天应用（dmg/AppImage/exe 安装包）
- v7 两跳 TEE 信任链：Intel TDX SecretVM 与 GPU 远程证明
- CLI 与 headless 路由二进制支持提供者部署

## 适用场景

- 作为消费者通过桌面聊天界面使用 Morpheus 网络上的分布式模型
- 作为提供者在链上注册并托管自己的模型
- 以 headless 方式部署代理路由节点

## 场景标签

`聊天机器人` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: The purpose of this software is to enable interaction with distributed, decentralized LLMs on the Morpheus network t
> L22: - Lumerin `proxy-router` — background process that monitors blockchain contract events, manages secure sessions bet
> L23: - `ui-desktop/` (**MorpheusUI**) — Electron desktop app for consumers. Release assets are `*-morpheus-app-*` instal

## 星数曲线

```mermaid
xychart-beta
    title "MorpheusAIs/Morpheus-Lumerin-Node 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7441d207c24f` · [字段定义](../../DATASET.md)*
