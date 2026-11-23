# onehumanbeing/esp32-iphone-agent

⭐ 5,227 · Swift · MIT · 推送 2026-11-22 · [GitHub](https://github.com/onehumanbeing/esp32-iphone-agent) · [官网](https://manina.ai?ref=github) · 个人维护 · 中文 README

**用 $7 ESP32 让 AI 视觉模型操控真实 iPhone**

软硬结合的 iPhone 自动化方案：ESP32-S3 板作为 AirPlay 接收端镜像屏幕（H.264 直传，TCP :7201），同时充当 USB/蓝牙 HID 鼠标键盘，配套 iOS 应用解码画面后发送截图给任意 OpenAI 兼容视觉模型，由 planner/actor 两级模型生成点击、滑动、输入等动作，并通过指针追踪、预点抖动校正等机制闭合控制回路。无需 Mac、开发者账号或越狱；每次运行在手机上留有可回放、可导出的 trace。提供 TestFlight 应用、浏览器刷写固件路径，以及可被编码代理调用的 MCP 服务器与 Claude Code 插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AirPlay 镜像（板端 H.264 直传）+ USB/蓝牙 HID 输入组成"眼睛与手"
- planner/actor 双模型架构，可分别指定模型并支持 extra body JSON 定制
- esp32agent CLI 提供 MCP 服务器，可被 Claude Code/Cursor 等编码代理驱动
- 运行留痕：逐步回放、截图与标注导出，供其他 agent 分析

## 适用场景

- 让 AI 代为完成 iPhone 上的 App 操作任务（如打开设置连 Wi-Fi）
- 通过 Siri/快捷方式/控制中心触发已保存的自动任务
- 把 iPhone 作为 MCP 服务器接入本地编码代理工作流
- 在无 Mac、无开发者账号的条件下做 iOS UI 自动化实验

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L89: - **Brain — the app.** The app decodes the stream, sends screenshots to any OpenAI-compatible vision model, and run
> L90:  a planner and an actor: tap, swipe, draw, type, press keys, go home, finish. It runs in the background while it
> L216: - Any OpenAI-compatible vision endpoint works (vLLM, SGLang, llama.cpp, Ollama, cloud APIs). The app lists the

## 星数曲线

```mermaid
xychart-beta
    title "onehumanbeing/esp32-iphone-agent 星数(近 27 点)"
    x-axis ["2026-10-20", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 3078 --> 5422
    line [3273, 3461, 3549, 3623, 3764, 3867, 3939, 4005, 4058, 4094, 4131, 4153, 4191, 3764, 4681, 4809, 4850, 4888, 4911, 4950, 4990, 5027, 5067, 5106, 5158, 5189, 5227]
```

2026-10-20 3,273 → 2026-11-23 5,227（+1,954）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `93529f5acb81` · [字段定义](../../DATASET.md)*
