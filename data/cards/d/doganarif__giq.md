# doganarif/giq

⭐ 15 · Go · MIT · 推送 2026-06-23 · [GitHub](https://github.com/doganarif/giq) · 个人维护

**Git 包装 CLI：AI 生成 commit 信息与状态分析**

Go 编写的 Git 命令行包装器，保持标准 Git 命令兼容，未知命令透传给系统 Git。AI 功能包括：基于暂存变更自动生成上下文 commit 信息供选择，以及在标准 status 输出上附加 AI 洞察。支持 OpenAI 与 Azure OpenAI 两种提供商，配置向导或 YAML/环境变量均可设置。安装提供 Homebrew、预编译二进制（macOS ARM64/AMD64、Linux x86_64/ARM64）与 Go 源码构建三种途径，需要 Git 与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 根据暂存变更自动生成 commit 信息建议
- giq status 附加 AI 生成的变更洞察
- 支持 OpenAI 与 Azure OpenAI，未知命令透传给系统 Git
- 提供 Homebrew 安装与多平台预编译二进制（macOS/Linux ARM64/AMD64）

## 适用场景

- 不想手写 commit message 时用 AI 建议快速提交
- 在 git status 输出基础上获得变更的 AI 分析
- 保留原有 git 使用习惯，按需使用 AI 增强

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: giq is a Git wrapper that enhances your Git workflow with AI-powered features. It provides intelligent commit messag
> L11: - **AI-Powered Commit Messages**: Automatically generates contextual commit messages based on your staged changes
> L14: - **Git Command Passthrough**: Seamlessly delegates unknown commands to your system's Git

## 星数曲线

```mermaid
xychart-beta
    title "doganarif/giq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7c73771bb82f` · [字段定义](../../DATASET.md)*
