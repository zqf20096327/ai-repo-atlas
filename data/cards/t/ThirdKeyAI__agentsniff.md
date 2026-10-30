# ThirdKeyAI/agentsniff

⭐ 15 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/ThirdKeyAI/agentsniff) · [官网](https://docs.agentsniff.org) · 组织维护

**网络扫描器：发现并核验内网中的 AI agent 基础设施**

Rust 编写的网络扫描工具，通过主动探测（端口扫描、AgentPin/MCP/A2A 协议探测、端点探测）与被动监测（DNS、流量分析、SSE、TLS 指纹、可选 eBPF）发现网络中的 AI agent 服务，并将多检测器信号关联为确定性服务资产。身份保证采用 fail-closed 设计：仅签名核验成功才产生 trusted_verified。提供 CLI、带认证的 Web 仪表盘与 REST/SSE API，支持 SQLite/PostgreSQL 持久化与 SARIF 导出，扫描范围限 65,536 目标。限定授权网络扫描用途。

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

- 9 类检测器（DNS/端口/AgentPin/A2A/MCP/端点/TLS/流量/SSE）信号关联
- AgentPin 凭证 ES256 签名 fail-closed 核验（含撤销与委托链检查）
- 签名验签的检测特征数据集与原子更新
- CLI + 仪表盘 + REST/SSE/MCP API，SQLite/PostgreSQL 后端

## 适用场景

- 盘点内网中暴露的 AI agent、MCP 与推理服务
- 对比历次扫描，对新出现或变更的 agent 资产生成告警
- 核验 A2A Agent Card 与 AgentPin 凭证的签名身份
- 以 SARIF 格式导出扫描结果接入安全流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: AgentSniff is a Rust network scanner for discovering AI-agent infrastructure through active probing, passive monitor
> L15: |MCP detector|Version-negotiated JSON-RPC discovery and capability enumeration|No|High–Confirmed|

## 星数曲线

```mermaid
xychart-beta
    title "ThirdKeyAI/agentsniff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8e0a0b7460bf` · [字段定义](../../DATASET.md)*
