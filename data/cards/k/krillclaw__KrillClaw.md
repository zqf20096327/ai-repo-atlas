# krillclaw/KrillClaw

⭐ 195 · Zig · NOASSERTION · 推送 2026-03-02 · [GitHub](https://github.com/krillclaw/KrillClaw) · [官网](https://krillclaw.com) · 个人维护

**Zig 编写的微型 AI agent 运行时，可跑在微控制器上**

以 Zig 编写的自主 AI agent 运行时，约 450KB 二进制、零依赖、启动 <10ms，目标硬件从 $3 微控制器到云服务器。核心机制：多 provider HTTP 客户端（Claude/OpenAI/Ollama 及 OpenAI 兼容 API）、工具执行循环、SSE 流式解析、编译期 profile（coding/iot/robotics）裁剪工具集。另含 cron 调度、持久 KV 存储、MCP 支持、7 种消息通道、GPIO/I2C/SPI 硬件控制与 BLE/Serial 传输，面向嵌入式与边缘设备开发者，用 zig build 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ~450KB 二进制、零依赖、编译期 profile 裁剪工具集（coding/iot/robotics）
- 支持 20+ LLM provider：Claude/OpenAI/Ollama 及 OpenAI 兼容 --base-url
- MCP 集成与 7 种消息通道（Telegram/Discord/Slack 等）
- GPIO/I2C/SPI 硬件控制与 BLE/Serial 嵌入式传输，固定 arena 分配器

## 适用场景

- 在微控制器或低内存设备上运行 LLM agent
- 通过 BLE/Serial 桥接让边缘设备调用云端 LLM
- 以 daemon 模式定时执行传感器巡检等 agent 任务
- 通过 Telegram/Discord 等通道与 agent 交互

## 场景标签

 · 领域:嵌入式/边缘 AI 基础设施

## 证据(README 行号)

> L22: KrillClaw is an autonomous AI agent runtime written in Zig. It connects to 20+ LLM providers (Claude, OpenAI, Ollam
> L154: KrillClaw supports **20+ LLM providers** through three protocol backends. Any provider with an OpenAI-compatible A

## 星数曲线

```mermaid
xychart-beta
    title "krillclaw/KrillClaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 193 --> 196
    line [194, 195, 195]
```

2026-10-18 194 → 2026-10-22 195（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `38c756bf7b8f` · [字段定义](../../DATASET.md)*
