# Aryan-mor/tinyfix-hotkey

⭐ 3 · C# · MIT · 推送 2026-11-24 · [GitHub](https://github.com/Aryan-mor/tinyfix-hotkey) · 个人维护

**给终端用户一键修正/翻译/改写所选文本的系统托盘工具**

C#/Avalonia 编写的桌面工具：在任何应用中选中文字后按快捷键，修正、翻译或改写结果就地替换原文，附带环形技能菜单与撤销提示。接入 Google、OpenRouter 或任意 OpenAI 兼容端点，密钥加密存储，可自定义技能（名称、输入模式、提示词、快捷键）。另含不依赖 AI 的键盘布局纠错功能。Windows 提供安装包与便携版，macOS/Linux 包状态为仅在 CI 构建测试，Linux 需 X11。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选中文字按快捷键就地替换，无需复制粘贴或切换浏览器
- 支持 Google、OpenRouter 及任意 OpenAI 兼容端点，密钥用 Windows DPAPI 加密
- 自定义 AI 技能：各自提示词、输入模式与快捷键
- 键盘布局错打转换无需 AI 模型和网络

## 适用场景

- 聊天、邮件、编辑器里一键修正正在输入的句子
- 选中文字直接翻译成原文所在语言之外的处理结果
- 把用错误键盘布局打出的字符转换回目标语言
- 为常用 AI 提示词配置专属快捷键调用

## 场景标签

`AI 写作` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: TinyFix fixes, translates and rewrites the text you are typing, right where you type it: in chat, mail, your editor 
> L17: - **Your model, your keys.** Google, OpenRouter or any OpenAI-compatible endpoint (including one running on your ow


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7ad7e3fed67d` · [字段定义](../../DATASET.md)*
