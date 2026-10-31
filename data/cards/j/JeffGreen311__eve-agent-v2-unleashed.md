# JeffGreen311/eve-agent-v2-unleashed

⭐ 42 · Python · MIT · 推送 2026-09-17 · [GitHub](https://github.com/JeffGreen311/eve-agent-v2-unleashed) · 个人维护

**本地优先的自主 AI 编程 agent，经 Ollama 运行**

面向开发者的自主编程智能体：读取项目后自主完成规划、写代码、跑测试、修复错误与验证，最多支持 40 轮工具调用循环，工具覆盖 bash、文件 I/O、grep、git、web 搜索与截屏/OCR/GUI 操作。模型通过本地 Ollama 运行（默认 Eve Qwen 合并模型），可中途切换到 Ollama 云端的 MiniMax M3/Qwen 大参数模型，v2.2 起按复杂度增量自动升降级路由。附带 112 个子 agent、111 个斜杠命令、273 个技能模块、Quest 任务队列、RPG 经验系统与 Telegram 通知，UI 为 FastAPI Web 服务。要求 Python 3.11+、已安装 Ollama，GPU 推荐（4GB VRAM 起）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 最多 40 轮工具调用的规划-执行-验证-自纠循环
- 本地 Ollama 模型与云端 MiniMax M3 按复杂度中途升降级切换
- 112 个子 agent、111 个斜杠命令、273 个技能模块
- 截屏、OCR 屏幕分析与 GUI 交互（经 OpenClaw）的计算机视觉工具

## 适用场景

- 用一句自然语言描述需求，让 agent 自主完成多文件编码与测试
- 本地 GPU 上离线运行编程 agent，按需升级到云端大模型
- 通过 Telegram 远程接收任务完成通知并与 agent 对话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: Eve is an autonomous coding agent that **plans, executes, and verifies** multi-step programming tasks without hand-
> L26: Eve: [reads project] → [plans approach] → [writes 6 files] →
> L27:      [runs tests] → [fixes 2 errors] → [verifies it works] → Done ✓

## 星数曲线

```mermaid
xychart-beta
    title "JeffGreen311/eve-agent-v2-unleashed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b1020dc823b0` · [字段定义](../../DATASET.md)*
