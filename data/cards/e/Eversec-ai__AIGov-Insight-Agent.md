# Eversec-ai/AIGov-Insight-Agent

⭐ 10 · 推送 2026-04-22 · [GitHub](https://github.com/Eversec-ai/AIGov-Insight-Agent) · [官网](http://insight.aigovian.com/) · 组织维护 · 中文 README

**面向 AI 智能体运维/安全团队的 eBPF 全链路可观测探针**

基于 eBPF 的探针程序，用于观测 AI 智能体与 LLM 应用的行为：通过 TC 挂载监控网络流量（支持 Dify Agent、Workflow、MCP、vLLM、Ollama、OpenClaw 协议解析），通过 uprobe 监控 ROS2 机器人节点通信与 HTTPS 加密流量明文，另可监控敏感文件访问与进程执行并按风险等级过滤。以 DEB 安装包形式分发，通过 ai-sec-ctl 交互式向导配置监控模式、端口与部署方向，日志写入本地目录供聚合。要求 Ubuntu 22.04、x86_64、内核 ≥5.4。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TC eBPF 流量监控并解析 Dify/MCP/vLLM/Ollama/OpenClaw 协议
- uprobe 监控 ROS2 机器人节点通信（话题、消息、节点名）
- HTTPS 加密流量解密观测与 LLM 请求/响应自动解析
- 敏感文件访问与进程执行的监控与风险等级过滤

## 适用场景

- 为部署的 AI 智能体应用采集会话、工具调用与 Token 统计数据
- 监控企业内 LLM 服务的流量并关联请求/响应日志
- 观测机器人系统中 ROS2 节点间通信
- 审计智能体对敏感文件的访问与命令执行行为

## 场景标签

`LLM 可观测性` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L5: 基于 eBPF 技术的 AI 智能体全链路可观测探针，用于观测 AI 智能体和 LLM 应用的网络流量、ROS2 通信以及系统指令执行、系统文件访问等行为。AIGov-Insight Web 与 AIGov-Insight Agen
> L31: 通过 TC (Traffic Control) eBPF 程序监控 AI 智能体/LLM/MCP/RAG/OpenClaw 等应用流量。
> L438: |**基于 eBPF**|内核态监控，无需修改应用程序|

## 星数曲线

```mermaid
xychart-beta
    title "Eversec-ai/AIGov-Insight-Agent 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `f7a130dafe62` · [字段定义](../../DATASET.md)*
