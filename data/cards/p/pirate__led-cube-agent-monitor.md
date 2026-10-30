# pirate/led-cube-agent-monitor

⭐ 22 · Python · 推送 2026-07-15 · [GitHub](https://github.com/pirate/led-cube-agent-monitor) · [官网](https://www.amazon.com/dp/B0CGCH393Z) · 个人维护

**在 5×5×5 WLED LED 立方体上实时显示 Codex/Claude 会话状态的 macOS 守护进程**

单文件 Python 标准库实现的 macOS 守护进程 agent_cube.py：读取 Claude hooks 与 Codex 会话状态，通过 DDP 协议直接驱动 WLED LED 立方体，五个纵向平面按 iTerm 窗格顺序对应五个 agent 会话。提供思考中、流式输出、等待工具、空闲、错误等六种状态动画。一行 pip 命令安装并完成 LaunchAgent 注册；无需 Home Assistant。默认参数针对特定 Treedix WS2812B 硬件，可用命令行参数与环境变量覆盖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件实现，仅依赖 Python 标准库
- 通过 DDP 直连 WLED，无需 Home Assistant
- 六种会话状态对应不同动画（思考/流式/等待工具/空闲/错误等）
- 一行命令完成安装与 macOS LaunchAgent 后台服务注册

## 适用场景

- 在桌面 LED 立方体上远程观察多个 Claude/Codex 终端会话的状态
- 为自建 WLED 灯效改造自定义 agent 状态动画
- 同时跑多个 AI 编程会话时用余光判断哪些在等待输入

## 场景标签

 · 领域:开发工具/硬件可视化

## 证据(README 行号)

> L3: A tiny macOS daemon that shows live Codex and Claude session states on a
> L21: This installs the package, then performs the one-time macOS setup: it merges Claude hooks,

## 星数曲线

```mermaid
xychart-beta
    title "pirate/led-cube-agent-monitor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7b5f159b8cfb` · [字段定义](../../DATASET.md)*
