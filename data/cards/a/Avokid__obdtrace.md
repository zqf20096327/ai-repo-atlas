# Avokid/obdtrace

⭐ 3 · Rust · MIT · 推送 2026-11-24 · [GitHub](https://github.com/Avokid/obdtrace) · 个人维护

**面向车主与 AI agent 的本地 OBD-II 读取与会话记录工具**

单二进制 Rust 程序，读取 ELM327 兼容适配器（BLE/SPP 串行/TCP）的故障码、冻结帧、就绪状态与实时传感器数据，持续写入本地 SQLite 会话历史并可导出。通过内置 stdio MCP server 向任意 MCP 客户端提供诊断与历史查询工具，支持只读环境变量与清码人工确认机制；无 AI 服务与云端调用，浏览器 UI 支持 6 种语言。当前首个二进制发布仅覆盖 Linux x86-64，Windows/macOS 构建仅在 CI 测试未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 MCP server，提供诊断与历史查询工具（JSON 时间序列、桶状摘要、多传感器对齐表）
- 持续记录实时 PID 与 DTC 事件到本地 SQLite，可浏览导出
- OBDTRACE_READ_ONLY=1 限只读，清码需显式开启并人工确认
- 单 Rust 二进制 + 浏览器 UI，本地运行，MIT 许可

## 适用场景

- 连接 ELM327 适配器记录车辆实时传感器数据与故障码
- 让 MCP 客户端中的 AI agent 查询历史会话并比较维修前后行为
- 在无 AI 客户端的情况下本地浏览车辆诊断历史

## 场景标签

 · 领域:车辆诊断/IoT 工具

## 证据(README 行号)

> L6: history and exposes it all over MCP, so an AI agent can read the car, query
> L12: - **Agent-ready:** an MCP server with diagnostic and history tools (compact
> L17: - **Local first:** one Rust binary with a browser UI. It works without an AI


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `c1ed533a43a3` · [字段定义](../../DATASET.md)*
