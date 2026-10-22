# tninja/aider.el

⭐ 682 · Emacs Lisp · Apache-2.0 · 推送 2026-10-04 · [GitHub](https://github.com/tninja/aider.el) · 个人维护 · 中文 README

**在 Emacs 中使用 Aider 进行 AI 辅助编程的界面**

为 Emacs 用户提供与终端 AI 结对编程工具 Aider 交互的 Elisp 包：通过 comint 建立 git 仓库专属会话，支持 transient/Helm 菜单、代码重构、就地实现 TODO 注释、生成单元测试、代码问答等命令，并提供带语法高亮与 yasnippet 支持的 prompt 文件管理工作流。配置通过 aider-args 直传 Aider CLI，需 Emacs >= 26.1 及 Aider、Transient、Magit、Markdown-mode 依赖，经 MELPA、package-vc-install、Straight 或 Doom 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- comint 式 git 仓库专属 Aider 会话，可多仓库并行
- 就地实现 TODO/注释、区域重构、单元测试生成等命令
- 仓库专属 prompt 文件，支持语法高亮、补全与 yasnippet 片段
- 支持 MELPA、package-vc-install、Straight、Doom 多种安装方式

## 适用场景

- 不离开 Emacs 即可与 Aider 进行 AI 辅助编码
- 在大型 monorepo 子目录内启动受限范围的 Aider 会话
- 通过 prompt 文件组织并复用 AI 编程任务提示词

## 场景标签

 · 领域:开发工具/AI 辅助编程

## 证据(README 行号)

> L26: - [[https://github.com/paul-gauthier/aider][Aider]] is a well-known and highly effective AI pair programming tool f
> L28: - The aider.el package offers an simple UI to communicate with Aider in Emacs. It aim to minimize the user's effort

## 星数曲线

```mermaid
xychart-beta
    title "tninja/aider.el 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 681 --> 683
    line [682, 682]
```

2026-10-18 682 → 2026-10-22 682（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `167a05448a5c` · [字段定义](../../DATASET.md)*
