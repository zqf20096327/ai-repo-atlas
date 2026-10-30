# qingshan/dotfiles

⭐ 15 · Shell · MIT · 推送 2026-10-01 · [GitHub](https://github.com/qingshan/dotfiles) · 个人维护

**macOS/Linux 开发环境 dotfiles：终端、Shell、编辑器与 AI CLI 配置**

个人开发环境配置仓库，通过 make 一键安装 vim、fish、tmux、herdr 等配置，覆盖 macOS 与 Linux 桌面、开发环境、服务器与容器场景。语言工具链含 Rust/Python/Java/Node/Go，桌面统一在 macOS 与 Omarchy 间使用相同快捷键。AI 部分：make ai 命令安装 Claude Code、GitHub Copilot、OpenAI Codex 等 AI CLI 工具，herdr 集成在 ghostty 中作为 AI agent 终端；去掉 AI 部分其余配置仍完整可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- make / make desktop / make ai 分层安装，覆盖桌面到容器场景
- herdr 集成 ghostty 作为 AI agent 终端
- fish 集成 starship/fzf/zoxide 等 CLI 工具链
- 支持 Docker / Apple Container 环境下测试

## 适用场景

- 快速在新机器上复现统一开发环境
- macOS 与 Linux 桌面间保持一致快捷键与工具链
- 安装并配置常用 AI CLI 编码工具

## 场景标签

 · 领域:开发者工具/系统配置

## 证据(README 行号)

> L21: For AI CLI tools, run:
> L123: - Claude Code

## 星数曲线

```mermaid
xychart-beta
    title "qingshan/dotfiles 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `818feafc06df` · [字段定义](../../DATASET.md)*
