# OpenCognitOS/opencognit-releases

⭐ 4 · 推送 2026-11-23 · [GitHub](https://github.com/OpenCognitOS/opencognit-releases) · [官网](https://opencognit.com) · 组织维护

**在一个窗口中并行运行多个 AI 编码代理的桌面控制台**

本仓库存放 OpenCognit Desktop 的安装包与版本说明（软件本身闭源，仓库不含源码）。该应用在本地同一窗口中并行运行 Claude Code、Codex、Gemini CLI、Kimi、Hermes 等编码 CLI，复用用户已有的订阅账号；提供按目录组织的代理视图、真实终端并排网格、目标描述后分发任务的总控、项目脑图、风险命令确认、任务全程追踪、实时预览与内建 Git 审查提交。支持 Linux（AppImage/deb）与 Windows 10/11（exe，未签名）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个窗口并排运行 Claude Code、Codex、Gemini CLI、Kimi、Hermes
- Orchestrator 总控：描述目标后由其分发工作给各代理
- Guardrails 风险命令需人工确认后执行
- 任务墙从开始到 commit 全程追踪，内建编辑器与 Git 审查

## 适用场景

- 同时开多个编码 CLI 在同一项目上并行工作
- 用自然语言描述目标，由总控分配给不同代理
- 集中审查代理执行的风险命令并控制提交流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L44: Installers and release notes for **OpenCognit Desktop**, the command center for AI coding agents:
> L63: - **At least one coding CLI**, installed and logged in: Claude Code, Codex, Gemini CLI, Kimi Code or

## 星数曲线

```mermaid
xychart-beta
    title "OpenCognitOS/opencognit-releases 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-10-23 4 → 2026-11-25 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `7b2a40ad4822` · [字段定义](../../DATASET.md)*
