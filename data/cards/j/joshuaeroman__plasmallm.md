# joshuaeroman/plasmallm

⭐ 30 · QML · GPL-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/joshuaeroman/plasmallm) · 个人维护

**KDE Plasma 6 桌面 LLM 聊天小组件，集成系统信息与命令执行**

面向 KDE Plasma 6 用户的桌面 AI 助手小组件，也提供独立窗口应用形态。连接 Ollama、LM Studio、OpenAI、Anthropic Claude、Google Gemini 等多种 LLM 端点及任意 OpenAI 兼容 API，可收集硬件/系统信息作为上下文，通过工具调用系统读写文件、执行 shell 命令、抓取网页，支持 DuckDuckGo/SearXNG 搜索、图像附件、语音输入（OpenAI 兼容转写 API 或本地 Whisper CLI）及 KWallet 密钥管理。README 注明定位为快速任务与系统集成，不替代完整聊天应用；Flatpak 构建未做沙箱隔离。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Provider 接入：Ollama、LM Studio、OpenAI、Claude、Gemini 及任意 OpenAI 兼容 API
- 工具调用系统：文件操作、shell 命令（可用第二模型校验）、网页抓取，均需用户批准
- 语音输入：OpenAI 兼容转写 API 或本地 Whisper CLI
- Agent Skills（SKILL.md）按需加载，附 create-skill 助手

## 适用场景

- 在桌面小组件中直接向 LLM 提问并执行建议的终端命令
- 让助手读取系统信息回答本机技术问题
- 通过语音输入与桌面 LLM 对话

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: PlasmaLLM is a system-aware AI assistant widget for the KDE Plasma 6 desktop. It provides a native interface to vari
> L15: - **Multi-Provider Support**: Connects to Ollama, LM Studio, OpenAI, Anthropic Claude, Google Gemini, OpenCode Zen/

## 星数曲线

```mermaid
xychart-beta
    title "joshuaeroman/plasmallm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d34efb51e454` · [字段定义](../../DATASET.md)*
