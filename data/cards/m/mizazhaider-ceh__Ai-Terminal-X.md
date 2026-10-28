# mizazhaider-ceh/Ai-Terminal-X

⭐ 38 · Python · 推送 2026-10-02 · [GitHub](https://github.com/mizazhaider-ceh/Ai-Terminal-X) · 个人维护

**Linux 终端 AI 助手：自然语言转可执行终端命令**

面向 Linux（尤其 Kali Linux）用户的终端辅助工具：输入自然语言，调用 Google Gemini（gemini-2.0-flash）生成对应终端命令，经多层风险检查与用户确认后在 tmux/xfce4-terminal 中执行，并提供命令解释、相关命令建议、历史日志（ai_cmd_x_history.log）与学习问答模式。采用双窗口界面（AI 对话 + 命令执行），支持多语言输入、解释固定为英文。以 Python 脚本形式从源码安装，需 Python 3.8+、tmux、xfce4-terminal 与 Gemini API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成 Kali/Linux 优化的终端命令（Gemini 2.0 Flash）
- 多层风险检查与权限确认，未经许可不执行命令
- 双窗口界面：AI 对话窗 + 命令执行窗
- 命令日志记录与学习模式（入门友好解释）

## 适用场景

- 不熟悉命令行时用自然语言完成终端操作
- 安全测试场景下生成并审查 Kali 工具命令
- 通过解释模式学习命令的作用

## 场景标签

`AI 助手` `网络安全` · 领域:对话与助手

## 证据(README 行号)

> L22: * **AI (Google's Gemini AI)** – Intelligent command generation
> L31: AI-Terminal-X is powered by **Google’s Gemini AI** , making it **exceptionally intelligent** and capable of underst
> L86: pip install -r requirements.txt

## 星数曲线

```mermaid
xychart-beta
    title "mizazhaider-ceh/Ai-Terminal-X 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4c9a22ac782f` · [字段定义](../../DATASET.md)*
