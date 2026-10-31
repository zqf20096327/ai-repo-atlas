# acrion/ditana-assistant

⭐ 13 · Python · AGPL-3.0 · 推送 2026-08-11 · [GitHub](https://github.com/acrion/ditana-assistant) · [官网](https://ditana.org/assistant) · 个人维护

**面向终端用户的 LLM 助手：自然语言问答并可建议执行终端命令**

Python 编写的 GUI/CLI 双模式 AI 助手，用户以自然语言提问，应用调用 LLM（默认本地 Ollama + Phi-4-mini，无 API key 即可用）生成回答；可分析输入并建议、经确认后执行终端命令实现 OS 交互。支持任何 OpenAI 兼容接口（OpenAI/Groq/Together AI/LM Studio 等）及 KoboldCpp Gemma。可选接入 Wolfram|Alpha Short Answers API 做上下文增强（ICA），并内置带生命周期管理的请求缓存。运行于 Linux/macOS/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认本地 Ollama + Phi-4-mini，无需 API key 或云账号
- 建议并（经用户确认）执行终端命令的 OS 交互能力
- 可选 Wolfram|Alpha 接入的内省式上下文增强（ICA）
- 对 LLM 与 Wolfram|Alpha 查询实现带生命周期管理的缓存

## 适用场景

- 用自然语言查询文件、进程、网络等系统状态并执行对应命令
- 在脚本中嵌入 ditana-assistant 快速生成命令输出
- 离线本地推理下进行私密问答与闲聊（Pastime 模式）

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: It leverages Large Language Models (LLMs) to provide intelligent assistance similar to the native browser interfaces
> L25: - **OS Interaction**: Capable of interacting with the operating system, suggesting and executing terminal commands 
> L30: - **Dual-Mode Operation**: Functions both as a GUI application and a stand-alone terminal tool for quick command ge

## 星数曲线

```mermaid
xychart-beta
    title "acrion/ditana-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1d91ef073c00` · [字段定义](../../DATASET.md)*
