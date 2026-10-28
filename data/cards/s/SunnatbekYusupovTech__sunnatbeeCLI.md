# SunnatbekYusupovTech/sunnatbeeCLI

⭐ 21 · Shell · MIT · 推送 2026-09-29 · [GitHub](https://github.com/SunnatbekYusupovTech/sunnatbeeCLI) · [官网](https://github.com/SUNNATBEE/sunnatbeeCLI) · 个人维护

**47 个终端 AI CLI 编码代理的交互式统一启动器**

Aidevix CLI 是一个 bash 脚本启动器，用单条 aidevix 命令通过 fzf 交互菜单管理 47 个终端 AI CLI 代理（Claude Code、Codex、Gemini、Aider、Ollama 等），覆盖安装、启动、更新、登录指引与本地使用统计。未安装的 CLI 经许可后自动安装；fzf 缺失时回退到数字菜单。作者定位为面向初学者，README 为乌兹别克语。限制：本体不提供模型输出，不保管 API 密钥；Windows 下需在 Git Bash 中运行。提供 curl 脚本、npm、Scoop、git clone 等安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单命令交互菜单管理 47 个 AI CLI（含状态、provider、登录要求展示）
- 未安装的 CLI 自动安装，fzf 自动下载，agent 定期自动更新
- aidevix --doctor 环境诊断、--add 交互添加 agent、--free 只列免费 agent
- 本地使用统计（仅本机）与 PATH 自动修正、shell 补全

## 适用场景

- 不想记各家安装命令，一条命令安装并启动任意 AI CLI
- 在多个终端 AI 编码代理之间统一选择和切换
- 初学者在 Windows/Linux/macOS 上快速搭建 AI 编码环境

## 场景标签

 · 领域:开发者工具/终端

## 证据(README 行号)

> L48: > ⚠️ **Aidevix nima — va nima EMAS.** Aidevix faqat **ishga tushirgich (launcher)**:
> L60: |🎛️|**Yagona `aidevix` menyusi**|47 ta top AI CLI bitta interaktiv ro'yxatda (status + preview)|

## 星数曲线

```mermaid
xychart-beta
    title "SunnatbekYusupovTech/sunnatbeeCLI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d6fd19c96cd3` · [字段定义](../../DATASET.md)*
