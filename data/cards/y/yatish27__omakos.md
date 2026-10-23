# yatish27/omakos

⭐ 149 · Shell · MIT · 推送 2026-04-18 · [GitHub](https://github.com/yatish27/omakos) · 个人维护

**macOS 开发环境一键初始化脚本**

受 Omakub 启发的 shell 脚本，单条命令将新 macOS 笔记本配置为开发环境：通过 Homebrew 与 Brewfile 安装命令行工具（Git/ZSH/fzf 等）、开发环境（Cursor、Neovim、Docker、PostgreSQL、Redis、Ollama、Mise 管理多语言运行时）、生产力应用与字体，并应用开发者导向的系统设置。脚本幂等可重复运行、模块化可单独执行，支持修改 Brewfile 与配置文件自定义。面向 macOS 开发者的新机初始化场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条 curl 命令完成整套开发环境安装
- 所有包通过 Homebrew/Brewfile 统一管理
- 脚本幂等，可重复运行，按需安装或跳过
- scripts/ 目录各脚本可独立运行与自定义

## 适用场景

- 新 Mac 到手后一条命令装好开发环境
- 只需配置系统设置或 Git 时单独运行对应脚本
- 按自己需求改 Brewfile 定制装机清单

## 场景标签

 · 领域:开发工具/系统配置

## 证据(README 行号)

> L5: > Omakos turns your macOS laptop into a fully functional development machine in a single command.
> L74: - Cursor - AI-powered code editor
> L84: - Ollama for local AI models

## 星数曲线

```mermaid
xychart-beta
    title "yatish27/omakos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 148 --> 150
    line [149, 149]
```

2026-10-18 149 → 2026-10-23 149（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `1014c3f07090` · [字段定义](../../DATASET.md)*
