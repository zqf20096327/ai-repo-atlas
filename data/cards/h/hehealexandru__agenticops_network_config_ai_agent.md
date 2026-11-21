# hehealexandru/agenticops_network_config_ai_agent

⭐ 3 · Python · AGPL-3.0 · 推送 2026-11-05 · [GitHub](https://github.com/hehealexandru/agenticops_network_config_ai_agent) · 个人维护

**面向 GNS3 实验室的 AI 网络配置 Agent：自然语言驱动设备配置**

该工具通过 GNS3 REST API 读取实验拓扑，自动分类路由器、交换机、终端等节点，经由 GNS3 控制台完成零接触 SSH 初始化，再基于 Netmiko 通过 SSH/Telnet 下发配置，覆盖 IP 分配、OSPF/EIGRP/RIPv2/静态路由、ACL、VLAN、Docker 容器配置等任务。每项配置变更需人工确认后执行；发送给 LLM 的内容默认掩码密钥类信息；支持多个 OpenAI 兼容 LLM 提供商按优先级列表自动故障切换；以 Docker 容器交付，也可用 Python 3.12 本地运行；依赖本机已运行的 GNS3 2.2+（localhost:3080）与 docker-ce。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取任意 GNS3 拓扑并自动分类设备类型（Dynamips/IOU/QEMU、交换机、VPCS 等）
- 零接触 SSH 初始化：等待 IOS 启动、跳过初始配置对话、验证 SSH v2 并返回管理 IP
- 多提供商 LLM 回退：按优先级列表在限流/故障时自动切换 OpenAI 兼容 API
- 人工审批与密钥掩码：每项变更确认后执行，发送到 LLM 的内容默认脱敏

## 适用场景

- 在 GNS3 实验中用自然语言让 Agent 自动完成路由、ACL、VLAN 配置
- 为整个网络实验生成 Markdown 格式文档并备份运行配置
- 排查实验网络连通性问题

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L16: - **Automatic topology discovery** — reads any GNS3 topology via REST API (localhost:3080)
> L28: - **Multi-provider LLM fallback** — NVIDIA NIM, Mistral, OpenRouter or any OpenAI-compatible API, with automatic fa
> L29: - **Human approval** — every configuration change is shown in full and runs only after you confirm it (`y` / `n` / 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `95c52867d95d` · [字段定义](../../DATASET.md)*
