# AtharvGogia/Inkling-for-Windows

⭐ 3 · C# · MIT · 推送 2026-11-14 · [GitHub](https://github.com/AtharvGogia/Inkling-for-Windows) · [官网](https://github.com/AtharvGogia/Inkling-for-Windows/releases/latest) · 个人维护

**Windows 任意输入处快捷键调用 AI 生成短答案的工具**

Inkling 是 Windows 托盘应用：按 Ctrl+Alt+Space 在任意可输入位置键入请求，回车后由模型生成的答案被模拟键入到光标处；支持选中文本问答与改写、重试、危险命令红色确认栏、本地 Snippets、按当前应用定制答案形态。默认走 NVIDIA 免费 API（密钥存于 Windows Credential Manager，约 40 次/分钟），可切换到 Claude Code / Gemini CLI 或本机 Ollama/LM Studio 的 OpenAI 兼容端点。安装包面向 Windows 10/11 64 位，含每日更新检查，MIT 许可的个人项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 任意应用中快捷键触发，答案直接键入/粘贴到光标处
- 识别危险命令（rm -rf、DROP TABLE 等）并要求二次确认
- 默认 NVIDIA 免费 API，可切换 Claude Code/Gemini CLI 或 Ollama/LM Studio 本地模型
- 按窗口标题识别应用与语言，适配 bash/PowerShell/Excel/编辑器场景

## 适用场景

- 在终端里把自然语言请求变成可执行的命令
- 选中文本直接翻译、改写语气或转成要点
- 在编辑器中按当前文件语言生成代码片段
- 完全离线地用本机模型获得同样体验

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: Inkling puts a short answer right where you're typing, in any app on Windows. Press a shortcut, type what you want (
> L130: The free key allows about 40 requests a minute. Inkling stays under that and tells you if you hit it. Settings → M
> L134: Inkling can also use a model running on your own computer through Ollama or LM Studio (or any server with the same

## 星数曲线

```mermaid
xychart-beta
    title "AtharvGogia/Inkling-for-Windows 星数(近 2 点)"
    x-axis ["2026-11-13", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-13 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `754a56c37394` · [字段定义](../../DATASET.md)*
