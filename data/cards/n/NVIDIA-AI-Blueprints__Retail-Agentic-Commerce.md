# NVIDIA-AI-Blueprints/Retail-Agentic-Commerce

⭐ 82 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/NVIDIA-AI-Blueprints/Retail-Agentic-Commerce) · 组织维护

**NVIDIA 参考实现：ACP/UCP 协议下的商家可控 AI 结账与支付**

NVIDIA AI Blueprints 出品的 Agentic Commerce Protocol（ACP）与 Universal Commerce Protocol（UCP）参考实现，面向零售商务场景的代理化结账、支付与编排。包含 Merchant API（ACP+UCP 发现/A2A）、PSP 委托支付服务、Apps SDK MCP 服务器与小组件、促销/推荐/搜索/售后 NAT 代理，以及带协议面板的演示 UI。默认部署走 NVIDIA 公共 API 端点，无需 GPU；可选本地 NIM 自托管推理（Nemotron LLM 与嵌入模型）最低需 2× A100 80GB。通过 Docker Compose 或 install.sh 启动 8 个服务，也可在 Codex/Claude Code 中运行 /setup。

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

- Merchant API 提供 ACP + UCP 发现与 A2A 能力
- 含 PSP 委托支付流、Apps SDK MCP 服务器与小组件
- 促销/推荐/搜索/售后消息四类 NAT 代理
- 默认用 NVIDIA 公共端点无需 GPU，可选本地 NIM 部署（Nemotron LLM + 嵌入模型）

## 适用场景

- 零售商搭建代理化结账与支付的参考架构
- 验证 ACP/UCP 协议下的商家可控交易流程
- 作为 MCP/A2A 电商代理编排的二次开发起点

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: A reference implementation of the Agentic Commerce Protocol (ACP) and Universal Commerce Protocol (UCP), built for m
> L17: - Merchant API (ACP + UCP discovery/A2A)
> L19: - Apps SDK MCP server + widget

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA-AI-Blueprints/Retail-Agentic-Commerce 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-27 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0b0e7298cd75` · [字段定义](../../DATASET.md)*
