# copywriting-software/ai-assistant-for-writing

⭐ 3 · Rust · 推送 2026-11-19 · [GitHub](https://github.com/copywriting-software/ai-assistant-for-writing) · [官网](https://copywriting-software.github.io/ai-assistant-for-writing/) · 个人维护

**macOS 系统级 AI 写作助手：ghost text 补全、语法/布局修复**

以 Rust 实现并配合 Swift 原生层（AppKit + AXUIElement + CGEventTap）的 macOS 写作助手，在系统与第三方应用（Notes、TextEdit、Mail、Chrome、Telegram、Slack）中显示光标旁的 ghost text 补全，支持 Tab 整段接受、按词接受与 Esc 隐藏。提供 ⌘⇧G 语法/错误键盘布局修复（ghbdtn→привет）与 ⌘⇧R 文本改写（concise/professional 等风格）。通过 git clone 源码构建，配置文件为 TOML 格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 系统级 ghost text 补全，结合活动应用、窗口标题与光标后文本生成上下文
- 本地记忆与 fast-path：已接受短语本地提示，0 ms 且不调用 LLM
- 错误键盘布局本地修复（EN↔RU）与语法/标点改写
- Privacy Guard 屏蔽密码字段、密码管理器、终端及含 API key/银行卡号的文本

## 适用场景

- 在任意 macOS 应用中获得输入位置的文本续写提示
- 修复误用英文键盘输入的俄语文本
- 对选中片段按指定风格改写
- 在密码框和敏感文本处阻止 AI 读取

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: Фоновый AI-ассистент для письма на **Rust** и нативном слое **macOS** (`AppKit` + `AXUIElement` + `CGEventTap`). Раб
> L17: - **Local-First + BYOK**: работает с бесплатной локальной моделью **Ollama** (`qwen2.5:1.5b`), OpenAI-совместимым A


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `2ff1ba85eb08` · [字段定义](../../DATASET.md)*
