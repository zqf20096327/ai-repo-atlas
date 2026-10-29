# LingaoM/zbot

⭐ 34 · C · Apache-2.0 · 推送 2026-04-17 · [GitHub](https://github.com/LingaoM/zbot) · 个人维护

**运行在 Zephyr RTOS 上的嵌入式 AI agent，用 LLM 控制硬件**

基于 Zephyr RTOS 的开源嵌入式 AI agent 固件：实现 ReAct 循环，通过 HTTPS 调用任意 OpenAI 兼容的 Chat Completions API（默认 OpenRouter，可配置 OpenAI/DeepSeek/本地 Ollama），以 tool_exec/read_skill 两个 LLM 可见工具调度开机自注册的技能（GPIO 读写/闪烁/SOS、系统信息等）。对话历史用 10 节点静态内存池，满时由 LLM 压缩为滚动摘要写入 NVS。支持 nRF7002-DK 与 native_sim 仿真，经串口 shell 或 Telegram Bot 交互。需自建 Zephyr 开发环境编译烧录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct 循环（每轮最多 10 次迭代）连接 OpenAI 兼容 LLM API
- 技能经 SYS_INIT 自注册，LLM 通过 tool_exec 按名调度
- 对话内存满时 LLM 压缩为滚动摘要并 NVS 持久化
- Telegram Bot 长轮询线程转发消息给 agent

## 适用场景

- 在开发板上通过自然语言控制 LED 等 GPIO 外设
- 通过 Telegram 远程对话操控嵌入式设备
- 在 native_sim 上无硬件仿真体验嵌入式 agent
- 按 SKILL.c/SKILL.md 模板扩展自定义技能

## 场景标签

 · 领域:嵌入式/IoT

## 证据(README 行号)

> L3:  An open-source embedded AI agent powered by Zephyr RTOS
> L4:  zbot implements a ReAct (Reason + Act) loop that connects to any OpenAI-compatible LLM API,
> L5:  enabling hardware control, persistent memory, and multi-step skills.

## 星数曲线

```mermaid
xychart-beta
    title "LingaoM/zbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-29 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `43f40d9aac53` · [字段定义](../../DATASET.md)*
