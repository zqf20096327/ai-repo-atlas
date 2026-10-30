# device-context-protocol/dcp

⭐ 62 · Python · MIT · 推送 2026-05-27 · [GitHub](https://github.com/device-context-protocol/dcp) · 组织维护

**让 LLM agent 安全控制微控制器等物理设备的协议与桥接**

面向 ESP32/ESP8266 等资源受限 MCU 的意图级设备控制协议：CBOR 压缩帧（典型调用 19 字节）、编译期静态意图表、传输无关（UART/BLE/MQTT/USB-CDC/WebSocket）。安全机制集中在 Bridge 进程：能力令牌（HMAC-SHA256）、范围/类型/单位校验、dry-run 原语。参考 Bridge 将 DCP 翻译为 MCP，使 Claude Desktop 等 MCP 宿主零配置接入。DCP 层实测 27.6KB flash / 0.6KB RAM，在 ESP32-WROOM-32 与 ESP32-S3 两块板运行时验证，其余 ESP 目标为构建验证。以 pydcp（PyPI）提供 CLI 与 MCP server。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- DCP↔MCP 参考 Bridge，MCP 宿主零配置接入
- CBOR 帧典型调用 19 字节，DCP 层实测 27.6KB flash / 0.6KB RAM
- 能力令牌、范围/单位校验与 dry-run 原语在 Bridge 层强制执行
- 跨 Xtensa 与 RISC-V 的 ESP 家族及 ESP8266 可交叉编译

## 适用场景

- 让 Claude 等 MCP 宿主通过对话控制 ESP32 灯具等实体设备
- 为 MCU 固件定义意图清单并以 MCP server 形式暴露给 LLM
- 在无硬件条件下用模拟器演示 LLM 设备控制流程

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L17: > Complementary to MCP — a reference
> L34: A reference Bridge translates **DCP ↔ MCP**, so any MCP-compatible LLM works
> L189: The reference Bridge ships an MCP server that exposes each DCP intent as an

## 星数曲线

```mermaid
xychart-beta
    title "device-context-protocol/dcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-10-18 62 → 2026-10-30 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c97b33941453` · [字段定义](../../DATASET.md)*
