# AlvaroHoux/gito

⭐ 15 · Go · MIT · 推送 2026-02-23 · [GitHub](https://github.com/AlvaroHoux/gito) · 个人维护

**Go CLI：基于暂存 diff 与本地 Ollama 生成 Conventional Commits**

面向使用 Git 的开发者的命令行工具：读取已暂存的变更（git diff --staged），连接本地 Ollama 模型生成符合 Conventional Commits 规范的提交信息，可交互确认或用 -y 静默提交，-m 可临时切换模型。Ollama 不可用时回退为将 diff 与内置系统提示词复制到剪贴板，供粘贴到 ChatGPT、Gemini 或 Claude 等网页 AI。内置 prompt 可用本地 prompt.txt 覆盖。通过 go install 安装，跨 Linux/macOS/Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取暂存 diff 并调用 Ollama 生成 Conventional Commits
- Ollama 离线时回退为复制 diff+提示词到剪贴板
- prompt.txt 可自定义团队提交规则
- 支持 -y 静默提交、-m 指定模型、-d 仅复制 diff

## 适用场景

- 提交前快速生成规范的 commit message
- 团队统一提交信息风格（自定义 prompt 规则）
- 无本地模型时借助网页 AI 手动生成提交信息

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: > A Go-based CLI tool designed to streamline AI-assisted commits. Gito captures your staged changes to provide insta
> L5: Gito acts as a bridge between your code and AI. It natively integrates with Ollama to generate commits automatically

## 星数曲线

```mermaid
xychart-beta
    title "AlvaroHoux/gito 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `02ad04580766` · [字段定义](../../DATASET.md)*
