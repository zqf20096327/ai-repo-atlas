# lacymorrow/lacy

⭐ 29 · Shell · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/lacymorrow/lacy) · [官网](https://lacy.sh) · 个人维护

**无需前缀的智能 shell：命令进 shell，问题进 AI 编程工具**

嵌入 zsh、Bash 4+ 和 fish 的 shell 层：按 Enter 时通过词表和首词是否为命令的启发式判断（不经 AI），把输入行分别送往 shell 或用户已装的 AI 编程工具（claude、opencode、copilot、aider 等，或自定义命令），也可用 ! 和 @ 前缀强制指定去向。提问时携带目录、git 分支、最近命令与 tmux/iTerm2 等可见终端输出作为上下文。提供 curl 安装脚本、npx 与 brew 安装方式，配置存于 ~/.lacy/config.yaml，安装时发送匿名事件（可用 DO_NOT_TRACK=1 关闭）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 启发式分流（非 AI）自动判定输入进 shell 还是 agent
- 支持 10 种 AI 编程工具或自定义命令
- 提问自动携带目录、git 分支、最近命令与终端可见输出上下文
- zsh 中实时显示输入去向标记（$ / ?）

## 适用场景

- 在同一个提示符里混用 shell 命令和 AI 问答，省去切换工具
- 让 AI 工具感知我的终端上下文来排查问题
- 命令失败后一键把意图改发给 agent 处理

## 场景标签

 · 领域:开发者工具/终端

## 证据(README 行号)

> L7: Talk to your shell. Commands run in your shell, and questions go to the AI coding tool you already use.
> L29: Lacy runs in zsh, Bash 4+ and fish on macOS, Linux and WSL. It works with lash, claude, opencode, gemini, codex, he

## 星数曲线

```mermaid
xychart-beta
    title "lacymorrow/lacy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `25a55a857eb3` · [字段定义](../../DATASET.md)*
