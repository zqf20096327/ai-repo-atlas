# AvantMaker/ESP32_AI_Connect

⭐ 41 · C++ · MIT · 推送 2025-12-15 · [GitHub](https://github.com/AvantMaker/ESP32_AI_Connect) · [官网](https://www.AvantMaker.com) · 组织维护

**让 ESP32 微控制器统一接入多家 AI API 的 Arduino 库**

面向 IoT 开发者的 Arduino 库：以单一接口连接 OpenAI、Gemini、Claude、DeepSeek、xAI Grok 及 OpenAI 兼容平台，支持工具调用、流式通信、自动重试与错误分类。为适配 ESP32 有限内存，采用共享 JSON 缓冲、可按需启用/禁用平台与功能以缩减二进制体积。依赖 ArduinoJson（≥7.0.0），可通过 Arduino IDE Library Manager 或手动 ZIP 安装，附用户指南与配置头文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单接口对接 OpenAI/Gemini/Claude/DeepSeek/Grok 及 OpenAI 兼容平台
- 工具调用与线程安全的流式通信支持
- 可选自动重试：WiFi 健康检查、指数退避、错误分类
- 可配置裁剪平台与功能以降低内存占用

## 适用场景

- 在 ESP32 项目中接入大模型 API 实现对话或 AI 助手
- 让 AI 通过工具调用读取传感器数据或控制硬件
- 资源受限设备上按需裁剪平台支持以节省内存

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L17: ESP32_AI_Connect is an Arduino library that enables ESP32 microcontrollers to interact seamlessly with popular AI A
> L27: - **Multi-platform support**: Single interface for different AI providers

## 星数曲线

```mermaid
xychart-beta
    title "AvantMaker/ESP32_AI_Connect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `04530833913b` · [字段定义](../../DATASET.md)*
