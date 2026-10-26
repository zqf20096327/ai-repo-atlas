# ra1nyxin/immersive-vibration-response-skill

⭐ 52 · Python · MIT · 推送 2026-09-07 · [GitHub](https://github.com/ra1nyxin/immersive-vibration-response-skill) · 个人维护 · 中文 README

**让 AI Agent 主动驱动低功率震动设备的 Codex 触觉反馈 Skill**

由 ESP-IDF 固件与 Python 本地通信桥（监听 127.0.0.1:25363）组成的 Codex skill：Agent 可依据剧情、任务进度、错误与情绪，通过异步 HIT/SET/STOP 命令与 JSON 节奏编排驱动 BLE（GK36 协议）低功率震动设备，命令入队即返回，不阻塞对话或任务。Skill 同时定义 Agent 俏皮、有主见的互动风格。限定 16MB Flash 的 ESP32-S3 开发板，需 Python 3.10+ 与 ESP-IDF 5.5 构建，不适用于未知或高功率设备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 异步 HIT/SET/STOP 命令，入队即返回 QUEUED，不阻塞 Agent 工作
- JSON pattern 节奏编排（周期/概率/抖动/循环）及 heartbeat、celebration 等 6 种内置配方
- ESP32-S3 经 BLE 服务 0x1000 连接 GK36 协议低功率震动设备
- bridge-status 可区分本机桥、串口、编排与 ESP32/BLE 各环节问题

## 适用场景

- 互动游戏或角色扮演中按剧情节点获得主动触觉反馈
- 长时编译或后台任务期间获得节奏化进度提示
- 为具身智能互动实验接入低功率触觉输出通道

## 场景标签

 · 领域:硬件/人机交互

## 证据(README 行号)

> L3: 这是一个面向互动游戏、具身智能互动、模拟、角色扮演和长任务协作的 Codex skill。它把低功率震动设备接入 AI 的互动流程，让 AI 不必等待明确指令，也能依据剧情、事件、进度和氛围主动为**玩家**触发震动反馈；同时让 A
> L18: 通信桥默认只监听本机 `127.0.0.1:25363`。普通 `HIT` 进入后台串口队列后会立即返回 `QUEUED`，因此 AI 可以一边推进对话、编程或游戏，一边让震动在后台发生。
> L31: 本仓库已包含可直接构建的 ESP-IDF 固件项目，项目根目录为 `firmware/`。其默认 Flash 配置为 DIO、80 MHz、16 MB；请使用与该配置匹配的开发板。

## 星数曲线

```mermaid
xychart-beta
    title "ra1nyxin/immersive-vibration-response-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-26 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `172b5d2ee76f` · [字段定义](../../DATASET.md)*
