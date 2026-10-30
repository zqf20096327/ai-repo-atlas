# AI-NAtive-I/agent-ros-bridge

⭐ 21 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/AI-NAtive-I/agent-ros-bridge) · 个人维护 · 中文 README

**AI agent 控制机器人的 ROS1/ROS2 安全网关**

面向机器人与具身智能系统的通用 ROS1/ROS2 桥接网关，让 AI agent 通过 WebSocket/gRPC/MQTT/TCP 四种协议控制移动机器人、无人机、机械臂和人形机器人。核心机制是安全层：默认强制人在回路、影子模式记录 AI 提议与人类决策、1 万场景仿真测试（95.93% 成功率）、渐进放权与紧急停止。支持多 LLM（OpenAI/Moonshot/Anthropic）、意图解析与多语言，提供 Web 仪表盘与 Docker 部署。限制：影子模式数据与 ISO 10218 审查仍在进行中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- WebSocket/gRPC/MQTT/TCP 四协议网关，支持 ROS1 与 ROS2
- 安全层：默认人工审批、影子模式、渐进放权、紧急停止
- 1 万场景仿真测试，宣称 95.93% 成功率
- Web 仪表盘：机器人控制、遥测、影子模式指标与多机管理

## 适用场景

- 让 LLM agent 安全控制 ROS 机器人执行导航、抓取等任务
- 在部署 AI 控制前用影子模式收集 AI 与人类决策对比数据
- 多机器人编队的监控与管理

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L107: AI Agents ─┬─ WebSocket ─┐
> L118: |**Safety Layer**|Validation & enforcement|✅ Implemented|
> L146: - **Multi-LLM** - OpenAI, Moonshot, Anthropic

## 星数曲线

```mermaid
xychart-beta
    title "AI-NAtive-I/agent-ros-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `810e496308ca` · [字段定义](../../DATASET.md)*
