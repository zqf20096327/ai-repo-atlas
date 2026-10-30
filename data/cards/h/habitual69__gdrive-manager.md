# habitual69/gdrive-manager

⭐ 15 · Python · 推送 2026-03-06 · [GitHub](https://github.com/habitual69/gdrive-manager) · 个人维护

**让 AI 编码助手全面管理 Google Drive 的 Agent Skill**

遵循 Agent Skills 开放标准（SKILL.md + Python 脚本）的技能包，使 AI agent 可对 Google Drive 执行文件/文件夹增删改查、递归上传下载（Office 与 Workspace 格式互转）、按名称/全文/类型搜索及共享权限管理；破坏性操作在代码层面强制两步人工确认。同一技能文件夹可在 Claude Code、Gemini CLI、Codex CLI、Kilo、Kiro、OpenCode、GitHub Copilot 等助手原生使用，支持 npx skills 或 git clone 安装，需 Python 3.10+、Google OAuth 凭据并启用 Drive/Docs/Sheets/Slides 四个 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件/文件夹 CRUD、递归上传下载与 Office↔Workspace 格式互转
- 按名称/全文内容/MIME 类型/父文件夹搜索
- 破坏性操作代码级强制两步人工确认
- 同一技能文件夹跨多家 AI 编码助手原生复用

## 适用场景

- 让 Claude Code/Copilot 等 AI 助手代为整理、搜索我的 Google Drive 文件
- 把项目文件夹递归上传到 Drive 或下载为 Office 格式
- 通过对话管理文件共享权限并保留人工确认安全门

## 场景标签

 · 领域:开发工具/云存储自动化

## 证据(README 行号)

> L18: `gdrive-manager` is a single **Agent Skill** following the Agent Skills open standard — a `SKILL.md` + executable P
> L26: Because it follows the open Agent Skills standard, the **same skill folder works natively** across every major AI c

## 星数曲线

```mermaid
xychart-beta
    title "habitual69/gdrive-manager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `4bba6727c6dd` · [字段定义](../../DATASET.md)*
