# daniel-c-silva/Clanka

⭐ 13 · Python · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/daniel-c-silva/Clanka) · [官网](https://clanka-eight.vercel.app) · 个人维护

**语音控制的桌面 AI 机器人（Mistral 驱动，含情感表达）**

基于自制底盘的机器人项目：Arduino Nano（C++）控制 2x NEMA 17 步进电机与 A4988 驱动器，Raspberry Pi 3B 运行 Python/Flask 后端，前端为 Vite + React，通过串口/USB 桥接通信。AI 部分接入 Mistral API（需自备 API key），目标是可远程控制的带情感表达的 AI 伴侣。README 自述项目处于极早期（“beginning of the beginnings”），情感动画、唤醒词、整机组装仍在 TODO 中。提供底盘机械图纸与接线蓝图。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Arduino Nano + Raspberry Pi 3B 双板架构，串口/USB 桥接
- 2x NEMA 17 步进电机 + A4988 驱动器，附底盘机械图纸与接线蓝图
- 接入 Mistral API 的对话能力（需自建 .env 配置 key）
- Vite + React 前端与 Flask + PostgreSQL 后端

## 适用场景

- 搭建可远程控制的桌面机器人朋友
- 参考自制底盘、扭矩计算与双板接线方案
- 在树莓派上实验接入 Mistral AI 的对话机器人

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: ## robot friend, still in the begining of the begginings but Clanka is supposed to be an ai friend powered by Mistra
> L47: * **Microcontroller:** Arduino Nano (C++) — may migrate to Uno
> L48: * **SBC:** Raspberry Pi 3B (Python Backend)

## 星数曲线

```mermaid
xychart-beta
    title "daniel-c-silva/Clanka 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e3c3142653ca` · [字段定义](../../DATASET.md)*
