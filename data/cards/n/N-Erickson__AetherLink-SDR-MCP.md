# N-Erickson/AetherLink-SDR-MCP

⭐ 30 · Python · 推送 2026-07-21 · [GitHub](https://github.com/N-Erickson/AetherLink-SDR-MCP) · 个人维护

**让 Claude/LLM 通过 MCP 控制软件无线电的协议解码服务器**

面向 Claude Desktop 等 MCP 客户端的软件定义无线电（SDR）控制服务器：提供 26 个 MCP 工具，支持 RTL-SDR、HackRF One、Nooelec E4000 硬件，可执行 ADS-B 飞机追踪、AIS 船舶追踪、POCSAG 寻呼解码、Meteor-M 气象卫星成像、ISM 频段设备扫描、频谱分析与 FM/AM 音频录制。解码依赖 dump1090、rtl_433、multimon-ng、SatDump 等系统级工具（多为子进程调用）。pip 安装后 --setup 可自动写入 Claude Desktop 配置；设备为独占访问，子进程解码器与 Python SDR 控制不能同时运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 26 个 MCP 工具覆盖 SDR 控制、频谱分析、录音与多协议解码
- 支持 RTL-SDR / HackRF One / Nooelec E4000 硬件
- ISM 频段经 rtl_433 可自动解码 200+ 种 433/315/868/915MHz 设备
- aetherlink --setup 自动检测操作系统并写入 Claude Desktop 配置

## 适用场景

- 在 Claude Desktop 里用自然语言追踪附近飞机、船舶
- 扫描解码家用 433MHz 传感器、气象站、门铃信号
- 解码 Meteor-M 气象卫星过境图像与录制 FM 广播

## 场景标签

 · 领域:硬件接口/无线电

## 证据(README 行号)

> L7: Control Software Defined Radios and decode radio protocols through an AI-friendly Model Context Protocol interface.
> L16: - **MCP Integration**: Seamless integration with Claude Desktop and other MCP clients

## 星数曲线

```mermaid
xychart-beta
    title "N-Erickson/AetherLink-SDR-MCP 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-29"]
    y-axis "stars" 27 --> 31
    line [28, 29, 30, 30]
```

2026-10-18 28 → 2026-10-29 30（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1e4a3c620ee4` · [字段定义](../../DATASET.md)*
