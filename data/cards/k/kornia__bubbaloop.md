# kornia/bubbaloop

⭐ 30 · Rust · Apache-2.0 · 推送 2026-06-26 · [GitHub](https://github.com/kornia/bubbaloop) · [官网](https://www.kornia.org/bubbaloop/) · 组织维护

**硬件 AI agent：单 Rust 二进制管理摄像头/传感器/机器人车队**

以约 13 MB 的单一 Rust 二进制提供 CLI、守护进程与 MCP 服务器，用于以自然语言和 AI agent 管理摄像头、传感器、机器人与 IoT 车队。数据面基于 Zenoh 发布/订阅，节点自描述（manifest/schema/health），守护进程内置 agent 运行时：每个 agent 有身份文件与四级记忆（SQLite 世界状态、RAM、NDJSON 情景、信念库），并带 CPU/RAM/磁盘遥测看门狗。通过 47 个 MCP 工具供 Gemini/Claude/Ollama 接入，另提供 YOLO11 物体检测与 VLM 场景描述节点。限制：systemd 的 Linux 为生产支持路径，Docker/非 systemd 环境仅开发回退，服务管理命令不适用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 ~13 MB Rust 二进制：CLI + daemon + MCP 服务器（47 个 MCP 工具，3 级 RBAC）
- Zenoh 发布/订阅数据面与自描述节点契约（manifest/schema/health/config/command）
- 多 agent 运行时：四级记忆、自适应心跳、遥测看门狗与断路器
- YAML Skills 零代码接入传感器；官方节点含 YOLO11 检测与 VLM 场景描述

## 适用场景

- 用 Claude/Gemini/Ollama 等 agent 通过自然语言管理摄像头、传感器和机器人
- 在 Jetson、树莓派等 Linux 设备上组建联邦 IoT/机器人车队并实时遥测
- 为 AI agent 提供 MCP 工具层以读取摄像头帧、查询节点与发送控制命令

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L135: The daemon hosts the **agent runtime** (multi-agent Zenoh gateway) alongside the MCP server. Agents are configured

## 星数曲线

```mermaid
xychart-beta
    title "kornia/bubbaloop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-28 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e8f2c0bcf1a2` · [字段定义](../../DATASET.md)*
