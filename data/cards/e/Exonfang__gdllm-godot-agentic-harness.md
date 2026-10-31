# Exonfang/gdllm-godot-agentic-harness

⭐ 39 · GDScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Exonfang/gdllm-godot-agentic-harness) · 个人维护

**Godot 编辑器内的 LLM agentic harness：连接任意模型驱动编辑器内 agent**

以 Godot 插件形式嵌入编辑器的 agentic harness：通过 API 连接任意 LLM 提供商（原生支持 Ollama、OpenAI、Anthropic、Gemini，或经 OpenAI 兼容适配器接入其他），也可绑定 ChatGPT 订阅登录。Agent 获得读码、写文件、场景/资源编辑、运行调试、游戏内省等编辑器工具，所有动作对用户透明并保存会话日志。采用渐进披露策略压缩上下文，支持子 agent、权限门控、技能与自定义工具（需人工审批后加载）。安装方式为下载 release zip 解压到项目目录并启用插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生支持 Ollama/OpenAI/Anthropic/Gemini，其余经 OpenAI 兼容适配接入，或用 ChatGPT 订阅登录
- 覆盖读码、写文件、场景/资源编辑、运行调试、游戏内省与输入驱动的编辑器工具集
- 所有 agent 动作透明展示，会话日志本地保存，权限门控与循环失控中断
- 支持 /skills/ 与 /gdllm-tools/ 自定义工具（新工具需人工审批加载）、子 agent 与缓存感知压缩

## 适用场景

- 在 Godot 编辑器内用对话驱动 agent 完成脚本编写、场景编辑与调试
- 接入本地 Ollama 或自有 API 模型在编辑器内执行游戏开发任务
- 让 agent 在运行中的游戏里读取 UI、发送输入、分析性能与错误

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A fully transparent in-editor agentic harness for large language models inside the Godot Engine. Connect to any LLM 
> L77: - Using the **Connections** button in the session panel, link up your inference providers via API. Supports Ollama,

## 星数曲线

```mermaid
xychart-beta
    title "Exonfang/gdllm-godot-agentic-harness 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-31 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0822a25fe4b0` · [字段定义](../../DATASET.md)*
